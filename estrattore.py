import requests
import json

url = "https://www.romagnacque.it/datidiretta/index2.php"
response = requests.get(url)

if response.status_code == 200:
    storicoridracoli = response.json()
    with open("storicoridracoli.json", "a") as f:
        json.dump(storicoridracoli, f)
        f.write('\n')  # add a newline separator
        print("New data appended to storicoridracoli.json")
else:
    print("Error: Failed to retrieve data from URL")
