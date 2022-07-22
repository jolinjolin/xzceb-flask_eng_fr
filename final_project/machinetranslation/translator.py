import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def e2f_translator(text):
    '''
    translate english to french
    '''
    if text is None:
        return ''
    result = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()["translations"][0]
    return result["translation"]

def f2e_translator(text):
    '''
    translate french to english
    '''
    if text is None:
        return ''
    result = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()["translations"][0]
    return result["translation"]
