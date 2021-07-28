### STT
# APIKEy: 0GcD0ZyhaapJ_4lap__tXpxGhOvKu27OHlFbZP2LoS0E
# Region: us-east
# url: https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/eb52bc8c-a66b-45de-94f2-789c0fdb6b85
# models: https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models

### TTS
# APIKEy: wQKfJxiQ2m8GLO2XiVteuPrtm1gOrDphDpYLPUlSbnp4
# Region: us-east
# url: https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/f909583b-89e5-4a94-af24-caa14ffef879

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

APIKEy= 'wQKfJxiQ2m8GLO2XiVteuPrtm1gOrDphDpYLPUlSbnp4'
url= 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/f909583b-89e5-4a94-af24-caa14ffef879'

authenticator = IAMAuthenticator(APIKEy)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#txt = input('Enter a text:- ')

#with open ('./tts.mp3', 'wb') as audio_file:
 #   res = tts.synthesize(txt, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
  #  audio_file.write(res.content)

with open('stt.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)

with open('./tts.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)