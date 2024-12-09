import requests

def fetch_data(url):
    response =  requests.get(url)
    
    if response.status_code == 200:
       complete_data = response.json()
       for each_user_data in complete_data:
           print(each_user_data["user"]["login"])       
    else:
        print(f"Failed with status code: {response.status_code}")
        

fetch_data('https://api.github.com/repos/kubernetes/kubernetes/pulls')
