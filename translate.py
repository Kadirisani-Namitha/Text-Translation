import requests
import uuid
import json

# Add your subscription key and endpoint
subscription_key = "ceb2254243c441c1a8a4a2e85396a17e"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global. This is required if using a Cognitive Services resource.
location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': "en",
    'to': ['hi', 'te', 'ka']
}

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceld': str(uuid.uuid4())
}

# You can pass more than one object in the body.
body = [{
    'text': 'Good morning!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ' : ')))



