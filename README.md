# 💻 Projeto Portfólio Fullstack com Flask

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos em desenvolvimento backend utilizando Flask, integrando um frontend simples em HTML/CSS com persistência de dados em banco.

A aplicação simula um cenário real de contato profissional, onde um usuário pode enviar uma mensagem através de um formulário e os dados são processados e armazenados no banco de dados.

  
Para acessar o site hospedado entre [Aqui](https://portifolio-flask-w80v.onrender.com/).

---

## 🎯 Objetivo

Criar uma aplicação web completa, aplicando conceitos fundamentais de desenvolvimento backend:

* Estruturação de projeto com Flask
* Criação de rotas e Blueprints
* Integração com banco de dados (SQLAlchemy)
* Processamento de formulários
* Persistência de dados
* Boas práticas de organização de código

---

## 🧱 Arquitetura do Projeto

O projeto segue uma estrutura modular inspirada em aplicações reais:

```
Site_html_flask/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── contact.py
│   ├── routes/
│   │   ├── main_routes.py
│   │   └── contact_routes.py
│   ├── database/
│   │   └── db.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── project.html
│   │   └── contact.html
│   └── static/
│       ├── css/
│       └── img/
│
├── config.py
├── run.py
└── database.db
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3

---

## 🔄 Fluxo da Aplicação

1. Usuário acessa a página de contato
2. Preenche o formulário
3. Dados são enviados via método POST
4. Backend processa as informações
5. Dados são salvos no banco
6. Usuário é redirecionado para a página inicial
7. Mensagem de sucesso é exibida

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acessar a pasta

```
cd Site_html_flask
```

### 3. Criar ambiente virtual

```
python -m venv venv
```

### 4. Ativar ambiente

Windows:

```
venv\Scripts\activate
```

### 5. Instalar dependências

```
pip install flask flask_sqlalchemy
```

### 6. Executar aplicação

```
python run.py
```

### 7. Acessar no navegador

```
http://127.0.0.1:5000
```

---

## 🧪 Funcionalidades Implementadas

✔ Página inicial (Home)  
✔ Página de projetos  
✔ Formulário de contato  
✔ Integração com backend Flask  
✔ Persistência de dados em banco SQLite  
✔ Feedback ao usuário (mensagem de sucesso)  
✔ Redirecionamento após envio  

---

## 🚧 Roadmap (Evolução do Projeto)

* [ ] Envio automático de e-mail
* [ ] Painel administrativo para visualizar contatos


---

## 🌐 Deploy

(Em andamento)

---

## 👨‍💻 Autor

Bruno Santos

* GitHub: https://github.com/bruunovsanttos
* LinkedIn: https://www.linkedin.com/in/brunovieirasantos/

---

## 📌 Considerações Finais

Este projeto faz parte da minha transição de carreira para a área de desenvolvimento backend, onde venho aplicando na prática conceitos fundamentais de construção de aplicações web.

O foco está na evolução contínua, implementando melhorias progressivas que aproximam o projeto de um cenário real de produção.
