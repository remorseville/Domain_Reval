import requests

domain_list = [3336093, 2984503] # This is a array of DigiCert domain_id's 

for i in domain_list:

    url = f"https://www.digicert.com/services/v2/domain/{i}/validation"

    payload="{\n\"validations\":[\n{\n\"type\":\"ov\"\n},\n{\n\"type\":\"ev\"\n}\n],\n\"dcv_method\":\"email\"\n}"
    headers = {
      'X-DC-DEVKEY': 'BWST6J7CZ5Z---BRING-YOUR-OWN-KEY---SBPI42ZX4GAT34UNRLHO',  # Need to update API key with one from your own account
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
