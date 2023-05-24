""" api test """

import os
import requests
import time
from pathlib import Path
from dotenv import load_dotenv
from escriptorium_connector import EscriptoriumConnector


if __name__ == '__main__':

    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)

    ESCRIPTORIUM_USERNAME = os.environ.get('ESCRIPTORIUM_USERNAME')
    ESCRIPTORIUM_PASSWORD = os.environ.get('ESCRIPTORIUM_PASSWORD')
    ESCRIPTORIUM_TOKEN = os.environ.get('ESCRIPTORIUM_TOKEN')
    ESCRIPTORIUM_SERVER = os.environ.get('ESCRIPTORIUM_SERVER')

    url = ESCRIPTORIUM_SERVER
    escr = EscriptoriumConnector(url, ESCRIPTORIUM_USERNAME, ESCRIPTORIUM_PASSWORD)
    doc_pk = 102 # 'test' document in 'test-api' project
    print('Dokument:', escr.get_document(doc_pk).name)

    # first file of the document
    file = escr.get_document_parts(doc_pk).results[0].filename
    part_pk = escr.get_document_parts(doc_pk).results[0].pk
    print(file)
    print(part_pk)

    #model_pk = 64 # model 'chrobierz_wislica'
    #model_pk = 62 # model 'corticelli'
    model_pk = 65  # model 'chrobierz_wislica_olesnica_oblekon'

    http = requests.Session()
    http.headers.update({"Accept": "application/json"})
    http.headers.update({"Authorization": f"""Token {ESCRIPTORIUM_TOKEN}"""})

    # note: each of these steps takes, even for a single page, several seconds

    # automatic segmentation, eScriptorium has a built-in default model for segmentation
    # but I don't know how to get its pk, so I added a copy under a different name to the explicit model list
    # where it got pk = 68
    model_segm = 68
    dane = {"parts": [part_pk], "model": model_segm, "steps":"both"}
    result = http.post(f"{escr.api_url}documents/{doc_pk}/segment/", dane)
    print(result)

    # time.sleep(10) - how to check if the segmentation and transcription, which often take several seconds, have already been done

    # automatic transcription
    dane = {"parts": [part_pk], "model": model_pk}
    result = http.post(f"{escr.api_url}documents/{doc_pk}/transcribe/", dane)
    print(result)
