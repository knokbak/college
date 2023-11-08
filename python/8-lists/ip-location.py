import requests

ip_addr = input("Enter IP address: ").strip()
try:
    response = requests.get(f'https://geolocation-db.com/json/{ip_addr}').json()
except Exception as e:
    print(f'Error: {e}')
    print('Check the provided IP address is valid!')
    exit(1)

print(f'''
City: {response['city']}
State: {response['state']}
Country: {response['country_name']}
Postal code: {response['postal']}
Longitude: {response['longitude']}
Latitude: {response['latitude']}
''')
