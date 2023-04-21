# BBB API Desafio

É recomendavel usar um ambiente virtual

No Linux e Mac

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Instalando as dependencias:

```shell
pip install -r requirements.txt
```

Para rodar a app:

```shell
uvicorn app:app --reload
```

Por padrão roda na porta 8000, em http://127.0.0.1:8000/docs você pode ver a documentação e executar as chamadas da API.

Quando um candidato é criado a app criara um arquivo candidatos.sqlite3, caso queria modificar a app para aceitar novos campos é só excluir esse arquivo

Alguns exemplos de Candidatos incritos:

````json
[
  {
    "nome": "Gabriel Froes",
    "email": "gabriel.ffroes123@g.globo",
    "sobre": "Gabriel, 27 anos, é um personal trainer que está sempre em busca do próximo desafio. Ele é apaixonado por atividades físicas e tem uma rotina intensa de treinos. Gabriel é competitivo, ambicioso e não mede esforços para alcançar seus objetivos. Ele está ansioso para participar do reality show e mostrar que pode vencer qualquer prova física que seja proposta.",
    "idade": 27,
    "avatar_url": "https://avatars.githubusercontent.com/u/19231904?v=4",
    "id": 1
  },
  {
    "nome": "Luis Santana",
    "email": "luis.santana@gmail.com",
    "sobre": "Luis Santana, 25 anos, é um aspirante a músico que cresceu em uma pequena cidade do interior. Ele abandonou a faculdade de direito para seguir seu sonho de se tornar um cantor. Luis é enérgico, confiante e nunca perde uma oportunidade de se apresentar. Ele está pronto para lutar por sua chance de se tornar uma estrela do pop em um reality show.",
    "idade": 25,
    "avatar_url": "https://avatars.githubusercontent.com/u/35848866?v=4",
    "id": 2
  },
  {
    "nome": "Vanessa Weber",
    "email": "vanessaaweber@g.globo",
    "sobre": "Vanessa, 30 anos, é uma influenciadora digital com mais de 1 milhão de seguidores nas redes sociais. Ela é uma mulher forte e confiante, que usa suas plataformas para inspirar outras mulheres a se amarem e se cuidarem. Vanessa é muito ligada à sua família e acredita que a união é a chave para o sucesso. Ela está animada para entrar no reality show e mostrar seu lado mais autêntico e vulnerável.",
    "idade": 30,
    "avatar_url": "https://avatars.githubusercontent.com/u/25768509?v=4r",
    "id": 3
  },
  {
    "nome": "Raquel Ramos",
    "email": "raquel.ramos@gmail.com",
    "sobre": "Raquel, 22 anos, é uma estudante de moda que sonha em se tornar uma designer renomada. Ela é uma jovem determinada, criativa e apaixonada por moda desde criança. Raquel tem um estilo único e está sempre experimentando novas tendências. Ela vê o reality show como uma oportunidade de mostrar seu talento para o mundo e provar que a moda é sua verdadeira paixão.",
    "idade": 22,
    "avatar_url": null,
    "id": 4
  }
]
````

Como avatar estamos usando a url da foto de perfil do GitHub