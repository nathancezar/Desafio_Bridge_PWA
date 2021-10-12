# Desafio de Desenvolvimento Bridge

Aplicação que calcula o menor número real duodigito múltiplo de X, com X > 100.
## Dependências

### Backend
    - Python 3.8.10
    - pip = 21.2.4
    - pipenv = 2021.5.29
    - peewee = 3.14.4
    - tornado = 6.1

### Frontend
    - Node = 16.10.0
    - NPM = 7.24.0
    - Vue = 2.6.11
    - Bootstrap-vue = 2.21.2

### Banco de Dados
    - Sqlite3 = 5.0.2

## Ambiente de Desenv.
    - Ubuntu 20.04
    - Visual Studio Code

# Instalação

## Banco de dados

Criação de um novo Banco de Dados:

```sh
$ cd backend-python/database/
$ npm run create
```

## Server
Para executar o server:

```sh
$ cd backend-python/
$ python main.py
```
o Servidor ficara escutando em http://localhost:8888

## Aplicação
Para acessar a plicação no navegador:

```sh
$ cd bridge/
$ npm run serve
```
A aplicação ficará acessível em http://localhost:8080/

# Uso

O usuário deve inserir um número real maior que 100 e clicar em "Calcular menor duodigito".
O resultado e o tempo de execução aparecerão em um log abaixo do botão.
A aplicação salva cada novo valor no banco de dados. Para visualizar os valores salvos é necessário
acessar o banco de dados "backend-python/database/duodigito.db" com uma IDE. (exemplo DBeaver).
Como não foi passado limite de tempo ou de tentativas, não foi implementada nenhuma exceção para
parar o algoritmo, o que pode causar um loop infinito.

O algoritmo usado para encontrar o multiplo duodigito pode ser testado isoladamente, apenas com uso do python.
Para isso deve-se acessar:

```sh
$ cd backend-python/engine/
```
E executar o script "calculate_duodigito.py", passando um número como argumento.
Exemplo:

```sh
$ python calculate_duodigito.py -n 290
```


