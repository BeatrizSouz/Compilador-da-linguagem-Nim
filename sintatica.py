import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens
import logging


def p_programa(p):
    '''Programa : smt 
                | smt PV'''
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

def p_ifStm(p):
    '''ifStm : IF exp DOISPONTOS codigo
             | IF exp DOISPONTOS codigo cond ifStm'''
    if len(p) == 10:
        p[0] = [p[2],p[3]]
    else:
        p[0] = [p[5],p[6]] + p[7]

def p_whenStm(p):
    '''whenStm : WHEN exp DOISPONTOS codigo
        | WHEN exp DOISPONTOS codigo cond whenStm'''

def p_whileStm(p):
    '''whileStm : WHILE exp DOISPONTOS codigo
                | WHILE exp DOISPONTOS codigo whileStm'''

def p_cond(p):
    '''cond :  ELIF exp DOISPONTOS codigo
            | ELIF exp DOISPONTOS codigo cond 
            | ELSE DOISPONTOS 
            | ELSE DOISPONTOS cond '''

def p_codigo(p):
    '''cond : ELIF exp DOISPONTOS codigo
            | ELIF exp DOISPONTOS codigo cond 
            | ELSE DOISPONTOS 
            | ELSE DOISPONTOS cond '''
