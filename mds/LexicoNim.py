import ply.lex as lex

reservadas = {
    'addr': 'ADDR', 
    'and':'AND',
    'as':'AS',
    'asm':'ASM',
    'bind':'BIND',
    'block':'BLOCK',
    'break':'BREAK',
    'case':'CASE',
    'cast': 'CAST', 
    'concept': 'CONCEPT',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'converter': 'CONVERTER',
    'defer': 'DEFER',
    'discard': 'DISCARD',
    'distinct': 'DISTINCT',
    'div': 'DIV',
    'do': 'DO',
    'elif': 'ELIF',
    'else': 'ELSE',
    'end': 'END',
    'enum': 'ENUM',
    'except': 'EXCEPT',
    'export': 'EXPORT',
    'finally': 'FINALLY',
    'for': 'FOR',
    'from': 'FROM',
    'func': 'FUNC',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'include': 'INCLUDE',
    'interface': 'INTERFACE',
    'iterator': 'ITERATOR',
    'let': 'LET',
    'macro': 'MACRO',
    'mixin': 'MIXIN',
    'mod': 'MOD',
    'nil': 'NIL',
    'not': 'NOT',
    'notin': 'NOTIN',
    'or': 'OR',
    'out': 'OUT',
    'proc': 'PROC',
    'ptr': 'PTR',
    'raise': 'RAISE',
    'return': 'RETURN',
    'shl': 'SHL',
    'shr': 'SHR',
    'static': 'STATIC',
    'template': 'TEMPLATE',
    'try': 'TRY',
    'tuple': 'TUPLE',
    'type': 'TYPE',
    'using': 'USING',
    'var': 'VAR',
    'when': 'WHEN',
    'while': 'WHILE',
    'xor': 'XOR',
    'yield': 'YIELD',
    'true': 'TRUE',
    'false': 'FALSE'
}

    
tokens = ['PLUS','MINUS','TIMES','DIVIDE','CARET','EXPONENT']+list(reservadas.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_CARET = r'\^'
t_EXPONENT = r'\**'

