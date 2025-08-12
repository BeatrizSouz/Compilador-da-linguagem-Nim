import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens
import logging


def p_programa(p):
    '''Programa : smt 
                | smt IND{=}
                | smt;'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[1]
    

def p_smt(p):
    '''Smt : ifStm
           | whenStm
           | whileStm
           | ForStm'''
    p[0] =  p[1]

def p_tipo(p):
    '''tipo : inteiro
            | float
            | boolean
            | string
            | char'''
    p[0] = p[1]

def p_inteiro(p):
     '''inteiro : INT
                | INT8
                | INT16
                | INT32
                | INT64'''
     p[0] = p[1]

def p_float(p):
    '''float : FLOAT32
             | FLOAT64'''
    
    p[0] = p[1]

def p_boolean(p):
    '''boolean : BOOL'''
    p[0] = p[1]

def p_string(p):
    '''string : STRING'''
    p[0]= p[1]

def p_char(p):
    '''char : CHAR'''
    p[0] = p[1]
