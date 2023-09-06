# GA Recommender

 Essa api foi construída para implementar o algoritmo genético para sistemas de recomendacão. Esse codigo foi criado com propósito educativo, sendo base para atividades desenvolvidas na disciplina de Inteligência Artificial. 

## Instalação

A API foi desenvolvida utilizando o [FastAPI](https://fastapi.tiangolo.com/) e todos os requisitos estão presentes no arquivo [requirements.txt](requirements.txt). 

Para istalar, use o comando: 

```bash
pip install -r requirements.txt
```

Os requisitos são: 

* [fastapi](https://fastapi.tiangolo.com/): Biblioteca de criação da API
* [SQLAlchemy](https://www.sqlalchemy.org/): Biblioteca para gerenciamento do banco de dados
* [uvicorn](https://www.uvicorn.org/): Servidor Web para execução da API.
* [deap](https://deap.readthedocs.io/en/master/): Biblioteca para implementação do Algoritmo Genético.

## Execução 

Após a instalação de toos os requisitos, a API pode ser executada localmente utilizando o comando: 

```bash
uvicorn main:app --reload
```

Por padrão, a API Vai está disponível no link: https://127.0.0.1:8000/.

## Doumentação

Após a instalação, toda a documentação da API pode ser encontrada no endereço: https://127.0.0.1/docs/. Os `endpoints` implementados são: 

* `/api/movies`: retorna os filmes da base;
* `/api/movies/{id}`: retorna um filme com um determinado `{id}`;
* `/api/users`: retorna todos os usuários da base;
* `/api/users/{id}`: retorna um usuário com um determinado `{id}`;
* `/api/movies_by_user/{user_id}`: retorna todos os filmes que foram avaliados por um usuário (`{user_id}`).
* `/api/users_by_movie/{movie_id}`: retorna todos os usuários que avaliaram um determinado filme (`{movie_id}`).
* `/api/recommender`: executa o processo de evolução e retorna uma recomendação para um determinado usuário. 

## Banco de Dados

