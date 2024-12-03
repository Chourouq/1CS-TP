from aima.logic import * ;
from  aima.utils import *;

kb = FolKB()
kb.tell(expr('Nat(Anglais)'))
kb.tell(expr('Nat(Espagnole)'))
kb.tell(expr('Nat(Français)'))

kb.tell(expr('Sport(Football)'))
kb.tell(expr('Sport(Natation)'))
kb.tell(expr('Sport(Tennis)'))

kb.tell(expr('Color(Blanc)'))
kb.tell(expr('Color(Blue)'))
kb.tell(expr('Color(Vert)'))

kb.tell(expr('Empl(Debut)'))
kb.tell(expr('Empl(Milieu)'))
kb.tell(expr('Empl(Bout)'))

kb.tell(expr('Empl(Debut) & Empl(Milieu) ==> Avant(Debut,Milieu) '))
kb.tell(expr('Empl(Milieu) & Empl(Bout) ==> Avant(Milieu,Bout) '))
kb.tell(expr('Empl(Debut) & Empl(Milieu) ==> Devant(Milieu,Debut) '))
kb.tell(expr('Empl(Milieu) & Empl(Bout) ==> Devant(Bout,Milieu) '))


kb.tell(expr('Nat(x) & Sport(y) & Color(z) & Empl(t) ==> Maison(x,y,z,t)'))
kb.tell(expr('Color(m,Vert) ==> Sport(m,Natation)'))
kb.tell(expr('Color(m,Vert) & Avant(x,y) ==> Nat(m,Espagnole)'))
kb.tell(expr('Nat(m,Anglais) ==> Color(m,Blanc)'))
kb.tell(expr('Color(m,Vert) & Avant(x,y) ==> Sport(m,Football)'))
kb.tell(expr('Sport(m,Tennis) ==> Empl(m,Debut)'))
kb.tell(expr('Nat(m,Espagnole) ==> Empl(m,Bout)'))
kb.tell(expr('Empl(m,Bout) ==> Sport(m,Football)'))
kb.tell(expr('Nat(m,Anglais) ==> Empl(m,Debut)'))
kb.tell(expr('Nat(m,Français) ==> Empl(m,Milieu)'))
kb.tell(expr('Color(m,Blue) & Devant(x,y) ==> Nat(m,Français)'))

L = fol_fc_ask(kb,expr('Maison(x,y,z,t)'))
print(list(L))

