# **Documentação Sintática da Linguagem Nim**

---

## 1. Elementos Sintáticos

Um programa em Nim é composto por **declarações de variáveis**, **definições de tipos**, **procedimentos (funções)** e **comandos**. Um procedimento possui sintaxe semelhante a Python, com indentação significativa e blocos delimitados por dois-pontos `:`.

A regra geral para um procedimento é:

```
proc → "proc" ID "(" parametros ")" ":" tipoRetorno corpo
```

Onde:
- `proc` é a palavra-chave para definição de procedimento,
- O primeiro `ID` é o nome do procedimento,
- `parametros` são os argumentos (podem ser vazios),
- `tipoRetorno` indica o tipo de retorno após os dois-pontos,
- `corpo` representa uma sequência indentada de comandos.

---

## 1.1 Comandos da Linguagem Nim

Os comandos que Nim aceita neste subconjunto são:

```
comando → atribuicao
        | chamada
        | whileLoop
        | ifElse
        | return
```

### Atribuição:
```
atribuicao → ID "=" expressao
           | ID "+=" expressao
           | ID "-=" expressao
```

### Chamada de Procedimento:
```
chamada → ID "(" argumentos? ")"
```

### Laço While:
```
whileLoop → "while" expressao ":" bloco
```

### Condicional If/Else:
```
ifElse → "if" expressao ":" bloco ("else" ":" bloco)?
```

### Comando Return:
```
return → "return" expressao
```

---

## 1.2 Expressões

As expressões em Nim incluem operadores aritméticos, números, identificadores, chamadas de função, strings e precedência por parênteses.

```
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
```

---

## 1.3 Parâmetros e Argumentos

### Parâmetros:
```
parametros → parametro ("," parametro)*
parametro → ID ":" tipo
```

### Argumentos:
```
argumentos → expressao ("," expressao)*
```

---

## 1.4 Tipos

Tipos são identificadores literais como `int`, `string`, etc. ou estruturas definidas pelo usuário com `type`.

```
tipo → ID
```

---

# 2. Exemplos de Código na Linguagem Nim

---

### Exemplo 1 – Procedimento com retorno e parâmetros:

```nim
proc saudacao(): string =
  return "Olá, mundo!"
```

---

### Exemplo 2 – Tipos e variáveis:

```nim
type Pessoa = object
  nome: string
  idade: int

var p: Pessoa
p.nome = "João"
p.idade = 30
```

---

### Exemplo 3 – Operações aritméticas e atribuições compostas:

```nim
var x = 10
x += 5
x -= 2
```

---

### Exemplo 4 – While com expressões:

```nim
var contador = 0
while contador < 5:
  contador += 1
```

---

### Exemplo 5 – If/Else e chamadas:

```nim
proc verificaIdade(idade: int): string =
  if idade >= 18:
    return "Maior de idade"
  else:
    return "Menor de idade"
```

---

### Exemplo 6 – Strings multilinha:

```nim
let texto = """Essa é uma string
multilinha com "aspas" e quebras."""
```