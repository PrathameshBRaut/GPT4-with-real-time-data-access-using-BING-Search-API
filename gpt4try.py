import os
import openai
import requests
from pprint import pprint
import dotenv

dotenv.load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
bing_search_api_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
bing_search_endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] 


def search(query):
    # Construct a request
    mkt = 'en-US'
    params = {'q': query, 'mkt': mkt}
    headers = {'Ocp-Apim-Subscription-Key': bing_search_api_key}

    # Call the API
    try:
        response = requests.get(bing_search_endpoint,
                                headers=headers, params=params)
        response.raise_for_status()
        json = response.json()
        if 'webPages' in json:
            return json["webPages"]["value"]
        else:
            print("No search results found.")
            return []
    except Exception as ex:
        print(f"An error occurred: {ex}")
        return []


def chat_with_gpt(prompt):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "do not answer anything rather than question answer in short only use the information in content to answer"},
            {"role": "user", "content": prompt}
        ]
    )

    # Print the answer from OpenAI
    answer = response.choices[0].message['content']
    print(f"Answer: {answer}")


# Continuous chat loop
while True:
    # Prompt the user for a question
    question = input("What is your question? ")

    # Send a query to the Bing search engine and retrieve the results
    results = search(question)

    results_prompts = [
        f"Source:\nTitle: {result['name']}\nURL: {result['url']}\nContent: {result['snippet']}" for result in results
    ]

    prompt = "Use the following sources only to answer the question:\n\n" + \
        "\n\n".join(results_prompts) + "\n\nQuestion: " + question + "\n\nAnswer:"

    print(prompt)

    # Check if there are any results
    if results:
        # Use OpenAI's GPT-4 API to answer the question
        chat_with_gpt(prompt)
    else:
        # Print an error message if there are no results
        print("Error: No results found for the given query.")
