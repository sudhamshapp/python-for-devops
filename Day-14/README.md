git pull upstream main


know about how to create a issue on github
problem statement:
when they(qe/dev) notice a bug in the application(after testing) > they create a issue in the git repo

whoever created a issue that shouldn't considered as issue, there may have some configuration mistakes or they din't understand the application workflow

if the issue isn't valid, simply close the issue, if the issue is valid they need to work on particular issue(to work on the issue, they have to track the amount of work that is required)> then they need to go to jira dashboard and they need to create the ticket on jira dashboard

when someone comments on jira, the ticket should be automatically created on jira
there needs to be a bridge for this, when someone comments on github issue saying that jira ticket is needed only then jira ticket has to be created
to automate the above job, we can use python, but not shell(its not deal with APIs)
whenever someone comments: /jira, hey github I created a python application and I hosted it on ec2 instance(why don't you send me a webhook), send me all the particular information of that issue(send me the description of issue, who was created the issue, when did they create and what did they create), the entire UI thing of github actions can be converted to json format. github sends the information to the python application then will make a API call to jira

github actions>python-application>Jira
provides the json to python-application> then it send the json data to jira
we need to convert the python script to the flask application

PART - 1
Jira setup
Jira API calls
python script
execution of python script
issue/ticket in jira


API token of JIRA ATATT3xFfGF0deYISBvcjQOnx3CB7jPbcPld_JYkX1aeGMoUiIvgY-jEyB1wBsNuuEL1JSopEiRmznntE8fAL4V3puF79FNbtFjzEaSGZiwj1VMcM7lco2S2UJHBoA9B-I5pygVavnCR0jM8bpZvLFcYawLRKWIcGRSlXuWghZVzqvX09FZBzBA=88F93695

Now we to understand how to talk with jira APIs, like which modules in python I need to use and on which url I need to access Jira, what is the context route