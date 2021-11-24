import requests
from googletrans import Translator
from requests.auth import HTTPBasicAuth
import json
import time
import os

def connection_general():
    url = "https://us-east.wh-acd.cloud.ibm.com/wh-acd/api/v1/analyze/wh_acd.ibm_clinical_insights_v1.0_standard_flow?version=2020-03-31"
    auth_data = HTTPBasicAuth('apikey', 'NzSpCPnTX6NusWbiIq1KrfhPPUCk7jWfMqUjn-yA6tPB')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    test_data = "Paciente con dolor de espalda severo, usaba medicamento Ibuprofeno 800mg, sin historial familiar. Posible tuberculosis."
    translator = Translator()
    test_data_en = translator.translate(test_data, dest='en')

    print("Data español: ",test_data)
    print("Data Ingles:  ",test_data_en.text)

    query_post = requests.post(url, headers=headers, auth=auth_data, data=test_data_en.text)
    #print(json.dumps(query_post.json(), sort_keys=True, indent=4))
    
    with open('result.json', 'w') as f:
        f.write(json.dumps(query_post.json(), sort_keys=True, indent=4))


if __name__ == "__main__":
    print("#### METODO DE LLAMADO A LA API ####")
    connection_general()