#WEEKLY ORGANIZER

#SET UP 
import requests
import datetime

data = requests.get("https://sheetdb.io/api/v1/nbalaz9v6jo2q").json()

today = [datetime.datetime.now().strftime("%x")]
today.append(int(input("How many minutes do you have to do homework today? \n")))

tomorrow = [(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%x")]
tomorrow.append(int(input("How many minutes do you have to do homework tomorrow? /n")))

dayafter = [(datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%x")]
dayafter.append(int(input("How many minutes do you have to do homework the day after? /n")))


# ASSIGNMENT STARTS HERE

# FIRST WRITE A COMMENT DESCRIBING YOUR ALGORITHM
# HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  

#The goal of the algorithm is to find the most eficient way to complete all homework assignments on time. 
# The algorithm will first prioritize the assignments due the earliest. If multiple assignments are due the 
# same day, the priority value of the assignments will then dictate. This will sort the the assignments by 
# importance and the succession of assignments will be assigned based on the first day there is enough time 
# to complete it. The point value of the assignments is relative only to its individual class and will not 
# be taken into consideration. If there is not enough time to complete an assignment any of the three days, 
# the program will suggest to get the work from someone. 

# NEXT WRITE YOUR ALGORITHM OUT IN PSEUDOCODE
#
# The program will suggest the user with a schedule of when to do which homework asignments.
#
# Sort data by "Due Date" and "Priority"
# Create dictionaries for available time each day and the assignements given.


#FINALLY - IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT


def schedule(input_data):
    time_inputs = int(input(day))
    day_totals = {"today" : x , "tomorrow" : x , "dayafter" : x}
    assignments = {"today" : [], "tomorrow" : [] , "dayafter" : []}
    assignment_unassigned = []

    for i in range(len(input_data)):
        
        i = len(assignment_unassigned)
        assignment = input_data[i]

        if day_totals[day] + int(assignment["Required Time"]) <= time_inputs(day):
            assignment_unassigned.append(assignment)
            day_totals += int(assignment["Required Time"])
            input_data.remove(assignment)