# import requests

# # /repos/sudhamshapp/repositoryname/pulls

# # "api.github.com/repos/kubernetes/kubernetes/pulls"
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# # print(type(response)) # we get the response object
# complete_detail = response.json() # it automatically converts internally json to python dictionary
# print(complete_detail[0]['user']["login"]) # retrives the single user

import requests

# Send a GET request to the GitHub API
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response into a list of dictionaries
    complete_detail = response.json()

    # Iterate through the list of dictionaries
    # for pull_request in complete_detail:
    #     # Access specific information from each dictionary
    #     user_login = pull_request['user']['login']
    #     # print(f"User Login: {user_login}")
    #     print(user_login)
    # we can also the follow this is approach as well
    for each_user in range(len(complete_detail)):
        print(complete_detail[each_user]['user']['login'])    
else:
    # If the request was not successful, print an error message
    print(f"Error: {response.status_code}")

print(list_of_users)
