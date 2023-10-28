# export password="sudhamsh"
# export apitoken="djnsdkanckdckjdvkv"  
# we need to set the above stuff in the cli
# we can execute this python stuff securely in ci/cd, cronjob, automation securely 
import os
print(os.getenv("password"))
print(os.getenv("apitoken"))