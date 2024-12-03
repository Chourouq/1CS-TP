from aima.logic import * ;
from  aima.utils import *;

kb = FolKB()


kb.tell(expr('Nationality(Anglaise)'))
kb.tell(expr('Nationality(Espagnole)'))
kb.tell(expr('Nationality(Francaise)'))
kb.tell(expr('Sport(Football)'))
kb.tell(expr('Sport(Natation)'))
kb.tell(expr('Sport(Tennis)'))
kb.tell(expr('Color(Blanc)'))
kb.tell(expr('Color(Bleu)'))
kb.tell(expr('Color(Vert)'))
kb.tell(expr('Rue(Debut)'))
kb.tell(expr('Rue(Milieu)'))
kb.tell(expr('Rue(Fin)'))
kb.tell(expr('Avant(Debut,Milieu)'))
kb.tell(expr('Avant(Milieu,Fin)'))
kb.tell(expr('Avant(Debut,Fin)'))
kb.tell(expr('Nationality(x) & Sport(y) & Color(z) & Rue(t) ==> Maison(x,y,z,t)'))

KB.tell(expr('Color(Vert) ==> Maison(x,Natation,Vert,t)'))
KB.tell(expr('Maison(x,Natation,Vert,t) & Avant(Debut,Fin)'))
KB.tell(expr('Nationality(Anglaise) ==> Maison(Anglaise,y,Blanc,t)'))
KB.tell(expr('Sport(Tennis) ==> Maison(x,Tennis,z,Debut)'))
KB.tell(expr('Nationality(Espagnole) ==> Maison(Espagnole,y,z,Fin) '))
KB.tell(expr('Rue(Fin) ==> Maison(x, Natation, z,Fin ) '))
KB.tell(expr('Nationality(Anglaise) ==> Maison(Anglaise,y,z,Debut)'))
KB.tell(expr('Nationality(Francaise) ==> Maison( Francaise,y,z,Milieu)'))
KB.tell(expr('Color(Bleu) ==> Avant(Milieu,Fin) & Maison(Francaise,y,z,Milieu) & Maison(x,y,Blue,Fin)'))

L = fol_fc_ask(kb,expr('Maison(x,y,z,t)'))
print(list(L))




