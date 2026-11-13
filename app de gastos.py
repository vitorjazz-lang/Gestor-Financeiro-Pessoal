import sqlite3
from datetime import date
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Controle de Gastos Pessoal", layout="wide")


def iniciar_banco():
  conn = sqlite3.connect("financas.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            tipo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descricao TEXT,
            valor REAL NOT NULL
        )
    """)
  conn.commit()
  return conn


conn = iniciar_banco()

st.title("💰 Controle Pessoal de Gastos e Receitas")

# Barra lateral para cadastrar novos lançamentos
with st.sidebar:
  st.subheader("Novo Lançamento")
  tipo = st.selectbox("Tipo de Movimentação", ["Despesa", "Receita"])

  opcoes_categoria = (
      [
          "Alimentação",
          "Moradia",
          "Transporte",
          "Contas Fixas",
          "Lazer",
          "Saúde",
          "Outros",
      ]
      if tipo == "Despesa"
      else ["Salário", "Renda Extra", "Investimentos", "Outros"]
  )

  with st.form("form_transacao", clear_on_submit=True):
    categoria = st.selectbox("Categoria", opcoes_categoria)
    descricao = st.text_input("Descrição (ex: Supermercado, Luz)")
    valor = st.number_input(
        "Valor (R$)", min_value=0.01, step=10.0, format="%.2f"
    )
    data_lancamento = st.date_input("Data", value=date.today())

    if st.form_submit_button("Salvar Lançamento"):
      cursor = conn.cursor()
      cursor.execute(
          "INSERT INTO transacoes (data, tipo, categoria, descricao, valor)"
          " VALUES (?, ?, ?, ?, ?)",
          (
              data_lancamento.strftime("%Y-%m-%d"),
              tipo,
              categoria,
              descricao,
              valor,
          ),
      )
      conn.commit()
      st.success("Registrado com sucesso!")
      st.rerun()

# Carregamento dos dados
df = pd.read_sql_query(
    "SELECT * FROM transacoes ORDER BY data DESC, id DESC", conn
)

if df.empty:
  st.info(
      "Nenhum lançamento cadastrado ainda. Utilize o menu lateral à esquerda"
      " para começar."
  )
else:
  # Cálculo de resumo financeiro
  receitas = df[df["tipo"] == "Receita"]["valor"].sum()
  despesas = df[df["tipo"] == "Despesa"]["valor"].sum()
  saldo = receitas - despesas

  col1, col2, col3 = st.columns(3)
  col1.metric("Total de Receitas", f"R$ {receitas:,.2f}")
  col2.metric("Total de Despesas", f"R$ {despesas:,.2f}")
  col3.metric("Saldo Atual", f"R$ {saldo:,.2f}")

  # Gráficos e Histórico
  col_grafico, col_tabela = st.columns([1, 1.5])

  with col_grafico:
    st.subheader("Despesas por Categoria")
    df_despesas = df[df["tipo"] == "Despesa"]
    if not df_despesas.empty:
      gastos_categoria = df_despesas.groupby("categoria")["valor"].sum()
      st.bar_chart(gastos_categoria)
    else:
      st.write("Sem despesas registradas.")

  with col_tabela:
    st.subheader("Histórico de Lançamentos")
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Opção para excluir um lançamento pelo ID
    with st.expander("Excluir um lançamento"):
      id_excluir = st.number_input(
          "Digite o ID do lançamento", min_value=1, step=1
      )
      if st.button("Confirmar Exclusão"):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transacoes WHERE id = ?", (id_excluir,))
        conn.commit()
        st.rerun()