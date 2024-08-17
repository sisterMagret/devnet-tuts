import requests


token='YmYzZmI2M2MtODVkMy00MWQ1LTg0MDQtYmQ2MTJmODJiZDllY2NhNjcyOTMtYWFm_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9'
url= 'https://webexapis.com/v1/rooms'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
# params = {'email':'chile.msendoo@e4email.net'}
body = {
  "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmM5MWRlYTAtNWM3Mi0xMWVmLThiNDItZjNkMzgxNzUyOTQ1",
  "text": "This is a new text",
  "markdown": "**Devnet** A new project plan has been published [on Box](http://box.com/s/lf5vj). The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
  "title": "*Hello word*",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "TextBlock",
            "text": "Adaptive Cards",
            "size": "large"
          }
        ],
        "actions": [
          {
            "type": "Action.OpenUrl",
            "url": "http://adaptivecards.io",
            "title": "Learn More"
          }
        ]
      }
    }
  ]
}
res = requests.post(url, headers=headers, json=body)

print(res.status_code)

{'id': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYTE5NjgxZC02NzdlLTRlZmItYTFlYS1kNjE3NzY4ODA5OTQ', 'emails': ['wistler4u@gmail.com'], 'phoneNumbers': [], 'displayName': 'CHILE SIMON', 'nickName': 'CHILE', 'firstName': 'CHILE', 'lastName': 'SIMON', 'userName': 'wistler4u@gmail.com', 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi82MzZiOTdhMC1iMGFmLTQyOTctYjBlNy00ODBkZDUxN2IzZjk', 'created': '2024-08-17T08:08:36.272Z', 'lastModified': '2024-08-17T08:09:37.412Z', 'timeZone': 'Africa/Lagos', 'lastActivity': '2024-08-17T08:10:28.891Z', 'status': 'inactive', 'type': 'person'}