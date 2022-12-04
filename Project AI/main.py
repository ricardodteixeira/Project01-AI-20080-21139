from csp_init import *
import prettytable
from csp import *
from mrv import *
from forward_checking import *
import random as rnd #----------------------------------------- doesn't work

#TODO: INCLUIR TYPE (ONLINE, PRESENCIAL), incluindo o init no data.py
#TODO: MUDAR CÓDIGO, SUAVIZAR
#TODO: ALTERAR CONSTRAINTS, ADD AS QUE FALTAM
#•	Each class must have the duration of 2 hours
# •	Each class must only take place on weekdays
# •	All classes must have 10 lessons per week, of which 1 ou 2 classes must be online
# •	A class should not have more than 3 lessons per day
# •	Online classes can’t be right after a face-to-face lesson
# •	Only up to 2 lessons can take place in the morning and up to 2 lessons in the afternoon
# •	Every class has 2 to 4 lessons in a specific classroom
# •	Time slots cannot be overlapped
# •	Each teacher cannot in two classes/rooms at the same time
#	Rooms can only have one class at a time



result_default = backtracking(init_assignment_default(my_csp), my_csp, default_heuristic)
print("Counter for default backtracking: " + str(get_counter_default()))

result_mrv = mrv_backtracking(init_assignment_mrv(my_csp),my_csp)
print("Counter for backtracking with MRV: " + str(get_counter_mrv()))


# result_forward_check = forward_checking(init_assignment_forw(my_csp), my_csp)
# print("Counter for backtracking with Forward Checking: " + str(get_counter_forw()))


result = result_mrv


monday, tuesday, wednesday, thursday, friday = [], [], [], [], []
days = [monday, tuesday, wednesday, thursday, friday]
for i in result.keys():
    if result[i] < 4:
        monday.append((i,result[i]))
    elif result[i] < 8 and result[i]>=4:
        tuesday.append((i,result[i]-4))
    elif result[i] < 12 and result[i]>=8:
        wednesday.append((i,result[i] - 8))
    elif result[i] < 16 and result[i]>=12:
        thursday.append((i, result[i] - 12))
    elif result[i] >= 16:
        friday.append((i, result[i] - 16))


def print_day(day,l):
	r = ""
	for d,n in day:
		if (l == n):
			r += str(d) + "\n" 
	return r


table = prettytable.PrettyTable(['Lesson Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
k = 0
for i in range(len(MEETING_TIMES)):
    table.add_row([MEETING_TIMES[i], print_day(monday,k), print_day(tuesday,k), print_day(wednesday,k), print_day(thursday,k), print_day(friday,k)])
    k+=1
print(table)