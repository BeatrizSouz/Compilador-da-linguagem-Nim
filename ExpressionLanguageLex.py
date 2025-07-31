import ply.lex as lex

reservadas = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR',
    'proc': 'PROC', 'var': 'VAR', 'type': 'TYPE',
    'return': 'RETURN', 'import': 'IMPORT'
}

tokens = [
    'ID', 'NUMBER', 'STRING',
    'SOMA', 'SUB', 'MUL', 'DIV', 'MOD', 'EXP',
    'ATRIB', 'ADICIGUAL', 'SUBIGUAL',
    'PV', 'VIRG', 'LPAREN', 'RPAREN',
    'LCHAV', 'RCHAV', 'LCOLCH', 'RCOLCH', 'DOISPONTOS'
] + list(reservadas.values())

t_SOMA       = r'\+'
t_SUB        = r'-'
t_MUL        = r'\*'
t_DIV        = r'/'
t_MOD        = r'\bmod\b'
t_EXP        = r'\^'
t_ATRIB      = r'='
t_ADICIGUAL  = r'\+='
t_SUBIGUAL   = r'-='
t_PV         = r';'
t_VIRG       = r','
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LCHAV      = r'\{'
t_RCHAV      = r'\}'
t_LCOLCH     = r'\['
t_RCOLCH     = r'\]'
t_DOISPONTOS = r':'

def t_ID(t):
    r'`?[a-zA-Z][a-zA-Z_0-9]*`?'
    lexema = t.value.strip('`')
    if lexema in reservadas and not (t.value.startswith('`') and t.value.endswith('`')):
        t.type = reservadas[lexema]
    else:
        t.type = 'ID'
        t.value = lexema
    return t

def t_NUMBER(t):
    r'0[xX][0-9a-fA-F]+|0[bB][01]+|0[oO][0-7]+|\d+\.\d+|\d+'
    if t.value.startswith(('0x', '0X')):
        t.value = int(t.value, 16)
    elif t.value.startswith(('0b', '0B')):
        t.value = int(t.value, 2)
    elif t.value.startswith(('0o', '0O')):
        t.value = int(t.value, 8)
    elif '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\"\"\"(.|\n)*?\"\"\"|\"(\\.|[^\\"])*\")'
    t.value = t.value[1:-1]
    return t

def t_comment_multiline(t):
    r'\#\[(.|\n)*?\]\#'
    pass

def t_comment_line(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

def main():
    f = open("input1.nim", "r")
    lexer = lex.lex(debug=1)
    lexer.input(f.read())
    print('\n\n# lexer output:')
    for tok in lexer:
        print('type:', tok.type, ', value:', tok.value)

if __name__ == "__main__":
    main()