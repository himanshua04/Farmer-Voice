#LanguageTranslatorV2 is not no longer exist in watson_developer_cloud :(
from watson_developer_cloud import LanguageTranslatorV3

iimport json
language_translator = LanguageTranslatorV3(
    # Don't default to the current date. Instead, specify a date that matches a 
    # version that is compatible with your app, and don't change it until your app
    # is ready for a later version.
    version='{2018-05-01}',
    username='{5bb173e4-db59-4b54-b55b-f9b34b934c46}',
    password='{0TtwvNoKnSgb}',
    url='{https://gateway.watsonplatform.net/language-translator/api}'
)
#Service end-pt
language_translator.set_url('https://gateway-wdc.watsonplatform.net/language-translator/api')

language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})

translation = language_translator.translate(
    text='Hello',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))