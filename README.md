# wsBackend-Fabrica25.2

Workshop da Fábrica de Software - 2025.2

# Simple Blog Django

Um projeto simples em **Django** onde o usuário pode se cadastrar, realizar login e fazer postagens após autenticado. Também possui uma página de notícias utilizando a **NewsAPI**, com opção de abrir uma notícia aleatória.

---

## 🚀 Preparação do Ambiente

### Usando python e venv(opcional)

### 1. Verifique se o Python está instalado

No terminal (PowerShell, CMD ou Bash), execute:

```bash
python --version
```

ou, em alguns sistemas:

```bash
python3 --version
```

Se não aparecer a versão, baixe e instale o Python:
👉 [Download do Python](https://www.python.org/downloads/)

---

### 2. Verifique se o pip está instalado

```bash
pip --version
```

Se não aparecer, instale o pip (no Windows ele geralmente vem junto com o Python).
No Linux/Mac você pode instalar com:

```bash
sudo apt install python3-pip
```

---

### 3. Clone o projeto e entre na pasta

```bash
git clone https://github.com/dante-alves/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2
```

---

### 4. Crie e ative um ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv
```

Ativar o ambiente virtual:

* **Windows (PowerShell):**

```bash
venv\Scripts\Activate
```

* **Linux/Mac:**

```bash
source venv/bin/activate
```

Você verá o prefixo `(venv)` no terminal quando estiver ativo.

---

### 5. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

---

### 6. Gerando o banco de dados

```bash
python manage.py migrate
```

---

### 7. Criando um superuser (admin)

```bash
python manage.py createsuperuser
```

---

### 8. Rodando o projeto

```bash
python manage.py runserver
```

Abra no navegador:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Usando Docker(recomendado)

### 1. Build e subida dos contêineres
```bash
docker-compose up -d --build
```

### 2. Aplicar migrations
```bash
docker-compose exec web python manage.py migrate

```

### 3. Criar superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

### Acessar o projeto no navegador
Abra:
http://localhost:8000

## 📂 Estrutura do Projeto

```
simple-blog-django/
│
├─ myproject/
│  ├─ assets/
│  ├─ media/
│  ├─ myproject/
│  ├─ static/    
│  ├─ templates/  
│  ├─ news/      # applications
│  ├─ posts/      # applications
│  ├─ users/      # applications
├─ venv/
├─ .gitignore
├─ README.md
└─ requirements.txt
```

---

## 📦 requirements.txt

```txt
asgiref==3.9.1
certifi==2025.8.3
charset-normalizer==3.4.3
Django==5.2.5
idna==3.10
pillow==11.3.0
requests==2.32.5
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.5.0
```

---

## 🛠️ Tecnologias

* Python 3.x
* Django
* SQLite (banco padrão do Django)
* NewsAPI para notícias

---

## ✨ Funcionalidades

* Cadastro e login de usuários
* Postagens autenticadas
* Visualização de posts no feed
* Página de notícias do momento
* Encaminhamento para notícias aleatórias

---

## 🔗 APIs utilizadas

* [NewsAPI](https://newsapi.org/) para exibir notícias do momento.

---

## 📄 Licença

Este projeto é de uso livre para estudos e melhorias.

## 😃 Autor

Feito por Dante Alves
