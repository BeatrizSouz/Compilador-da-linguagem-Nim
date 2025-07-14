# ✨ Linguagem Nim - Elementos Léxicos

Nim é uma linguagem de programação estática, imperativa e orientada a objetos, com sintaxe inspirada em Python. Ela é usada para demonstrar conceitos modernos de compilação e desempenho. A seguir, destacamos seus elementos léxicos:

#### 1. Palavras reservadas.

Nim apresenta apenas as seguintes palavras reservas: 
**addr**, **and**,**as**,**asm**,**bind**, **block**, **break**,**case**,**cast**, **concept**,  **const**, **continue**, **converter**,**defer**, **discard**, **distinct**, **div**, **do**,**elif**, **else**, **end**, **enum** **except**, **export**
**finally**, **for**, **from**, **func**,**if**, **import**, **in**, **include**, **interface**, **iterator**,
**let**,**macro**, **mixin**, **mod**,**nil**, **not**, **notin**,**or**, **out**,**proc**, **ptr**,**raise**, **return**,**shl**, **shr**, **static**,**template**, **try**, **tuple**, **type**,**using**,**var**,**when**, **while**,**xor**,**yield**, **true** e **false**.   

#### 2. Operadores

Nim apresenta os operadores aritméticos de **soma (+)**, **subtração (-)**, **multiplicação**  (*)**, **divisão (/)**, **módulo (mod)**, **exponenciação (^)**. Também apresenta o **operador =** para atribuições, além de operadores compostos como **+=**, **-=**. Nim possui a seguinte tabela de precedência, apresentada na ordem crescente de prescedência.

| Grau de Precedência | 	  Operador               |     Associativade     |
|:-------------------:|:----------------------------:|:---------------------:|
|          1          |     =, :=, +=, -=, *=, /=    | Direita para Esquerda |
|          2          |   	   or,xor                | Esquerda para direita |
|          3          |     	    and              | Esquerda para direita |
|          4          |             not              | Direita para Esquerda |
|          5          |    ==, !=, <, >, <=, >=, in  | Esquerda para direita |
|          6          |             +, -             | Esquerda para direita |
|          7          |    *, /, div, mod, shl, shr  | Esquerda para direita |
|          8          |              ^    	         | Direita para Esquerda |


#### 3. Delimitadores
Comandos em Nim utilizam **;** pode ser usado para separar comandos na mesma linha, mas é opcional e raramente utilizado devido à indentação significativa. Parâmetros de funções utiliza **,** como delimitador. Adicionalmente, Nim utiliza os delimitadores **( )** para expressões e chamadas de funções. Dois-pontos **:** para indicar blocos de código (como em Python). Colchetes **[ ]** para listas, arrays e índices. Por fim, também é utilizado o delimitador **{ }** para conjuntos (sets).

#### 4. Identificadores

Para identificadores, Nim apresenta regra bastante empregada em diferentes linguagens de programação. Nim aceita como identificador válido qualquer sequência de símbolos iniciada por **letras** ou **_**. Após esse simbolo inicial, o identificador pode conter **letras**, **_** e **números**. São **case-sensitive** (variavel e Variavel são diferentes) e não podem coincidir com palavras reservadas. Abaixo, alguns exemplos de identifidores válidos:

```
variavel
_nome
soma2
calcula_media
```
#### 5. Números

Nim dá suporte a números **inteiros**, **reais**, **Hexadecimais**, **Binários** e **Octais**. Os números podem ser positivos ou negativos. Para inteiros, não há obrigatoriedade de sinal, mas o uso de **-** é permitido para negativos.

#### 6. Comentários
Comentários de linha única começam com **#**.

Comentários de múltiplas linhas usam **#[ ... ]#**.

#### 7. Erros
Qualquer sequência de caracteres que não se enquadre nas regras acima é considerada um erro léxico.
Nim também acusa erro ao encontrar identificadores inválidos, números malformados ou uso incorreto de palavras reservadas. 

Espaços em branco, tabulações e quebras de linha são geralmente ignorados, exceto quando usados para definir blocos de código (indentação é significativa, como em Python).