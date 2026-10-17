# Estom

O Estom é um sistema de monitoramento de preços criado para ajudar pessoas que
desejam acompanhar produtos online sem precisar verificar manualmente seus
preços todos os dias.

O projeto está sendo desenvolvido durante o Coffee & Code da PUCPR e será
evoluído ao longo das próximas semanas.

## Objetivo

A primeira versão do Estom será focada no monitoramento de produtos do
Mercado Livre.

O usuário poderá cadastrar produtos, definir opcionalmente um preço máximo
desejado e acompanhar a situação do preço em relação à meta definida.

Futuramente, o sistema também deverá realizar o monitoramento automático dos
preços e enviar alertas quando as condições definidas pelo usuário forem
atingidas.

## Estado atual

Atualmente, o frontend inicial da aplicação está implementado utilizando
HTML, CSS e JavaScript.

A interface possui:

- visualização dos produtos monitorados;
- diferentes estados em relação à meta de preço;
- formulário de cadastro através de modal;
- tema claro e escuro;
- layout responsivo para desktop e dispositivos móveis;
- navegação por teclado;
- padrões visuais definidos através de um Design System.

Os produtos e preços apresentados atualmente são dados de demonstração.

## Funcionalidades planejadas

- Cadastro de usuários;
- Cadastro de produtos para monitoramento;
- Monitoramento diário de preços;
- Definição opcional de preço máximo;
- Armazenamento do histórico de preços;
- Alertas por e-mail quando o preço desejado for atingido;
- Pausa, edição e exclusão de produtos monitorados.

## Tecnologias utilizadas

Nesta etapa do projeto foram utilizadas:

- HTML5;
- CSS3;
- JavaScript.

Novas tecnologias poderão ser adicionadas conforme a evolução da aplicação.

## API REST

A API REST do Estom está sendo desenvolvida com Python e FastAPI. Nesta etapa, ela permite cadastrar, listar, consultar, atualizar e excluir produtos monitorados.

Os dados são armazenados temporariamente em memória, portanto são perdidos quando a aplicação é reiniciada.


### Requisitos

- Python instalado;
- pip para instalação das dependências.

### Instalação

Na raiz do projeto, crie e ative um ambiente virtual.

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

Com o ambiente virtual ativado, execute na raiz do projeto:

```bash
uvicorn api.main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

### Documentação interativa

Com a API em execução, acesse:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [OpenAPI JSON](http://127.0.0.1:8000/openapi.json)

### Endpoints disponíveis

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/produtos` | Cadastra um produto |
| GET | `/produtos` | Lista os produtos |
| GET | `/produtos/{produto_id}` | Consulta um produto |
| PUT | `/produtos/{produto_id}` | Substitui os dados de um produto |
| PATCH | `/produtos/{produto_id}` | Atualiza parcialmente um produto |
| DELETE | `/produtos/{produto_id}` | Exclui um produto |
| GET | `/categorias` | Lista as categorias |
| GET | `/categorias/{categoria_id}` | Consulta uma categoria por ID |

A API valida os dados recebidos e utiliza códigos de status HTTP para indicar sucesso ou erros nas operações.

## Interface

A interface segue uma abordagem mobile-first e utiliza componentes e tokens
visuais documentados no Design System.

Também foram implementados temas claro e escuro, além de cuidados com
contraste, navegação por teclado e foco visível.

A interface foi auditada utilizando o Lighthouse e atingiu pontuação 100 na
categoria Accessibility.

## Protótipo

O fluxo inicial da aplicação foi desenvolvido no Figma.

[Acessar protótipo no Figma](https://www.figma.com/proto/oL9MehNA1Gea3Zhzh8I69z/Sem-t%C3%ADtulo?node-id=0-1)

## Documentação

A documentação do projeto está disponível na pasta [docs](./docs).

- [Requisitos](./docs/requisitos.md)
- [Histórias de usuário](./docs/historias-de-usuario.md)
- [Design System](./docs/design-system.md)
- [Arquitetura inicial](./docs/arquitetura.md)

## Estrutura do projeto

```text
Estom/
├── api/
│   ├── main.py
│   ├── dados.py
│   └── schemas.py
├── assets/
│   ├── css/
│   ├── images/
│   └── js/
├── docs/
├── supabase/
├── index.html
├── login.html
├── perfil.html
├── requirements.txt
└── README.md
```

## Status do projeto

Em desenvolvimento.

O Estom está sendo desenvolvido de forma incremental durante os encontros do
Coffee & Code da PUCPR.

## Escopo inicial

A primeira versão será focada no Mercado Livre.

Outras lojas e funcionalidades adicionais poderão ser consideradas em versões
futuras.