import requests

api_key = ''
summoner_name = 'Doublelift'

try:
    response = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}")
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')
    
json_response = response.json()

print(json_response)
summoner_name = json_response['name']
print(summoner_name)
