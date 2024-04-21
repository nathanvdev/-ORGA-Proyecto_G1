
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMARILLO COMA CYAN END_PRINT ID MAGENTA NEGRO NEW_PRINT NUMBER PARA PARC PUNTOYCOMA SET_PRINT_ESTRELLA SET_PRINT_O SET_PRINT_TRIANGULO SET_PRINT_X SET_PRINT_Ystart    : NEW_PRINT ID PUNTOYCOMA instrucciones END_PRINT PUNTOYCOMAinstrucciones : instrucciones instruccion \n                     | instruccioninstruccion : SET_PRINT_X PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA\n                   | SET_PRINT_Y PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA\n                   | SET_PRINT_O PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA\n                   | SET_PRINT_TRIANGULO PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA\n                   | SET_PRINT_ESTRELLA PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMAcolor    : CYAN\n                | MAGENTA\n                | AMARILLO\n                | NEGRO '
    
_lr_action_items = {'NEW_PRINT':([0,],[2,]),'$end':([1,19,],[0,-1,]),'ID':([2,],[3,]),'PUNTOYCOMA':([3,12,49,50,51,52,53,],[4,19,54,55,56,57,58,]),'SET_PRINT_X':([4,5,6,13,54,55,56,57,58,],[7,7,-3,-2,-4,-5,-6,-7,-8,]),'SET_PRINT_Y':([4,5,6,13,54,55,56,57,58,],[8,8,-3,-2,-4,-5,-6,-7,-8,]),'SET_PRINT_O':([4,5,6,13,54,55,56,57,58,],[9,9,-3,-2,-4,-5,-6,-7,-8,]),'SET_PRINT_TRIANGULO':([4,5,6,13,54,55,56,57,58,],[10,10,-3,-2,-4,-5,-6,-7,-8,]),'SET_PRINT_ESTRELLA':([4,5,6,13,54,55,56,57,58,],[11,11,-3,-2,-4,-5,-6,-7,-8,]),'END_PRINT':([5,6,13,54,55,56,57,58,],[12,-3,-2,-4,-5,-6,-7,-8,]),'PARA':([7,8,9,10,11,],[14,15,16,17,18,]),'NUMBER':([14,15,16,17,18,25,26,27,28,29,],[20,21,22,23,24,30,31,32,33,34,]),'COMA':([20,21,22,23,24,30,31,32,33,34,],[25,26,27,28,29,35,36,37,38,39,]),'CYAN':([35,36,37,38,39,],[41,41,41,41,41,]),'MAGENTA':([35,36,37,38,39,],[42,42,42,42,42,]),'AMARILLO':([35,36,37,38,39,],[43,43,43,43,43,]),'NEGRO':([35,36,37,38,39,],[44,44,44,44,44,]),'PARC':([40,41,42,43,44,45,46,47,48,],[49,-9,-10,-11,-12,50,51,52,53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instrucciones':([4,],[5,]),'instruccion':([4,5,],[6,13,]),'color':([35,36,37,38,39,],[40,45,46,47,48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> NEW_PRINT ID PUNTOYCOMA instrucciones END_PRINT PUNTOYCOMA','start',6,'p_start','grammar.py',59),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','grammar.py',64),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','grammar.py',65),
  ('instruccion -> SET_PRINT_X PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA','instruccion',9,'p_instruccion','grammar.py',73),
  ('instruccion -> SET_PRINT_Y PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA','instruccion',9,'p_instruccion','grammar.py',74),
  ('instruccion -> SET_PRINT_O PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA','instruccion',9,'p_instruccion','grammar.py',75),
  ('instruccion -> SET_PRINT_TRIANGULO PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA','instruccion',9,'p_instruccion','grammar.py',76),
  ('instruccion -> SET_PRINT_ESTRELLA PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA','instruccion',9,'p_instruccion','grammar.py',77),
  ('color -> CYAN','color',1,'p_color','grammar.py',93),
  ('color -> MAGENTA','color',1,'p_color','grammar.py',94),
  ('color -> AMARILLO','color',1,'p_color','grammar.py',95),
  ('color -> NEGRO','color',1,'p_color','grammar.py',96),
]