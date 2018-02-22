""" get/post wrapper functions for hitting server retrieval routes"""
import requests

url = 'http://localhost:5000/api'

def temp():
    # example get request url
    ret = requests.get("http://localhost:5000/api/retrieve/all?template_id=1")

def post_template(template):
    payload = {"template": template}
    post = requests.post(f"{url}/define", json=payload)

    return post