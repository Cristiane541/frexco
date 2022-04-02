# frexco

<h1 align="center">Desafio Tech</h1> 


<p align="justify">🚀  Criar uma API usando a linguagem Python, frameworks: Django e Django Rest Framework.</p>
 A API deverá realizar a comunicação com um banco de dados SQL qualquer (pode ser SQLite)
 O banco deverá ter pelo menos duas tabelas: </p>
<p align="justify">       - Uma tabela chamada “Region” que conterá apenas uma coluna “name” com informação dos nomes das regiões do Brasil ( Norte, Nordeste, etc.)</p>
<p align="justify">          - Uma tabela chamada “Fruit” que conterá colunas “name” (o nome da fruta) e uma coluna de associação por chave estrangeira (foreign key) com a tabela “Region” associando cada fruta a uma região existente na primeira tabela.</p>
<p align="justify">- Para cada tabela, a API deve conter os quatro métodos GET, POST, PUT e DELETE.</p>

<p align="left"> Versões utilizadas por essa aplicação: <br>
 
```
Django==4.0.*
djangorestframework==3.13.*
python-decouple==3.*
django-extensions==3.1.*
```
<h2 align="left">Como executar o projeto:</h2> 

- Clone esse repositório; <br>
- Crie um virtualenv com Python 3.6; <br>
- Crie um arquivo `.env` na pasta principal e dentro dele escreva `SECRET_KEY=password-not-secure`
- Ative o virtualenv; <br>
- Instale as dependências; <br>
- Rode as migrações.

```
git clone https://github.com/Cristiane541/frexco
cd frexco
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```
