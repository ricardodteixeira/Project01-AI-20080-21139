from csp_init import *
from mrv import * 
csp = my_csp

counter = 0
var_domains = {}
degree_values = {}

#init empty assignment
def init_assignment_forw(csp):
  global var_domains
  global counter
  counter = 0
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
    var_domains[var] = csp[DOMAINS].copy()
  return assignment


def getRoom(csp, assignment,var, value):
  rooms = data._rooms
  rooms.sort(key=lambda c: c[1])
  
  for r in rooms:
    if (r[1] >= var._number_of_students):
      free = True
      for k in csp[VARIABLES]:
        if (assignment[k] is not None):
          if (k._room == r and assignment[k] == value):
            free = False
      if free:
       return r


def forward_checking(assignment,csp):
  global var_domains
  global counter
  while True:
    if is_complete(assignment):
      return assignment
    var = select_unassigned_variable(csp[VARIABLES],assignment)
    for value in csp[DOMAINS]:

      if is_in_domain(var, value):
        assignment[var] = value
        add_domains(assignment, csp, var)
        var._room = getRoom(csp,assignment, var, value)
        counter+=1
        if is_consistent(assignment, csp[CONSTRAINTS]):    
          break
        else: 
          assignment[var] = None
          var._room = None
          undo(assignment,csp)
  return FAILURE


def is_in_domain(var,value):
  global var_domains
  for d in var_domains[var]:
    if (d == value):
      return True
  return False


def add_domains(assignment, csp, value):
  global var_domains
  j = value
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      if (not i==j):
        if (i._teacher == j._teacher):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._type_of_class == j._type_of_class):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._speciality == j._speciality and (i._type_of_class == "Theoretical") or (j._type_of_class == "Theoretical")):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._speciality == j._speciality and (i._type_of_class == "Pratice") or (j._type_of_class == "Pratice")):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None


def get_counter_forw():
  global counter
  return counter