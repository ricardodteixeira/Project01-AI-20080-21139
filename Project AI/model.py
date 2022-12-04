#Object which contains all the information about one class
class Lession:
    def __init__(self, speciality, subject, room, time, day, type_of_class, _class, type):
        self._speciality = speciality
        self._subject = subject
        self._teacher = self._subject._teacher
        self._number_of_students = self._subject._number_of_students
        self._room = room
        self._time = time
        self._day = day
        self._type_of_class = type_of_class
        self._class = _class
        self._type = type


    def __str__(self):
        return str(self._subject._name) + "\n" + str(self._teacher) + ", " + str(self._type_of_class) + ", " + str(self._type) + "\nRoom: " + str(self._room[0]) + ", " + str(self._class) + "\n"

class Teacher:
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject
    def __str__(self): return self._name


class Subject:
    def __init__(self, name, number_of_students, teacher, _class):
        self._name = name
        self._number_of_students = number_of_students
        self._teacher = teacher
        self._class = _class


class Room:
	def __init__(self, name, capacity):
		self._name = name
		self._capacity = capacity


class Speciality:
    def __init__(self, name, subjects):
        self._name = name
        self._subjects = subjects

