import requests
import json

# API CONFIGURATION
api_key = "TU_API_KEY"
access_token = "TU_ACCESS_TOKEN"
list_id = "ID_DE_TU_LISTA"

# NEW CONTACT 
email = "ejemplo@dominio.com"
first_name = "example"
last_name = "lastname"

# Build the data in API  Constant Contact Formar
contact_data = {
    "email_addresses": [
        {
            "email_address": email
        }
    ],
    "first_name": first_name,
    "last_name": last_name
}

# REQUEST HTTP POST to API  Constant Contact for creating new contact
url = "https://api.cc.email/v3/contacts"
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
response = requests.post(url, headers=headers, json=contact_data)

# check if request was successfull and proceed to add.
if response.status_code == 201:
    contact_id = response.json()["id"]
    url = f"https://api.cc.email/v3/lists/{list_id}/contacts/{contact_id}"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    response = requests.put(url, headers=headers)
    if response.status_code == 204:
        print(f"The contact  {email} has been successfully added.")
    else:
        print("An error ocurred.")
else:
    print("The new contact was not able to be added.")
