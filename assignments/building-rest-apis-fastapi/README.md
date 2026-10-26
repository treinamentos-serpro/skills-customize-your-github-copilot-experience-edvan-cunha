# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando FastAPI. Pratique rotas HTTP, validação de dados e códigos de status em uma API com armazenamento temporário em memória.

## 📝 Tarefas

### 🛠️ Criar endpoints de leitura

#### Descrição

Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor a partir desta pasta com `uvicorn main:app --reload`. Implemente os endpoints para consultar os livros cadastrados.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books` para retornar a lista de livros em JSON.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID.
- Responder com status `404` quando o ID solicitado não existir.
- Permitir testar a API pela documentação interativa em `/docs`.

### 🛠️ Validar e cadastrar livros

#### Descrição

Adicione um endpoint para cadastrar livros. Use o modelo Pydantic fornecido no starter code para validar os dados recebidos no corpo da requisição.

#### Requisitos

O programa concluído deve:

- Implementar `POST /books` aceitando título, autor e ano de publicação.
- Validar os tipos dos campos usando o modelo Pydantic.
- Atribuir um ID único ao novo livro e incluí-lo na lista em memória.
- Retornar o livro criado com status `201`.
- Retornar um erro de validação para dados inválidos.

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```

### 🛠️ Atualizar e remover livros

#### Descrição

Complete as operações de gerenciamento implementando endpoints para atualizar e remover um livro existente.

#### Requisitos

O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar título, autor e ano.
- Implementar `DELETE /books/{book_id}` para remover o livro solicitado.
- Retornar status `404` quando a atualização ou remoção solicitar um ID inexistente.
- Retornar status `204` após remover um livro com sucesso.
- Manter as alterações disponíveis nas consultas seguintes enquanto o servidor estiver em execução.