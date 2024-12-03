from aima.logic import *
from aima.utils import *
kb = FolKB()
kb.tell(expr('Male(Jean)'))
kb.tell(expr('Male(Fabien)'))
kb.tell(expr('Male(Jérome)'))
kb.tell(expr('Male(Franck)'))
kb.tell(expr('Male(Bruno)'))

kb.tell(expr('Female(Evelyne)'))
kb.tell(expr('Female(Louise)'))
kb.tell(expr('Female(Eve)'))
kb.tell(expr('Female(Sophie)'))
kb.tell(expr('Female(Marie)'))

kb.tell(expr('Parent(Jean,Fabien)'))
kb.tell(expr('Parent(Fabien,Louise)'))
kb.tell(expr('Parent(Louise,Jérome)'))
kb.tell(expr('Parent(Louise,Sophie)'))
kb.tell(expr('Parent(Louise,Marie)'))
kb.tell(expr('Parent(Jérome,Franck)'))
kb.tell(expr('Parent(Sophie,Bruno)'))
kb.tell(expr('Parent(Sophie,Marie)'))
kb.tell(expr('Parent(Sophie,Eve)'))

kb.tell(expr('Parent(x,y)&Female(x)==>Mom(x,y)'))
kb.tell(expr('Parent(x,y)&Male(x)==>Dad(x,y)'))
kb.tell(expr('Parent(z,x) & Parent(z,y)==>FrereSoeur(x,y)'))
kb.tell(expr('FrereSoeur(x,y) & Male(x)==>Frere(x,y)'))
kb.tell(expr('FrereSoeur(x,y) & Female(x)==>Soeur(x,y)'))
kb.tell(expr('FrereSoeur(x,y) & Female(x)==>Soeur(x,y)'))
kb.tell(expr('Dad(z,y) & Frere(x,z)==>Oncle(x,y)'))
kb.tell(expr('Parent(z,y) & Soeur(x,z)==>Tante(x,y)'))
kb.tell(expr('Parent(z,y) & Soeur(x,z)==>Tante(x,y)'))
kb.tell(expr('Oncle(z,x) &Dad(z,y)==>Cousin(x,y)'))
kb.tell(expr('Parent(z,y) ==>Ancetre(z,y)'))
kb.tell(expr('Parent(x,z) & Ancetre(z,y)==>Ancetre(x,y)'))
R = kb.ask(expr('Ancetre(Jean,Franck)'))

print(R)
