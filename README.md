# Desafio Tech (Python)
<!--ts-->
* API usando a linguagem Python, frameworks: Django e Django Rest Framework
* Comunicação com banco de dados SQLite
* Aplicação possui duas tabelas: Region e Fruit, associação por chave estrangeira (foreign key)
* Métodos: GET, POST, PUT e DELETE
<!--te-->

```bash
# Clone este repositório
$ git clone https: <https://github.com/fernandanaser/DesafioTech.git>

# Criando a Virtual Env
$ python -m venv venv  

# Ativando a Venv
$ venv\Scripts\activate

# Instalando as dependências
$ pip install -r requirements.txt

# Configurar migrations
$ python manage.py makemigrations desafioapp
$ python manage.py migrate desafioapp

# Execute a aplicação em modo de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000/>
```
#Endpoints Region

`GET` <http://127.0.0.1:8000/region/>

`POST` <http://127.0.0.1:8000/region/>

  Body:
```json
  {
    "name": ""
  }
  ```

`PUT` <http://127.0.0.1:8000/region/:id/>

  Body:
```json
  {
    "id": ""
    "name": ""
  }
  ```
`DELETE` <http://127.0.0.1:8000/region/:id/>

#Endpoints Fruit

`GET` <http://127.0.0.1:8000/fruit/>

`POST` <http://127.0.0.1:8000/fruit/>

  Body:
```json
  {
    "name": ""
  }
```
`PUT` <http://127.0.0.1:8000/fruit/:id/>

  Body:
```json
  {
    "id": ""
    "name": ""
  }
```
`DELETE` <http://127.0.0.1:8000/fruit/:id/>


