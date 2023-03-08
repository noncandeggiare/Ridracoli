import requests
import json

url = "https://www.romagnacque.it/datidiretta/index2.php"
response = requests.get(url)

if response.status_code == 200:
    storicoridracoli = response.json()
    with open("storicoridracoli.json", "a") as f:
        json.dump(storicoridracoli, f)
        f.write('\n')  # add a newline separator
        print("Dati aggiunti a storicoridracoli.json")
else:
    print("Errore: URL non raggiungibile")