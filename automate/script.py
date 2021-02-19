import requests
import json

END_POINT_URL = "http://127.0.0.1:8000/"


def get_all_status():
    r = requests.get(END_POINT_URL+"status/")
    print(r.text)
    print(r.status_code)


def create_status(data):
    r = requests.post("http://127.0.0.1:8000/status/",  data={'content': 'value'})

    print(r.status_code)
    print(r.text)


# get_all_status()
create_status({"content": "Status List"})


