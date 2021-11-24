import requests
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
    test_data = "Patient has lung cancer, but did not smoke. She may consider chemotherapy as part of a treatment plan."

    query_post = requests.post(url, headers=headers, auth=auth_data, data=test_data)
    #print(json.dumps(query_post.json(), sort_keys=True, indent=4))
    
    with open('result.json', 'w') as f:
        f.write(json.dumps(query_post.json(), sort_keys=True, indent=4))


if __name__ == "__main__":
    print("#### METODO DE LLAMADO A LA API ####")
    connection_general()