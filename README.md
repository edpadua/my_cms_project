# my_cms_project

# 🚀 CMS Profissional com Django

> Um Sistema de Gerenciamento de Conteúdo (CMS) completo, construído para demonstrar proficiência em Django, CRUD, segurança e arquitetura MVT.

## 🌟 Recursos Principais

* **CRUD Completo:** Criação, Visualização, Edição e Exclusão de posts via interface front-end.
* **Controle de Acesso:** Uso de `LoginRequiredMixin` e `UserPassesTestMixin` para garantir que apenas o autor possa editar seu próprio conteúdo.
* **Estilização Profissional:** Design responsivo implementado com Bootstrap 5.
* **Templates Customizados:** Sobrescrita de templates do Admin para personalização de cores.
* **URLs Amigáveis:** Uso de `slugs` para URLs limpas e otimizadas para SEO.

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Back-end** | **Python** | Linguagem principal de desenvolvimento. |
| **Framework** | **Django (MVC/MVT)** | Estrutura para desenvolvimento de aplicações web. |
| **Banco de Dados** | **SQLite3** | Banco de dados padrão para desenvolvimento (pode ser trocado por PostgreSQL em produção). |
| **Estilização** | **Bootstrap 5** | Framework CSS para responsividade e design. |
| **Utilitário** | `django-widget-tweaks` | Para estilizar formulários de forma eficiente. |

## 🌟 Recursos Principais

* **CRUD Completo:** Criação, Visualização, Edição e Exclusão de posts via interface front-end.
* **Controle de Acesso:** Uso de `LoginRequiredMixin` e `UserPassesTestMixin` para garantir que apenas o autor possa editar seu próprio conteúdo.
* **Estilização Profissional:** Design responsivo implementado com Bootstrap 5.
* **Templates Customizados:** Sobrescrita de templates do Admin para personalização de cores.
* **URLs Amigáveis:** Uso de `slugs` para URLs limpas e otimizadas para SEO.

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Back-end** | **Python** | Linguagem principal de desenvolvimento. |
| **Framework** | **Django (MVC/MVT)** | Estrutura para desenvolvimento de aplicações web. |
| **Banco de Dados** | **SQLite3** | Banco de dados padrão para desenvolvimento (pode ser trocado por PostgreSQL em produção). |
| **Estilização** | **Bootstrap 5** | Framework CSS para responsividade e design. |
| **Utilitário** | `django-widget-tweaks` | Para estilizar formulários de forma eficiente. |

## 📁 Estrutura de Pastas

my_cms_project/ ├── my_cms_project/ # Configurações globais ├── posts/ # O aplicativo principal (Models, Views, URLs, Forms) │ ├── models.py # Modelagem de Post e Category │ ├── views.py # Views baseadas em classes (ListView, DetailView, etc.) │ ├── urls.py # Mapeamento de rotas do app │ └── templates/ # HTMLs customizados ├── templates/ # Templates Globais (base.html, admin/base.html) └── static/ # CSS Customizado (styles.css, admin/css/custom_admin.css)


## ⚙️ Instalação e Execução

Instruções claras são essenciais para que qualquer recrutador ou colega possa rodar seu projeto.

### Pré-requisitos

* Python 3.8+
* pip

### Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [https://www.youtube.com/watch?v=X49Wz3icO3E](https://www.youtube.com/watch?v=X49Wz3icO3E)
    cd django-cms-portfolio
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```

3.  **Instale as Dependências:** (Primeiro, crie o arquivo `requirements.txt` com `pip freeze > requirements.txt`)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crie a Estrutura do Banco de Dados e Superusuário:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5.  **Execute o Servidor:**
    ```bash
    python manage.py runserver
    ```

O projeto estará acessível em `http://127.0.0.1:8000/`.
