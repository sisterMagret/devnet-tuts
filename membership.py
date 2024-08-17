import requests


token='YmYzZmI2M2MtODVkMy00MWQ1LTg0MDQtYmQ2MTJmODJiZDllY2NhNjcyOTMtYWFm_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9'
url= 'https://webexapis.com/v1/memberships?personEmail=wistler4u@gmail.com&max=100'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
params = {'personEmails':['wistler4u@gmail.com']}
res = requests.get(url, headers=headers, )

print(res.json())


