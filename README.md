# llm-fact-check

# Welcome to LLM Fact Checker! 🚀🤖

Hi there,  our main goal is to ensure that we provide accurate and reliable information to our users. To achieve this, we have implemented a robust system that leverages the capabilities of Language Model (LLM) and LangChain Agents.

When we encounter claims or statements, our process involves creating a set of assumptions regarding their truthfulness or falsehood. We understand that assumptions can guide our investigation and help us uncover the veracity of the claims.

To validate these assumptions, we employ various trusted sources such as Google Fact Check, Wikipedia, the Knowledge Graph, and perform comprehensive searches using Google's search engine. These resources enable us to gather relevant and factual information to support or debunk the assumptions made.

In addition to these automated processes, we recognize the importance of human validation. In cases where LLM requires validation or where the information is complex and requires human judgment, we include human validators. These validators play a crucial role in ensuring the accuracy and integrity of the information provided.

By combining the power of LLM, LangChain Agents, and the expertise of human validators, we strive to deliver the most reliable and verified information to our users. Our commitment is to continuously improve our fact-checking methods and enhance the overall user experience.


## Steps to Run the Chat UI

1. Fork this repository or create a code space in GitHub.

2. Install the required Python packages by running the following command in your terminal:
   ```
   pipenv install 
   ```

3. Create a `.env` file in the project directory.
   ```
   OPENAI_API_KEY = 'key'
   API_KEY = 'key'
   GOOGLE_CSE_ID = 'key'
   GOOGLE_API_KEY = 'key'
   ```

4. Run the following command in your terminal to start the chat UI:
   ```
    run fact_check_llm.py 
   ```

   This will launch the chat UI, allowing you to interact with the Falcon LLM model using LangChain.

**Note:** Ensure that you have provided a valid OpenAI key  in the `.env` file, as mentioned in step 3. Please follow https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search 
To create Google Search Envoirment and  GOOGLE_CSE_ID

If you encounter any issues or have questions, please reach out to me .

Enjoy using  LLM as Fact Checker!

