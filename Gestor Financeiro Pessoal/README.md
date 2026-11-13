# 💰 Controle Pessoal de Gastos e Receitas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)

**Aplicação web interativa em Python e Streamlit para gestão financeira pessoal, com armazenamento local em SQLite e visualização gráfica de despesas por categoria.**

O **Controle Pessoal de Gastos e Receitas** é um painel financeiro leve e 100% offline projetado para facilitar o acompanhamento do orçamento individual. Com uma interface limpa executada diretamente no navegador, permite registrar entradas e saídas, acompanhar indicadores de saldo em tempo real, analisar a distribuição de gastos por categoria e gerenciar o histórico completo de lançamentos.

---

## 🎯 Objetivos do Projeto

* Oferecer uma interface web intuitiva e responsiva (`Streamlit`) para registro rápido de receitas e despesas.
* Garantir persistência local confiável e sem necessidade de servidores externos utilizando banco de dados relacional **SQLite** (`financas.db`).
* Exibir métricas financeiras consolidadas (Total de Receitas, Total de Despesas e Saldo Atual) e gráficos comparativos por categoria.
* Permitir consulta histórica ordenada e exclusão controlada de registros por ID.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Streamlit** – Framework para construção do dashboard web interativo
* **SQLite3** – Banco de dados relacional embutido para persistência local
* **Pandas** – Consulta SQL, manipulação tabular e agrupamento de dados financeiros

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Passo a passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/controle-gastos-pessoal.git
   cd controle-gastos-pessoal
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor local do Streamlit:**
   ```bash
   streamlit run app.py
   ```
   *(O aplicativo abrirá automaticamente no seu navegador padrão e criará o arquivo `financas.db` na primeira execução).*

---

## 🤝 Contribuição

Contribuições são muito bem-vindas! Ideias como filtros mensais/anuais, gráficos interativos com Plotly ou exportação para Excel podem ser enviadas via *Issue* ou *Pull Request*.
