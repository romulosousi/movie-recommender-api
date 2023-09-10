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

Por padrão, a API estará disponível no link: https://127.0.0.1:8000/.

## Documentação

Após a instalação, toda a documentação da API pode ser encontrada no endereço: https://127.0.0.1/docs/. Os `endpoints` implementados são: 

* `/api/movies`: retorna os filmes da base;
* `/api/movies/{id}`: retorna um filme com um determinado `{id}`;
* `/api/users`: retorna todos os usuários da base;
* `/api/users/{id}`: retorna um usuário com um determinado `{id}`;
* `/api/movies_by_user/{user_id}`: retorna todos os filmes que foram avaliados por um usuário (`{user_id}`).
* `/api/users_by_movie/{movie_id}`: retorna todos os usuários que avaliaram um determinado filme (`{movie_id}`).
* `/api/recommender`: executa o processo de evolução e retorna uma recomendação para um determinado usuário. 

A implementação de cada rota dessa está dentrodo arquivo `main.py`. Lá é possível ver quais métodos utilizados para extrair cada uma das informações e como utiliza-los.

Os métodos para extrair informações do banco de dados está em `db.repositories` a partir das classes específicas para usuários, filmes e ratings. São eles:

### `MovieRepository`

* `find_all`: retorna todos os filmes da base.
* `find_by_id`: retorna um filme dado um id.
* `find_all_ids`: retorna todos os filmes de uma lista de ids.

### `UserRepository`

* `find_all`: retorna todos os usuários da base. 
* `find_by_id`: retorna um usuário dado um id.

### `RatingsRepository`

* `find_by_userdid`: retorna os ratings dados por usuário dado seu id. 
* `find_by_movieid`: retorna os ratings que um dado filme recebeu dado seu id.
* `find_by_movieid_list`: retorna todos os ratings dos filmes que estão em uma lista de ids. 

## Banco de Dados

A base de dados foi construída a partir dos arquivos da base _Small_ da [movielens](https://grouplens.org/datasets/movielens/). Foi utilizada uma versão modificada [esse script](https://github.com/dleehr/movielens-sqlite) para transformar os arquivos em um banco SQLite. Você pode encontrar o script modificado em [db/make_sqlite.sh]. Os links para as capas dos filmes foram obtidos a partir da biblioteca [Cinemagoer](https://cinemagoer.github.io/). O script para pegar o link está disponível me [db/load_posters.py]. 

### Tabelas do banco de dados

**users**

Tabela com a identificação de todos os usuários da base. Possui os campos:

* **userId**: id do usuário
* **userName**: nome do usuário

**movies**

Tabela com as informações dos filmes da base. Posui os campos:

* **movieId**: id do filme
* **title**: título do filme
* **year**: ano de lançamento do filme
* **genres**: string com os gêneros dos filmes, separados por |
* **url_poster**: URL para a capa do filme
* **imdbId**: id do filme na base do IMDb

**ratings**

Tabela com as avaliações de um usuário para um determinado filme. Possui os campos:

* **userId**: id do usuário que avaliou o filme;
* **movieId**: id do filme que foi avaliado;
* **rating**: nota que o usuário deu ao filme. Varia de 0.5 a 5;
* **timestamp**: informação de quando a avaliação foi feita.

As tabelas a seguir não são utilizadas neste código. 

**tags**

Tabela com as tags aplicadas por um usuário a um determinado filme. Possui os campos:

* **userId**: id do usuário que adicionou a tag;
* **movieId**: id do filme que recebeu a tag do usuário;
* **tag**: string com a tag fornecida pelo usuário;
* **timestamp**: informação de quando a tag foi aplicada.

**links**

Tabela que link os filmes com outras base de dados. Possui os campos:

* **movieId**: id do filme;
* **imdbId**: identificador do filme na base do IMDb: http://www.imdb.com/;
* **tmdbId**: identificador do filme na base do The Movie DB: https://www.themoviedb.org/.


## Algoritmo Genético

O algoritmo Genético é executado pelo _endpoint_ `/api/recommender` que é acessado a partir de um requisição POST com os seguintes parâmetros:

* **query_search**: id do usuário para quem a recomendação será aplicada;
* **individual_size**: tamanho do indivíduo. Um indivíduo é representado por um vetor de inteiros que correpondem aos ids dos filmes. Ou seja, esse parâmetro vai indicar quantas recomendações serão realizadas;
* **population_size**: tamanho da população. Indica quantos conjunto de recomendações serão evoluídos;
* **p_crossover**: probabilidade de crossover (Formato: 0 a 100);
* **p_mutation**: probabilidade de crosover (Formato: 0 a 100);
* **max_generation**: número máximo de gerações da evolução;
* **size_hall_of_fame**: quantidade de bons indivíduos que serão armazenados para o resultado final. Isso não é elitismo. O elitismo não está implementado ainda.
* **seed**: seed do aleatório.

O algoritmo esá implementado no arquivo [ga/algorithm.py](ga/algorithm.py) que utiliza a biblioteca DEAP e o método `eaSimple` para executar uma versão simples do algoritmo de evolução. 

A implementação do algoritmo é feita no arquivo [ga/mygenetic.py](ga/mygenetic.py) na classe `MyGeneticAlgorithm`. É nesta classe que está implementada a fitness a partir da função `evaluate`. 

O método recebe um indivíduo e retorna um valor que corresponde a qualidade daquele indivíduo. Neste caso, o indivíduo é uma lista de filmes que devem ser recomendados. 

A função atual implementada não leva em consideração o usuário. Ela apenas calcula a média dos ratings dos filmes da lista e retorna como "qualidade" da recomendação. O id do indivídul pode ser acessado pela informação `self.query_search`. 

