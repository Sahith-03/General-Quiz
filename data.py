import requests
import html

parameters = {
    "type": "boolean",
    "amount": 10
}

data = requests.get(url="https://opentdb.com/api.php?", params=parameters)
data.raise_for_status()
question_data = data.json()["results"]
