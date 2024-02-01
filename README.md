# Project Title: Bing Search with GPT-4 Chat

## Overview
This project combines Bing Search API with OpenAI's GPT-4 to create a chat application that retrieves information from Bing search results and uses GPT-4 to generate answers based on the gathered information.

## Prerequisites
Before running the code, make sure you have the following:

- OpenAI API key: Obtain from OpenAI (https://beta.openai.com/signup/).
- Bing Search API key: Obtain from Microsoft Azure (https://azure.microsoft.com/en-us/services/cognitive-services/bing-search-api/).
- Environment Variables: Set up a `.env` file with the following variables:

```dotenv
OPENAI_API_KEY=your_openai_api_key
BING_SEARCH_V7_SUBSCRIPTION_KEY=your_bing_search_api_key
BING_SEARCH_V7_ENDPOINT=your_bing_search_endpoint
```

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your_username/your_repo.git
cd your_repo
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:

```bash
python main.py
```

2. Enter a question when prompted.

3. The script will utilize the Bing Search API to retrieve relevant web pages and then use GPT-4 to generate an answer based on the collected information.

## Configuration
Modify the `.env` file to update API keys and endpoint information.

## Notes
- The Bing Search API and GPT-4 API have usage limits. Ensure that you are within your quota to avoid disruptions.
- The GPT-4 model used in this code is "gpt-4-1106-preview." Update it accordingly based on OpenAI's latest models.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [OpenAI](https://beta.openai.com/) for providing the powerful GPT-4 model.
- [Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/bing-search-api/) for the Bing Search API.

Feel free to contribute and improve this project!
