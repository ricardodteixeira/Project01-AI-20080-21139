import random as rnd
from specs import *
from model import *

class Data:
    def __init__(self):
        self._days = DAYS
        self._meetingTimes = MEETING_TIMES
        self._subjects = self.init_subjects(SUBJECTS)
        self._specs = self.init_specs(SPECIALITIES)
        self._rooms = ROOMS
        self._classes = self.init_classes()
        self._type = TYPE
      
        

    def init_subjects(self, subjects):
        subj = []
        for s in subjects:
            name = s["name"]
            num = s["number_of_students"]
            gr = s["_class"]
            tea = s["teacher"]
            subj.append(Subject(name, num, tea, gr))
        return subj

    def get_domains(self):
        domains = []
        for i in range(30):
            domains.append(i)
        return domains


    def init_specs(self, specialities):
        spec = []
        for s in specialities:
            name = s["name"]
            sub = []
            for i in s["subjects"]:
                for j in self._subjects:
                    if i == j._name:
                        sub.append(j)
            spec.append(Speciality(name, sub))
        return spec


    def init_classes(self):
        classes = []
        counter_online_lessions = {"LESI1": 0, "LESI2": 0, "LESI3": 0}
        for sp in self._specs:
            for sub in sp._subjects:
                if counter_online_lessions[sub._class] < 3:
                    lect = Lession(sp, sub, None, None, None, "Theoretical", sub._class, "Online")
                    counter_online_lessions[sub._class] += 1
                else:
                    lect = Lession(sp, sub, None, None, None, "Theoretical", sub._class, "Presential")
                classes.append(lect)
                lect = Lession(sp, sub, None, None, None, "Pratical", sub._class, "Presential")
                classes.append(lect)

        return classes