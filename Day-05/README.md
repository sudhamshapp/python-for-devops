command line arguments
aws s3 ls - for example, aws cli is the python program, and the s3 ls are the command line arguments, command line arguments helps passing the values to the program
program can take command line arguments as input

sys module - helps read the command line arguments inside your program
By default arguments read as strings, we need to convert them to the integers
sys reads the command line arguments

Environmental Variables
for passwords and api keys, tokens, certificates(handles the senitive information)
we won't do hardcoding, we won't pass in the senstive information using command line arguments
export password="sudhamsh"
to read the environment variables we use the os module

env vars Vs command line arguments

