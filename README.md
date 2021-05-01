# VC-X Solutions Challenge

Avaliação técnica para a posição de full-stack engineer (Python) na VC-X Solutions.

## Escopo

O objetivo aqui é realizar a implementação de duas estruturas de dados clássicas: a [fila](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) e [pilha](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)), não utilizando outras
estruturas auxiliares, que sejam nativas da linguagem de programação em questão (eg. listas, tuplas, etc.). A
especificação e demais orientações acerca da execução do teste, submetidas pela empresa, podem ser conferidas [aqui](./resources/VCX_README.md).

## Preliminares

### Requisitos

O seu workspace já deve possuir instalados os seguintes ítems:

* [Git](https://git-scm.com/downloads) 2.25.1;
* [Python](https://www.python.org/downloads/release/python-385/) 3.8.5.


Em relação ao gerador de ambientes virtuais para Python, nesse projeto foi utilizado o [venv](https://docs.python.org/3.8/library/venv.html). Para instalá-lo, execute no terminal:

```bash
sudo apt-get install python3-venv
```
### Ambiente virtual

De modo a instalar o ambiente virtual do Python, e as dependências de projeto, executar no terminal:

```bash
python3 -m venv env \                                  # Instala ambiente virtual
&& source env/bin/activate \                           # Ativa ambiente virtual localmente
&& pip install --upgrade pip --no-cache-dir \          # Instala e atualiza package manager, sem usar ~/.cache/pip
&& pip install -r requirements.txt --no-cache-dir      # Instala dependências de projeto, sem usar ~/.cache/pip
```

## Testes unitários

Com o ambiente virtual e dependências instaladas, os testes unitários pode ser executados. Nesse projeto, o [pytest](https://docs.pytest.org/en/6.2.x/) está
sendo utilizado, pelo fato de o mesmo possuir uma verbosidade superior ao [unittest](https://docs.python.org/3/library/unittest.html), (na minha opinião). Assim, para executar
os testes e também gerar o relatório de cobertura, execute no terminal:

```bash
pytest --cov=src -vv src/tests/
```

Caso você queira só executar os testes unitários, com verbosidade:

```bash
pytest -vv
```

## Code linting

Concernindo padronização de código, o code linting nesse projeto está sendo feito mediante a utilização da ferramenta [prospector](http://prospector.landscape.io/en/master/),
que por sua vez converge vários outros analisadores de integridade de código (como [mypy](http://mypy-lang.org/) para análise estática de tipos e [mccabe](), para
aferição de [complexidade ciclomática](https://en.wikipedia.org/wiki/Cyclomatic_complexity#:~:text=Cyclomatic%20complexity%20is%20a%20software,in%201976.)).

Para rodar o code linting no código em Python, basta executar:

```bash
prospector
```

A saída deverá, no cenário em que nenhuma inconsistência é encontrada, será similar à:

![image](https://user-images.githubusercontent.com/35070513/116793854-a9c95c80-aa9f-11eb-8503-b790123446ef.png)