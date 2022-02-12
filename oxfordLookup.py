import requests

app_id = "fd8d5ef8"
app_key = "79beeddc4a3d7ced3ef826aed6fd92aa"
base_url = "https://od-api.oxforddictionaries.com/api/v2"
language = "en-gb"


def getDefenitios(word):
    url = f"{base_url}/entries/" + language + "/" + word.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    response = r.json()
    if "error" in response.keys():
        return False

    output = {}
    senses = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    audioFile = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile')

    if audioFile:
        output['audio'] = audioFile

    return output
