import requests
import sys
import json

def make_request(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        
        if 100 <= status_code < 400:
            print(f"Success: {status_code}")
            print(f"Response body: {response.text}")
            return True
        else:
            raise Exception(f"Error: {status_code}\nResponse body: {response.text}")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")

def main():
    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/201",
        "https://httpstat.us/301",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]
    
    for url in urls:
        try:
            print(f"\nChecking {url}")
            make_request(url)
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

if __name__ == "__main__":
    main()