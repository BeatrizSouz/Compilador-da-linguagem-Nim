# Rascunha da gramatica Nim
# program → funcdecl| funcdecl program | vardecl | vardecl program
# funcdecl → PROC ID ( sigparams ) : tipo body | PROC ID ( ) : tipo body
# sigparams → ID : tipo | ID : tipo , sigparams
# vardecl → VAR ID = exp | VAR ID : tipo
# body → : bloco
# bloco → comando | comando bloco
# comando → exp | while exp : bloco | if exp : bloco | if exp : bloco else : bloco | return exp
# call → ID ( params ) | ID ( )
# params → exp , params | exp
# assign → ID = exp | ID += exp | ID -= exp
# exp → exp + exp | exp * exp | exp ^ exp | call | assign | num | id

import ply.yacc as yacc
from NimLex import *   # aqui entraria seu analisador léxico
import SintaxeAbstrata as sa

# ------------------------------
# PROGRAM
# ------------------------------

def p_program1(p):
    '''program : decl'''
    p[0] = sa.SingleDeclProgram(p[1])

def p_program2(p):
    '''program : decl program'''
    p[0] = sa.CompoundDeclProgram(p[1], p[2])

# ------------------------------
# DECLARAÇÕES
# ------------------------------

def p_decl_vardecl(p):
    '''decl : vardecl'''
    p[0] = sa.VarDecl(p[1])

def p_decl_typedecl(p):
    '''decl : typedecl'''
    p[0] = sa.TypeDecl(p[1])

def p_decl_procdecl(p):
    '''decl : procdecl'''
    p[0] = sa.ProcDecl(p[1])

def p_decl_comando(p):
    '''decl : comando'''
    p[0] = sa.CommandDecl(p[1])

# ------------------------------
# VARIÁVEIS E TIPOS
# ------------------------------

def p_vardecl_assign(p):
    '''vardecl : VAR ID IGUAL expressao'''
    p[0] = sa.VarAssignDecl(p[2], p[4])

def p_vardecl_type(p):
    '''vardecl : VAR ID DOISPT tipo'''
    p[0] = sa.VarTypedDecl(p[2], p[4])

def p_typedecl(p):
    '''typedecl : TYPE ID IGUAL OBJECT LCHAV campos RCHAV'''
    p[0] = sa.TypeDeclConcrete(p[2], p[6])

def p_campos_single(p):
    '''campos : campo'''
    p[0] = sa.SingleCampo(p[1])

def p_campos_compound(p):
    '''campos : campo campos'''
    p[0] = sa.CompoundCampo(p[1], p[2])

def p_campo(p):
    '''campo : ID DOISPT tipo'''
    p[0] = sa.Campo(p[1], p[3])

# ------------------------------
# PROC
# ------------------------------

def p_procdecl(p):
    '''procdecl : PROC ID LPAREN parametros_opt RPAREN DOISPT tipo corpo'''
    p[0] = sa.ProcDeclConcrete(p[2], p[4], p[7], p[8])

def p_parametros_opt1(p):
    '''parametros_opt : parametros'''
    p[0] = p[1]

def p_parametros_opt2(p):
    '''parametros_opt : '''
    p[0] = None

def p_parametros_single(p):
    '''parametros : parametro'''
    p[0] = sa.SingleParam(p[1])

def p_parametros_compound(p):
    '''parametros : parametro COMMA parametros'''
    p[0] = sa.CompoundParams(p[1], p[3])

def p_parametro(p):
    '''parametro : ID DOISPT tipo'''
    p[0] = sa.Parametro(p[1], p[3])

# ------------------------------
# CORPO E BLOCOS
# ------------------------------

def p_corpo(p):
    '''corpo : DOISPTO bloco'''
    p[0] = sa.Corpo(p[2])

def p_bloco_single(p):
    '''bloco : comando'''
    p[0] = sa.SingleComando(p[1])

def p_bloco_compound(p):
    '''bloco : comando bloco'''
    p[0] = sa.CompoundComando(p[1], p[2])

# ------------------------------
# COMANDOS
# ------------------------------

def p_comando_atribuicao(p):
    '''comando : atribuicao'''
    p[0] = p[1]

def p_comando_chamada(p):
    '''comando : chamada'''
    p[0] = p[1]

def p_comando_while(p):
    '''comando : WHILE expressao DOISPTO bloco'''
    p[0] = sa.While(p[2], p[4])

def p_comando_ifelse1(p):
    '''comando : IF expressao DOISPTO bloco'''
    p[0] = sa.If(p[2], p[4])

def p_comando_ifelse2(p):
    '''comando : IF expressao DOISPTO bloco ELSE DOISPTO bloco'''
    p[0] = sa.IfElse(p[2], p[4], p[7])

def p_comando_return(p):
    '''comando : RETURN expressao'''
    p[0] = sa.Return(p[2])

# ------------------------------
# ATRIBUIÇÃO
# ------------------------------

def p_atribuicao_eq(p):
    '''atribuicao : ID IGUAL expressao'''
    p[0] = sa.Assign(p[1], p[3])

def p_atribuicao_add(p):
    '''atribuicao : ID MAISIGUAL expressao'''
    p[0] = sa.AssignAdd(p[1], p[3])

def p_atribuicao_sub(p):
    '''atribuicao : ID MENOSIGUAL expressao'''
    p[0] = sa.AssignSub(p[1], p[3])

# ------------------------------
# CHAMADAS E ARGUMENTOS
# ------------------------------
def p_chamada_args(p):
    '''chamada : ID LPAREN argumentos RPAREN'''
    p[0] = sa.Call(p[1], p[3])

def p_chamada_noargs(p):
    '''chamada : ID LPAREN RPAREN'''
    p[0] = sa.Call(p[1], None)

def p_argumentos_single(p):
    '''argumentos : expressao'''
    p[0] = sa.SingleArg(p[1])

def p_argumentos_compound(p):
    '''argumentos : expressao COMMA argumentos'''
    p[0] = sa.CompoundArgs(p[1], p[3])

# ------------------------------
# EXPRESSÕES
# ------------------------------

def p_expressao_binop(p):
    '''expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao VEZES expressao
                 | expressao DIV expressao
                 | expressao MOD expressao
                 | expressao POT expressao'''
    p[0] = sa.BinOp(p[1], p[2], p[3])

def p_expressao_chamada(p):
    '''expressao : chamada'''
    p[0] = p[1]

def p_expressao_numero(p):
    '''expressao : NUMBER'''
    p[0] = sa.Num(p[1])

def p_expressao_string(p):
    '''expressao : STRING'''
    p[0] = sa.String(p[1])

def p_expressao_id(p):
    '''expressao : ID'''
    p[0] = sa.Id(p[1])
  
# ------------------------------
# TIPOS
# ------------------------------
def p_tipo(p):
    '''tipo : ID'''
    p[0] = sa.Tipo(p[1])
# ------------------------------
# ERROS
# ------------------------------
def p_error(p):
    print("Syntax error in input!", p)
# ------------------------------
# MAIN
# ------------------------------
def main():
    f = open("input.nim", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)
    print(result)

if __name__ == "__main__":
    main()
