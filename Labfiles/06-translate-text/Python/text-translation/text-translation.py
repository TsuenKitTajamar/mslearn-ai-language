from dotenv import load_dotenv
import os, uuid
import requests

def main():
    global translator_endpoint
    global cog_key
    global cog_region

    try:
        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')
        translator_endpoint = 'https://api.cognitive.microsofttranslator.com'

        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Detect the language
            language = GetLanguage(text)
            print('Language:',language)

            # Translate if not already English
            if language != 'en':
                translation = Translate(text, language)
                print("\nTranslation:\n{}".format(translation))
                
    except Exception as ex:
        print(ex)

def GetLanguage(text):
    # Default language is English
    language = 'en'

    # Use the Azure AI Translator detect function
    path = '/detect'
    url = translator_endpoint + path
    params = {
        'api-version': '3.0'
    }
    headers = {
        'Ocp-Apim-Subscription-Key': cog_key,
        'Ocp-Apim-Subscription-Region': cog_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    language = response[0]['language']

    # Return the language
    return language

def Translate(text, source_language):
    translation = ''

    # Use the Azure AI Translator translate function
    path = '/translate'
    url = translator_endpoint + path
    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': 'en'
    }
    headers = {
        'Ocp-Apim-Subscription-Key': cog_key,
        'Ocp-Apim-Subscription-Region': cog_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    translation = response[0]['translations'][0]['text']

    # Return the translation
    return translation

if __name__ == "__main__":
    main()