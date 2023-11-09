import sys # read the command line argument that user is passing
type = sys.argv[1]
# print(f"This gonna give us first item of argument - {sys.argv[0]}")
if type == "t2.micro": # == comparison operator
    print("it will charge you $2 a day")
elif type == "t2.medium":
    print("it will charge you $3 a day")
elif type == "t2.xlarge":
    print("it will charge you $4 a day")
else:
    print("please, provide a valid instance type")

# in the cli give it like - python3 test.py t2.medium(test.py is first index and t2.medium is the second index)