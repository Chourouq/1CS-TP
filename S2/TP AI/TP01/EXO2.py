from aima.logic import *
from aima.utils import *
KB = FolKB()
KB.tell(expr(''))

KB.tell(expr('Couleur(Bleu)'))
KB.tell(expr('Couleur(Vert)'))
KB.tell(expr('Couleur(Blanc)'))
KB.tell(expr('Couleur(Noir)'))

KB.tell(expr('Dcl(Bleu,Vert)'))
KB.tell(expr('Dcl(Bleu,Blanc)'))
KB.tell(expr('Dcl(Bleu,Noir)'))
KB.tell(expr('Dcl(Vert,Blanc)'))
KB.tell(expr('Dcl(Vert,Noir)'))
KB.tell(expr('Dcl(Blanc,Noir)'))

# Define regions
KB.tell(expr('Region(1)'))
KB.tell(expr('Region(2)'))
KB.tell(expr('Region(3)'))
KB.tell(expr('Region(4)'))
KB.tell(expr('Region(5)'))
KB.tell(expr('Region(6)'))

KB.tell(expr('Adjacent(1,2)'))
KB.tell(expr('Adjacent(1,5)'))
KB.tell(expr('Adjacent(3,1)'))
KB.tell(expr('Adjacent(3,2)'))
KB.tell(expr('Adjacent(3,4)'))
KB.tell(expr('Adjacent(3,6)'))
KB.tell(expr('Adjacent(6,1)'))
KB.tell(expr('Adjacent(6,5)'))
KB.tell(expr('Adjacent(6,2)'))
KB.tell(expr('Adjacent(2,4)'))
KB.tell(expr('Adjacent(2,5)'))
KB.tell(expr('Adjacent(2,1)'))

KB.tell(expr('Dcl(x,y)    ==>    Dcl(y,x)'))
KB.tell(expr('Adjacent(x,y)   ==>    Adjacent(y,x)'))

#KB.tell(expr('Region(x) & Region(y) & Adjacent(x,y) & Couleur(c1) & Couleur(c2) & Dcl(c1,c2)  ==> (Color(x,c1) & Color(y,c2))'))
KB.tell(expr('(Region(x) & Region(y) & Adjacent(x,y) & Exists(c1, c2, (Couleur(c1) & Couleur(c2) & Difclr(c1,c2))))    ==> (Exists(c1, c2, (Color(x,c1) & Color(y,c2))))'))
R = fol_fc_ask(expr(KB,'(Color(1,Blue)& Color(2,Vert))'))

print(R)

