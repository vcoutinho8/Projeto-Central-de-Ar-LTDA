# Sistema de Gestão de Vendas e Relatórios Gerenciais

Projeto desenvolvido para a disciplina de **Banco de Dados II**, com o objetivo de informatizar o setor de vendas de uma empresa, centralizando dados operacionais e gerando **relatórios gerenciais estratégicos** a partir de um banco de dados relacional robusto.

O sistema foi projetado com foco em **modelagem de dados**, **integridade relacional**, **regra de negócio realista** e **arquitetura web moderna**, utilizando backend em API REST e frontend desacoplado.

---

## Objetivo do Projeto

A empresa necessita informatizar o setor de vendas para:

- Controlar **clientes, produtos, pedidos e vendedores**
- Gerenciar **comissões variáveis por pedido**
- Organizar vendas por **regiões personalizadas**
- Garantir que cada região seja atendida por **apenas um vendedor**
- Gerar **relatórios gerenciais consolidados** para apoio à tomada de decisão

---

## Regras de Negócio Implementadas

- Cada **pedido** pode conter **um ou mais produtos**
- A **comissão do vendedor** pode variar de acordo com cada pedido
- A empresa trabalha com **região fechada**, ou seja:
  - Cada região possui **apenas um vendedor responsável**
- O usuário pode **criar e gerenciar suas próprias regiões**
- Um cliente pertence a uma região específica
- As vendas podem ser analisadas por:
  - Região
  - Cliente
  - Vendedor
  - Produto

---

## Principais Relatórios Gerenciais

O sistema permite a geração dos seguintes relatórios:

- ✅ Total vendido por **região**
- ✅ Total vendido por **cliente**
- ✅ Total vendido por **vendedor**
- ✅ Vendedores responsáveis por determinada **região**
- ✅ Clientes de determinada **região**
- ✅ Total vendido por **produto**

Todos os relatórios são baseados em **consultas SQL otimizadas**, utilizando `JOIN`, `GROUP BY`, funções agregadas e integridade referencial.

---

## Tecnologias Utilizadas

### Frontend
- **HTML5** — Estrutura das páginas
- **CSS3 + Tailwind CSS** — Estilização moderna e responsiva
- **JavaScript** — Consumo da API, manipulação do DOM e interações dinâmicas

### Backend
- **Python**
- **FastAPI**
  - Criação de endpoints REST
  - Validação de dados
  - Separação de responsabilidades
  - Documentação automática via Swagger (`/docs`)

### Banco de Dados
- **SQL Server**
- Modelagem relacional normalizada
- Uso de:
  - `PRIMARY KEY`
  - `FOREIGN KEY`
  - Relacionamentos 1:N e N:N
  - Consultas analíticas para relatórios gerenciais


