# flake8: noqa

GOOGLEFACT_DOCS = """API documentation:
Endpoint:  https://factchecktools.googleapis.com/v1alpha1/claims:search HTTP/1.1

GET /search

This API is for searching if a Claim is fact or not .

Query parameters table:
query | string | Claim term, e.g.,Claims of a person or company or historical Events... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search. | required
key | string | Use API_Key from prompt

Response schema (JSON object):
claims[]	
object (Claim)

The list of claims and all of their associated information.


Each object in the "Claim"  has the following schema:
{
  "text": string,
  "claimant": string,
  "claimDate": string,
  "claimReview": [
    {
      object (ClaimReview)
    }
  ]
}

Each object of ClaimReview has following schema:
{
  "publisher": {
    object (Publisher)
  },
  "url": string,
  "title": string,
  "reviewDate": string,
  "textualRating": string,
  "languageCode": string
}

publisher object is like 
{
  "name": string,
  "site": string
}

A complete Response looks like 

{
  "claims": [
    {
      "text": "The Pennsylvania Supreme Court ruled that the 2020 election was rigged",
      "claimant": "Donald Trump",
      "claimDate": "2022-11-04T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "USA Today",
            "site": "usatoday.com"
          },
          "url": "https://www.usatoday.com/story/news/factcheck/2022/11/11/fact-check-2020-election-valid-contrary-trumps-latest-claim-pennsylvania/8318157001/",
          "title": "Fact check: 2020 election was valid, contrary to Trump's latest claim",
          "reviewDate": "2022-11-11T21:01:41Z",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "“It’s not that there is no evidence the election was stolen, but that no court had the guts to HEAR the evidence. They dismissed the cases, NOT the evidence.”",
      "claimant": "Instagram posts",
      "claimDate": "2022-10-25T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2022/oct/28/instagram-posts/trump-campaigns-evidence-of-fraud-was-reviewed-bef/",
          "title": "Courts did review Trump campaign ‘evidence’ of election fraud ...",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "The 2020 election was declared 'illegal'",
      "claimant": "Social media",
      "claimDate": "2022-10-11T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "USA Today",
            "site": "usatoday.com"
          },
          "url": "https://www.usatoday.com/story/news/factcheck/2022/11/04/fact-check-2020-presidential-election-results-still-legitimate-trump-biden/10649174002/",
          "title": "Fact check: 2020 presidential election results are still legitimate",
          "reviewDate": "2022-11-04T15:49:27Z",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "“A STOLEN ELECTION: State totals minus illegal ballot trafficking numbers give President Trump decisive victories in AZ, GA, MI, PA, and WI.”",
      "claimant": "The Gateway Pundit",
      "claimDate": "2022-04-24T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2022/may/04/gateway-pundit/claims-2020-election-was-stolen-are-still-false/",
          "title": "Claims that the 2020 election was stolen are still false",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "A video shows Jim Jordan saying the 2020 “election was stolen.”",
      "claimant": "Facebook posts",
      "claimDate": "2022-12-18T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2022/dec/20/facebook-posts/video-shows-jim-jordan-denying-he-said-election-wa/",
          "title": "Video shows Jim Jordan denying he said the election was stolen",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "The 2020 election “was stolen from Donald J. Trump.”",
      "claimant": "Josh Mandel",
      "claimDate": "2022-02-25T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2022/mar/01/josh-mandel/ohios-mandel-repeats-false-claim-stolen-2020-elect/",
          "title": "Ohio’s Josh Mandel repeats false claim of stolen 2020 election",
          "textualRating": "Pants on Fire",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "“President Joe Biden admits to faking the election.”",
      "claimant": "Instagram posts",
      "claimDate": "2023-02-22T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2023/feb/23/instagram-posts/no-president-joe-biden-didnt-admit-the-2020-presid/",
          "title": "No, President Joe Biden didn’t admit the 2020 presidential election ...",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "“President Trump and I lost an election in 2020 because of a rigged election.”",
      "claimant": "Jim Marchant",
      "claimDate": "2022-10-08T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "PolitiFact",
            "site": "politifact.com"
          },
          "url": "https://www.politifact.com/factchecks/2022/oct/10/jim-marchant/nevada-republican-echoes-trumps-pants-fire-about-r/",
          "title": "Nevada Republican echoes Trump’s Pants on Fire about 'rigged ...",
          "textualRating": "Pants on Fire",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "Did Trump win majority of registered voters in 2020 election?",
      "claimant": "@itspatsworld",
      "claimDate": "2023-04-19T16:14:26Z",
      "claimReview": [
        {
          "publisher": {
            "name": "Newsweek",
            "site": "newsweek.com"
          },
          "url": "https://www.newsweek.com/fact-check-did-trump-win-majority-registered-voters-2020-election-1795364",
          "title": "Fact Check: Did Trump Win Majority of Registered Voters in 2020 ...",
          "reviewDate": "2023-04-19T16:14:26Z",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    },
    {
      "text": "The 2020 presidential election was 'rigged'",
      "claimant": "Donald Trump, social media users",
      "claimDate": "2022-01-06T00:00:00Z",
      "claimReview": [
        {
          "publisher": {
            "name": "USA Today",
            "site": "usatoday.com"
          },
          "url": "https://www.usatoday.com/story/news/factcheck/2022/01/06/fact-check-donald-trump-2020-election-results/9115875002/",
          "title": "Fact check: Donald Trump persists with false claim about 2020 results",
          "reviewDate": "2022-01-06T20:45:43Z",
          "textualRating": "False",
          "languageCode": "en"
        }
      ]
    }
  ],
  "nextPageToken": "CAo"
}

Only look into "textualRating" and tell if it is false or true

"""