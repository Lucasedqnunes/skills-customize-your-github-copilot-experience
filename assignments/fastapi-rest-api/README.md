# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python, praticando conceitos de rotas, métodos HTTP e manipulação de dados.

## 📝 Tasks

### 🛠️ Criar uma API de Gerenciamento de Itens

#### Description
Implemente uma API REST que permita criar, listar, buscar e remover itens de uma lista em memória. Utilize o FastAPI para definir as rotas e métodos HTTP.

#### Requirements
Completed program should:

- Definir rotas para:
  - Listar todos os itens (GET /items)
  - Adicionar um novo item (POST /items)
  - Buscar um item pelo ID (GET /items/{id})
  - Remover um item pelo ID (DELETE /items/{id})
- Utilizar um dicionário ou lista em memória para armazenar os itens
- Retornar respostas apropriadas para sucesso e erro
- Documentação automática disponível em /docs

Exemplo de uso:
```
POST /items {"name": "Caderno"} → 201 Created
GET /items → [ {"id": 1, "name": "Caderno"} ]
GET /items/1 → {"id": 1, "name": "Caderno"}
DELETE /items/1 → 204 No Content
```
