# Gramática Livre de Contexto para a Linguagem Nim 
```
program → decl | decl program

decl → varDecl 
      | typeDecl 
      | procDecl
      | comando

varDecl → VAR ID "=" expressao
         | VAR ID ":" tipo

typeDecl → TYPE ID "=" "object" "{" campos "}"

campos → campo | campo campos
campo → ID ":" tipo

procDecl → PROC ID "(" parametros? ")" ":" tipo corpo

parametros → parametro | parametro "," parametros
parametro → ID ":" tipo

corpo → ":" bloco

bloco → comando 
       | comando bloco

comando → atribuicao 
         | chamada 
         | whileLoop 
         | ifElse 
         | return

atribuicao → ID "=" expressao
           | ID "+=" expressao
           | ID "-=" expressao

chamada → ID "(" argumentos? ")"

argumentos → expressao | expressao "," argumentos

whileLoop → WHILE expressao ":" bloco

ifElse → IF expressao ":" bloco 
        | IF expressao ":" bloco ELSE ":" bloco

return → RETURN expressao

expressao → expressao "+" expressao
           | expressao "-" expressao
           | expressao "*" expressao
           | expressao "/" expressao
           | expressao "mod" expressao
           | expressao "^" expressao
           | chamada
           | NUMBER
           | STRING
           | ID

tipo → ID
``
