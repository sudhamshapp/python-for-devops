# this whole sstuff pulled from jira API documentation - https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sudhamshchetla.atlassian.net/rest/api/3/project"

#Read this API token as the "environment variable" and command line arguments, don't keep this as plain text
API_TOKEN = "ATATT3xFfGF0deYISBvcjQOnx3CB7jPbcPld_JYkX1aeGMoUiIvgY-jEyB1wBsNuuEL1JSopEiRmznntE8fAL4V3puF79FNbtFjzEaSGZiwj1VMcM7lco2S2UJHBoA9B-I5pygVavnCR0jM8bpZvLFcYawLRKWIcGRSlXuWghZVzqvX09FZBzBA=88F93695"

auth = HTTPBasicAuth("sudhamsh1996@ggmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# json loads parses json data to python dictionary
# output = json.loads(response.text)
# name = output[0]["name"]
# print(name)