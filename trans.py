from watson_developer_cloud import LanguageTranslatorV2
#Credencial added from IBM cloud.
language_translator = LanguageTranslatorV2(
	#plz don't share this :)
    username='{5bb173e4-db59-4b54-b55b-f9b34b934c46}',
    password='{0TtwvNoKnSgb}',
    url='{https://gateway.watsonplatform.net/language-translator/api}'
)
#LanguageTranslatorV2 is not no longer exist in watson_developer_cloud :(