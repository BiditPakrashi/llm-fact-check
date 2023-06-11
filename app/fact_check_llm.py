from dotenv import load_dotenv
import chainlit as cl
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.agents import tool
import factapidoc
import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]


@tool
def check_claim_chain(claim) -> str:
    """  This tool be used as first option and  to break claims in  multiple assumtions \
    Returns  Statement is final statement after fact check  \  
        The input should always be  claim as string, \
        and this function will always looks into the claim then  \
    Make a bullet point list of the assumptions \
        Take every assumtion and do fact check\
        fact check will be outside this function.
        Fact check will be done by other tools"""
    llm = ChatOpenAI(temperature=0)
    template = """{question}\n\n"""
    prompt_template = PromptTemplate(input_variables=["question"], template=template)
    question_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = """Here is a statement:
    {statement}
    Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
    prompt_template = PromptTemplate(input_variables=["statement"], template=template)
    assumptions_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = """Here is a bullet point list of assertions:
    {assertions}
    For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
    prompt_template = PromptTemplate(input_variables=["assertions"], template=template)
    fact_checker_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = (
        f"""In light of the above facts, how would you answer the question '{claim}'"""
    )
    template = """{facts}\n""" + template
    prompt_template = PromptTemplate(input_variables=["facts"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)

    overall_chain = SimpleSequentialChain(
        chains=[question_chain, assumptions_chain, fact_checker_chain, answer_chain],
        verbose=True,
    )

    return overall_chain.run(claim)


@tool
def check_fact_google(statement: str) -> str:
    """Returns If the  statement given as parameter is not empty
    and returns true or false or partly false using  factchain.
    in case of partly false ask Human
    If APIChain response is Empty then use other tool"""
    llm = ChatOpenAI(temperature=0)
    api_key = os.environ["API_KEY"]
    factchain = APIChain.from_llm_and_api_docs(
        llm, factapidoc.GOOGLEFACT_DOCS, verbose=True
    )
    return factchain.run(
        f"Check if it is true for {statement} use  api_key like {api_key}"
    )


@tool
def ask_human(statement: str) -> str:
      """Returns If the  statement given as parameter is not empty
    and returns true or false or partly false using  Human input.
    Use this tool to ask question to Human"""
      cl.Message(
            content=f"{statement}",
        ).send()

def top5_results(query):
    search = GoogleSearchAPIWrapper()
    return search.results(query, 5)


def initialize_tools(llm):

    google_search_tool = Tool(
        name = "Google Search",
        description="Search Google for checking the statement is true or false or partially false and return to next tool",
        func=top5_results
    )
    tools = load_tools(["llm-math", "wikipedia", "human"], llm=llm)
    tools = tools + [
        check_claim_chain,
        check_fact_google,
        PythonREPLTool(),
        google_search_tool,
        ask_human
    ]
    return tools


@cl.langchain_factory
def agent():
    llm = ChatOpenAI(temperature=0)
    tools = initialize_tools(llm)
    print(tools)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True,
    )
    return agent


@cl.langchain_run
def run(agent, input):
    res = agent.run([input])
    cl.Message(content=res).send()

if __name__ == "__main__":
    agent_instance = agent()
    input_text = input("Please enter your input text: ")
    run(agent_instance, input_text)
