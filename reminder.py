import requests
from requests.structures import CaseInsensitiveDict




url = "https://graph.facebook.com/v13.0/103347919147898/messages"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer EAAHDZC1VSkZB0BALvKqzR7H7Vibgda5rY1uixAbuTjoAJrlZCOMCq55u7Kw2ZATBRgRVdWSXmlA1wMvsjnxxmS6wE5YgFxUtTzMDDITGSKEb11ZCWazyIviQGhs3eRyYCIZCCJxsUWJD56iDGzbmoda2gNWRK1OX8hoZBudaonJc53NXv5kMuMI6iJ9W1li0Aw9JU822W9PcgZDZD"
headers["Content-Type"] = "application/json"

for number, name in numbers.items():
    data = '{ "messaging_product": "whatsapp", "to": "%s", "type": "template", "template": { "name": "message_reminder", "language": { "code": "es_ES" } } }'% number

    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)
    print(resp.text)