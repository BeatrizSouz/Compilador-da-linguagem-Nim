import ply.lex as lex

reservadas = {
    'if': 'IF', 'elif':'ELIF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR',
    'proc': 'PROC', 'var': 'VAR', 'type': 'TYPE',
    'return': 'RETURN', 'import': 'IMPORT'
}

tokens = [
    'ID', 'INTNUMBER','FLOATNUMBER','HEX_INTNUMBER','BIN_INTNUMBER','OCT_INTNUMBER', 'STRING',
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

# permite "_" como separador dentro dos literais
underscore_digits = r'(?:[0-9]|_)+'

def _clean_underscores(s):
    return s.replace('_', '')


def t_HEX_INTNUMBER(t):
    r'0[xX](?:[0-9a-fA-F]|_)+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 16)
    return t


def t_BIN_INTNUMBER(t):
    r'0[bB][01_]+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 2)
    return t


def t_OCT_INTNUMBER(t):
    r'0[oO][0-7_]+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 8)
    return t


def t_FLOATNUMBER(t):
    r'\d+(?:_\d+)*\.\d+(?:_\d+)*(?:[eE][+-]?\d+(?:_\d+)*)?'
    raw = t.value
    t.value = float(_clean_underscores(raw))
    return t


def t_INTNUMBER(t):
    r'\d+(?:_\d+)*'
    raw = t.value
    t.value = int(_clean_underscores(raw))
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

#[if __name__ == "__main__":main()]#

lexer = lex.lex()
entrada = "0x1f 0b1011 0o755 let cad = 5\nvar a: int\nvar x: 6.02e23\nif cad == 0:\n   a = 3 mod 5 \n else:\n  x = 5.56 + 123.4\necho a\necho x\n"
lexer.input(entrada)
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos)