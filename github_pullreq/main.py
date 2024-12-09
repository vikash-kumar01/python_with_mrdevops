import requests
 
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(type(response)) --> <class 'requests.models.Response'>
complete_detail = response.json()
for each_user in complete_detail:
    print(each_user["user"]["login"])