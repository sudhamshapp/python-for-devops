text = "Python is awesome"
words = text.split()
print("Words:", words)


arn = "arn:aws:iam::623917384971:user/devops-sudhamsh/arbitary-sudhamsh-test-string"
# username = arn.split('/')
username = arn.split('-')
#here split is the built-in function that is used to split a string into a list of substrings.
print(username)
# This Python code takes an AWS IAM (Identity and Access Management) user's ARN (Amazon Resource Name) as input and extracts the username from the ARN.

# Here's a breakdown of the code:

# arn is a string that represents an AWS IAM user's ARN. ARN stands for Amazon Resource Name and is a way to uniquely identify AWS resources.

# arn.split('/') is used to split the arn string into a list of substrings using the forward slash ("/") as the delimiter. The forward slash is commonly used to separate components of an ARN.

# username is assigned the value of arn.split('/'). After splitting the arn string, the username variable should contain a list of substrings, and the username should be one of these substrings.

# print(username[1]) prints the second element (index 1) of the username list. In an ARN, the username typically appears as the second element after splitting by slashes. So, this line of code prints the IAM username extracted from the ARN.

# So, if the arn variable contains the ARN you provided ("arn:aws:iam::623917384971:user/devops-sudhamsh"), this code would print "user/devops-sudhamsh," which is the IAM username.