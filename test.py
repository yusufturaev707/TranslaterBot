import requests, oxfordLookup as ox

word = "cat"

url = f"{ox.base_url}/entries/" + ox.language + "/" + word
r = requests.get(url, headers={"app_id": ox.app_id, "app_key": ox.app_key})
response = r.json()
definitions = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
# print(definitions[0]['definitions'][0])

for i in definitions:
    print(i['definitions'][0])