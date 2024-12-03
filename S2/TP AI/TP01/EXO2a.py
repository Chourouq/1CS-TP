from aima.logic import *
from aima.utils import *

kb = FolKB()

kb.tell(expr('ClrD(Blue, Green)'))
kb.tell(expr('ClrD(Blue, White)'))
kb.tell(expr('ClrD(Blue, Black)'))
kb.tell(expr('ClrD(White, Green)'))
kb.tell(expr('ClrD(White, Black)'))
kb.tell(expr('ClrD(Black, Green)'))
kb.tell(expr('ClrD(x,y) ==>ClrD(y,x)'))
kb.tell(expr(
    'ClrD(c1,c2) & ClrD(c1,c3) & ClrD(c1,c5)& ClrD(c1,c6) & ClrD(c2,c3) & ClrD(c2,c4) & ClrD(c2, c5) & ClrD(c2, c6) & ClrD(c3, c4) & ClrD(c3, c6) & ClrD(c5, c6) ==> Location(c1, c2, c3, c4, c5, c6)'))

L = fol_fc_ask(kb,expr('Location(c1,c2,c3,c4,c5,c6)'))

print(list(L))
