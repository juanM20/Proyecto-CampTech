import json
from ibm_watson import SpeechToTextV1 as Stt
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



def speech_to_text(audio):

        authenticator = IAMAuthenticator('cCRifK-sspu8RhZ41WVx8bT8GWaHBR-sI90MwIHn7YOx')
        speech_to_text = Stt(authenticator = authenticator)

        speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/6c83017a-3519-4b2d-936b-9476a6757492')

        # La variable 'file' contendrá el audio, no sé si vas a usar el método open para abrirlo yo supongo
        # Pero bueno, eso no es problema, simplemente de donde obtengas el file lo abres y lo almacenas en la variable
        # Voy a asumir que ya está creada
        # EN el open iria la ruta

        with open(audio,'rb') as file:

                resultado = speech_to_text.recognize(audio = file,
                        content_type = 'audio/mp3',
                        word_alternatives_threshold = 0.9,
                        model = 'es-MX_BroadbandModel').get_result()
                json_string = json.dumps(resultado,indent=2)
                data_resultado = json.loads(json_string)
                # Este texto es el que pasaremos por todo el procedimiento a partir de la linea 35 del otro archivo jeje
                text = data_resultado['results'][0]['alternatives'][0]['transcript']
                print(text)
        
        return text
