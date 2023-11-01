import sys
type = sys.argv[1]
if type == "t2.micro": # == comparison operator
    print("it will charge you $2 a day")
elif type == "t2.medium":
    print("it will charge you $3 a day")
elif type == "t2.xlarge":
    print("it will charge you $4 a day")
else:
    print("please, provide a valid instance type")    