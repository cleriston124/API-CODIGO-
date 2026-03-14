# API-favip com Flask

API simples desenvolvida em Python utilizando o  Flask.
Ela permite realizar operações matemáticas básicas através de parâmetros enviados pela URL.

## Tecnologias utilizadas

* Python
* Flask

## Operações disponíveis

A API realiza as seguintes operações matemáticas:

* Soma
* Subtração
* Multiplicação
* Divisão

## Como funciona

A API recebe três parâmetros na URL:

* **n1** → primeiro número
* **n2** → segundo número
* **op** → operação matemática

## Estrutura da URL

```
http://localhost:5000/calcular?n1=NUMERO&n2=NUMERO&op=OPERACAO
```

## Exemplos de uso

### Soma

```
http://localhost:5000/calcular?n1=10&n2=5&op=soma
```

Resposta:

```json
{
 "numero1": 10,
 "numero2": 5,
 "operacao": "soma",
 "resultado": 15
}
```

### Subtração

```
http://localhost:5000/calcular?n1=10&n2=5&op=subtracao
```

### Multiplicação

```
http://localhost:5000/calcular?n1=10&n2=5&op=multiplicacao
```

### Divisão

```
http://localhost:5000/calcular?n1=10&n2=5&op=divisao
```

## Como executar o projeto

### 1 - Instalar as dependências

```
pip install flask
```

### 2 - Executar o projeto

```
python api.py
```

### 3 - Abrir no navegador

Depois de iniciar o servidor, utilize a URL:

```
http://localhost:5000/calcular
```

## alunos

clériston carlos gomes do nascimento-202503330409
João Lucas Araújo Caetano-202502587121
