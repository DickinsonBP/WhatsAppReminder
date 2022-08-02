import requests
from requests.structures import CaseInsensitiveDict



url = "https://graph.facebook.com/v13.0/103347919147898/messages"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer TOKEN"
headers["Content-Type"] = "application/json"

for number, name in numbers.items():
    data = '{ "messaging_product": "whatsapp", "to": "%s", "type": "template", "template": { "name": "message_reminder", "language": { "code": "es_ES" } } }'% number

    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)
    print(resp.text)