from data import *
data = Data()
classes = data._classes
meeting_times = data.get_domains()


DOMAINS = "DOMAINS"
VARIABLES = "VARIABLES"
CONSTRAINTS = "CONSTRAINTS"
FAILURE = "FAILURE"


def is_complete(assignment):
  return None not in (assignment.values())


def select_unassigned_variable(variables, assignment):
  for var in variables:
    if assignment[var] is None:
      return var  


def is_consistent(assignment, constraints):
  for constraint_violated in constraints:
    if constraint_violated(assignment):
      return False
  return True


def equal(a, b): return a is not None and b is not None and a == b
def is_between(hour,a,b): return a is not None and b is not None and a< hour and hour > b

def get_var(assignment):
  arr = []
  for i in assignment.keys():
    newClass = i
    if assignment[i] is not None:
      arr.append(newClass)
  return arr


def same_teacher(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._teacher, j._teacher) and i!=j and assignment[i]==assignment[j]:
        return True
  return False


def same_class(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._class, j._class) and equal(i._speciality, j._speciality) and equal(i._teacher, j._teacher) and i!=j and assignment[i]==assignment[j]:
        return True
  return False


def same_spec(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._speciality._name, j._speciality._name) and equal(i._subject._name, j._subject._name) and i != j and (((assignment[i] >= 0 and assignment[i] <=3) and (assignment[j] >= 0 and assignment[j] <= 3)) or ((assignment[i] >= 4 and assignment[i] <= 7) and (assignment[j] >= 4 and assignment[j] <= 7)) or ((assignment[i] >= 8 and assignment[i] <=11) and (assignment[j] >= 8 and assignment[j] <= 11)) or ((assignment[i] >= 12 and assignment[i] <=15) and (assignment[j] >= 12 and assignment[j] <= 15)) or (assignment[i] >= 16 and assignment[j] >= 16)):
        return True
  return False


def class_conflit(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._class, j._class) and i != j and assignment[i] == assignment[j] :
        return True
  return False


def three_lessions_per_day_by_class(assignment):
  arr = get_var(assignment)
  monday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  tuesday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  wednesday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  thursday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  friday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  if len(arr) == 1:
    return False
  for i in arr:
    if (assignment[i] >= 0 and assignment[i] <= 3):
        monday[i._subject._class] += 1
    if (assignment[i] >= 4 and assignment[i] <= 7):
        tuesday[i._subject._class] += 1
    if (assignment[i] >= 8 and assignment[i] <= 11):
        wednesday[i._subject._class] += 1
    if (assignment[i] >= 12 and assignment[i] <= 15):
        thursday[i._subject._class] += 1
    if (assignment[i] >= 16):
        friday[i._subject._class] += 1

  for i in monday.values():
    if i > 3:
      return True
  for i in tuesday.values():
    if i > 3:
      return True
  for i in wednesday.values():
    if i > 3:
      return True
  for i in thursday.values():
    if i > 3:
      return True
  for i in friday.values():
    if i > 3:
      return True


def mandatory_online_lessions(assignment):
  arr = get_var(assignment)


  if (len(assignment) == 1):
    return False
  counter_days_online = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  monday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  tuesday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  wednesday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  thursday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
  friday = {"LESI1": 0, "LESI2": 0, "LESI3": 0}

  for i in arr:
    if ((assignment[i] >= 0 and assignment[i] <= 3) and (i._type == "Online") and (i._type_of_class == "Theoretical")):
      monday[i._subject._class] += 1
    if ((assignment[i] >= 4 and assignment[i] <= 7) and (i._type == "Online") and (i._type_of_class == "Theoretical")):
      tuesday[i._subject._class] += 1
    if ((assignment[i] >= 8 and assignment[i] <= 11) and (i._type == "Online") and (i._type_of_class == "Theoretical")):
      wednesday[i._subject._class] += 1
    if ((assignment[i] >= 12 and assignment[i] <= 15) and (i._type == "Online") and (i._type_of_class == "Theoretical")):
      thursday[i._subject._class] += 1
    if ((assignment[i] >= 16) and (i._type == "Online") and (i._type_of_class == "Theoretical")):
      friday[i._subject._class] += 1

  for i in monday.keys():
    if not monday[i] > 3 and not monday[i] < 3:
      counter_days_online[i] += 1
  for i in tuesday.keys():
    if not tuesday[i] > 3 and not tuesday[i] < 3:
      counter_days_online[i] += 1
  for i in wednesday.keys():
    if not wednesday[i] > 3 and not wednesday[i] < 3:
      counter_days_online[i] += 1
  for i in thursday.keys():
    if not thursday[i] > 3 and not thursday[i] < 3:
      counter_days_online[i] += 1
  for i in friday.keys():
    if not friday[i] > 3 and not friday[i] < 3:
      counter_days_online[i] += 1

  for i in counter_days_online.keys():
    if not counter_days_online[i] == 1:
      return True



my_csp = {VARIABLES: classes,
          DOMAINS: meeting_times,
          CONSTRAINTS: [same_teacher, same_spec, same_class, class_conflit, three_lessions_per_day_by_class]
          }