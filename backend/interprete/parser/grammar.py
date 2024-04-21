import ply.lex as lex
import ply.yacc as yacc
from ..SetPrint import SetPrint

reserved = {
    "new_print" : "NEW_PRINT",
    "set_print_x" : "SET_PRINT_X",
    "set_print_y" : "SET_PRINT_Y",
    "set_print_o" : "SET_PRINT_O",
    "set_print_triangulo" : "SET_PRINT_TRIANGULO",
    "set_print_estrella" : "SET_PRINT_ESTRELLA",
    "cyan" : "CYAN",
    "magenta" : "MAGENTA",
    "amarillo" : "AMARILLO",
    "negro" : "NEGRO",
    "end_print" : "END_PRINT"
}

tokens = [
    'PARA', 'PARC', 'COMA', 'PUNTOYCOMA',
    'NUMBER', 'ID', 
] + list(reserved.values())

t_PARA = r'\('
t_PARC = r'\)'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value} \n column: {t.lexpos} line: {t.lineno}')
        t.value = None
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    
    return t

t_ignore = " \t"
t_ignore_COMMENTLINE = r'\#(.*)'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    try:
        print(f'Error lexico {t.value} \n column: {t.lexpos} line: {t.lineno}')
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
    t.lexer.skip(1) # recuperacion del error

def p_start(p):
    '''start    : NEW_PRINT ID PUNTOYCOMA instrucciones END_PRINT PUNTOYCOMA'''
    p[0] = p[4]
    return p[0]

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion 
                     | instruccion'''
    if len(p) > 2:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_instruccion(p):
    '''instruccion : SET_PRINT_X PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA
                   | SET_PRINT_Y PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA
                   | SET_PRINT_O PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA
                   | SET_PRINT_TRIANGULO PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA
                   | SET_PRINT_ESTRELLA PARA NUMBER COMA NUMBER COMA color PARC PUNTOYCOMA'''
    
    if p[1] == 'set_print_x':
        p[0] = SetPrint('X', p[3], p[5], p[7])
    elif p[1] == 'set_print_y':
        p[0] = SetPrint('Y', p[3], p[5], p[7])
    elif p[1] == 'set_print_o':
        p[0] = SetPrint('O', p[3], p[5], p[7])
    elif p[1] == 'set_print_triangulo':
        p[0] = SetPrint('T', p[3], p[5], p[7])
    elif p[1] == 'set_print_estrella':
        p[0] = SetPrint('E', p[3], p[5], p[7])

    return p[0]

def p_color(p):
    '''color    : CYAN
                | MAGENTA
                | AMARILLO
                | NEGRO '''

    p[0] = p[1]
    return p[0]


def p_error(p):
    try:
        if p:
            print(f'Error sintactico linea:{p.lineno}, col:{p.lexpos} Token: {p.value}')
        else:
            print(f'Error de sintaxis  \n column: {p.lexpos} line: {p.lineno}')
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        
def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)


def parse(input_text):
    lex.lex() #lexico
    parser = yacc.yacc() #sintactico
    result = parser.parse(input_text)
    return result
