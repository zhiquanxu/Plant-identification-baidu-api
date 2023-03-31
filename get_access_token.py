
import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=x8oohCg7uMZsqcnCl1V1QocZ&client_secret=iP9Yt2GGUaisaAYh3HWpALVR1fe7jApT&grant_type=client_credentials"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()
