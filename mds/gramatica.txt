Program :smt 
         |smt IND{=}
         |smt; 

Smt : ifStm
     |whenStm
     |whileStm
     |ForStm

ifStm : IF exp DOISPONTOS codigo
      |IF exp DOISPONTOS codigo cond ifStm

#dúvida em when só aceita exp como constante ou nada que seja definido em tempo de execução. Tenho que mudar a regra por causa disso ?

whenStm : WHEN exp DOISPONTOS codigo
        | WHEN exp DOISPONTOS codigo cond whenStm

whileStm : WHILE exp DOISPONTOS codigo
          |WHILE exp DOISPONTOS codigo whileStm

cond : ELIF exp DOISPONTOS codigo
       |ELIF exp DOISPONTOS codigo cond 
       |ELSE DOISPONTOS 
       |ELSE DOISPONTOS cond 