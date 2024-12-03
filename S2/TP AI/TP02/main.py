from aima.logic import *
from aima.utils import *

KB = FolKB()
#Facts
symptoms = ["Fever", "Cough", "Headache", "SoreThroat",
            "BodyAche", "RunnyNose", "Fatigue",
            "LightSensitivity", "FacialPain", "Congestion",
            "Rash", "AbdominalPain", "Vomiting", "Diarrhea"]
diseases = ["Flu","Migraine", "Infection",
            "AllergicRhinitis", "Cold"]
#Rules
KB.tell(expr('Fever(x)&Cough(x) ==>Flu(x)'))
KB.tell(expr('Fever(x)&Fatigue(x) ==>Flu(x)'))
KB.tell(expr('SoreThroat(x)&RunnyNose(x) ==>Cold(x)'))

Agenda = []
#add symptoms to the agenda
patient = expr('Ahmed')
Agenda.append(expr('Fever(Ahmed)'))
Agenda.append(expr('Cough(Ahmed)'))
Agenda.append(expr('Fatigue(Ahmed)'))
Agenda.append(expr('BodyAche(Ahmed)'))
seen = set()
while Agenda:
    s = Agenda.pop()
    if s in seen:
        continue
    seen.add(s)




