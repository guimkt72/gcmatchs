import pandas as pd
import requests 
import json 



url = 'https://gamersclub.com.br/lobby/match/22697838/1'
request = requests.get(url)
request_response = request.text
data = json.loads(request_response)


print(data)
