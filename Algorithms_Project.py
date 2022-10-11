#WEEKLY ORGANIZER

#SET UP 
import requests
import datetime

data = requests.get("https://sheetdb.io/api/v1/nbalaz9v6jo2q").json()

today = [datetime.datetime.now().strftime("%x")]
today.append(int(input("How many minutes do you have to do homework today?\n")))

tomorrow = [(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%x")]
tomorrow.append(int(input("How many minutes do you have to do homework tomorrow?\n")))

dayafter = [(datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%x")]
dayafter.append(int(input("How many minutes do you have to do homework the day after?\n")))

# ASSIGNMENT STARTS HERE

# FIRST WRITE A COMMENT DESCRIBING YOUR ALGORITHM. HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU 
# ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE 
# ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A 
# FEW ASSIGNMENTS.  
# The goal of the algorithm is to prioritize my worktime to complete the most important assignments first.
# The algorithm will recognize the priority value of the assignments which will dictate order. 
# NEXT WRITE YOUR ALGORITHM OUT IN PSEUDOCODE

#FINALLY - IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT

new_data = sorted(data, key = lambda x: int(x["Priority"]))[::-1]

def schedule(assignment_list):
    day_total = {"today": 0, "tomorrow": 0, "dayafter": 0}
    day_assignments = {"today": [], "tomorrow": [], "dayafter": []}
    assignments_scheduled = []

    for day in day_total.keys():
        for assignment in assignment_list:
            required_time = int(assignment['Required Time'])

            if day_total[day] + required_time <= globals()[day][1] and assignment not in assignments_scheduled:
                day_total[day] += required_time
                day_assignments[day].append(assignment['Assignment'])
                assignments_scheduled.append(assignment)
    return day_assignments


print(schedule(new_data))