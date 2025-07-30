# ✨ Linguagem Nim - Elementos Léxicos

Nim é uma linguagem de programação estática, imperativa e orientada a objetos, com sintaxe inspirada em Python. Ela é usada para demonstrar conceitos modernos de compilação e desempenho. A seguir, destacamos seus elementos léxicos:

#### 1. Palavras reservadas.

Nim apresenta apenas as seguintes palavras reservas: 
**if**, **else**, **while**, **for**, **proc**, **var**, **type**, **return** e **import**

**Regras:**  
- Palavras reservadas são palavras especiais da linguagem que não podem ser usadas diretamente como nomes de variáveis, funções ou outros identificadores.  
- Para usar uma palavra reservada como identificador, deve-se colocá-la entre acentos graves `` ` ``.

**Exemplo:**

```nim
var `if` = 10      # válido porque está entre acentos graves
# var if = 10      # inválido, gera erro pois 'if' é palavra reservada  

#### 2. Operadores

Nim apresenta os operadores aritméticos de **soma (+)**, **subtração (-)**, **multiplicação**  (*)**, **divisão (/)**, **módulo (mod)**, **exponenciação (^)**. Também apresenta o **operador =** para atribuições, além de operadores compostos como **+=**, **-=**. Nim possui a seguinte tabela de precedência, apresentada na ordem crescente de prescedência.

|   Grau de Precedência  |      Operador      |      Associatividade      |
|:----------------------:|:------------------:|:-------------------------:|
|          1             |     =, +=, -=      |   Direita para Esquerda   |
|          2             |        +, -        |   Esquerda para Direita   |
|          3             |      *, /, mod     |   Esquerda para Direita   |
|          4             |         ^          |   Direita para Esquerda   |


#### 3. Delimitadores
Comandos em Nim utilizam **;** pode ser usado para separar comandos na mesma linha, mas é opcional e raramente utilizado devido à indentação significativa. Parâmetros de funções utiliza **,** como delimitador. Adicionalmente, Nim utiliza os delimitadores **( )** para expressões e chamadas de funções. Dois-pontos **:** para indicar blocos de código (como em Python). Colchetes **[ ]** para listas, arrays e índices. Por fim, também é utilizado o delimitador **{ }** para conjuntos (sets).

#### 4. Identificadores

Para identificadores, Nim apresenta regra bastante empregada em diferentes linguagens de programação. Nim aceita como identificador qualquer sequência de **letras**, **dígitos** e **sublinhados**, apresentando as seguintes regras: 

Começa com pelo menos uma letra e depois o identificador pode conter **letras**, **'_'** e **números**.

Não termina com **'_'** .

Dois sublinhados imediatamente seguintes **"__"** não são permitidos.

São **case-sensitive** (variavel e Variavel são diferentes) e não podem coincidir com palavras reservadas. Abaixo, alguns exemplos de identifidores válidos:

```
variavel
_nome
soma2
calcula_media
```
#### 4.1 Palavras-chave como identificadores

Se uma palavra-chave estiver entre acentos graves, ela perderá sua propriedade de palavra-chave e se tornará um identificador comum.

```
var `var` = "Hello Stropping"
```
```
type Obj = object
  `type`: int

let `object` = Obj(`type`: 9)
assert `object` is Obj
assert `object`.`type` == 9

var `var` = 42
let `let` = 8
assert `var` + `let` == 50
```

#### 5. Strings

Podem ser delimitados por aspas duplas correspondentes e podem conter as seguintes sequências de escape:

| Sequência de escape | 	                Significado                        |
|:-------------------:|:----------------------------------------------------:|
| \n                  | Nova linha                                           |
| \t                  | Tabulação                                            |
| \\                  | Barra invertida                                      |
| \"                  | Aspas duplas dentro da string                        |
| \'                  | Apóstrofo dentro da string                           |
| \r                  | Retorno de carro (carriage return)                   |
| \xHH                | Caractere com código hexadecimal                     |


As Strings também podem ser delimitadas por três aspas duplas """ ... """. Podem ser executados por várias linhas, podem conter " e não precisa usar nenhuma sequência de escape. Quando a abertura """ é seguida por uma nova linha (pode haver espaço em branco entre a abertura """ e a nova linha), a nova linha (e o espaço em branco anterior) não é incluída na cadeia de caracteres. 

Exemplos: 
```
let = "Hello Word"
let = "Hello\nWord"
let mensagem = """Texto longo com "aspas" 
                e quebras de linha."""
```


#### 6. Números
 
Nim suporta os seguintes formatos numéricos:

- Inteiros: positivos ou negativos (ex: 10, -5)  
- Reais: números com ponto decimal (ex: 3.14)  
- Hexadecimais: prefixo 0x (ex: 0xFF)  
- Binários: prefixo 0b (ex: 0b1010)  
- Octais: prefixo 0o (ex: 0o755)  

Regras:

- O sinal `-` pode ser usado para números negativos.  
- Não há obrigatoriedade de sinal para números positivos.  

Exemplos:

```nim
let inteiro = 42
let negativo = -10
let real = 3.14
let hexadecimal = 0xFF
let binario = 0b1010
let octal = 0o755


#### 7. Comentários
Comentários de linha única começam com **#**.

Comentários de múltiplas linhas usam **#[ ... ]#**.

#### 8. Erros
Qualquer sequência de caracteres que não se enquadre nas regras acima é considerada um erro léxico.
Nim também acusa erro ao encontrar identificadores inválidos, números malformados ou uso incorreto de palavras reservadas. 

Espaços em branco, tabulações e quebras de linha são geralmente ignorados, exceto quando usados para definir blocos de código (indentação é significativa, como em Python).
