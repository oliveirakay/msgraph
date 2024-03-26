import requests

# Your access token
access_token = "YOUR_ACCESS_TOKEN_HERE"

# Endpoint URL
endpoint = "https://graph.microsoft.com/v1.0/users"

# Constructing the authorization header
headers = {
    "Authorization": "Bearer " + access_token
}

# Making the GET request
response = requests.get(endpoint, headers=headers)

# Checking the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()
    print(data)
else:
    # Request failed
    print("Error:", response.status_code, response.text)
