import pandas as pd
from config import PLANILHA

COLUNAS_OBRIGATORIAS = [
    "Cliente",
    "CPF/CNPJ",
    "CEP",
    "Endereço",
    "Bairro",
    "Municipio",
    "UF",
    "Inscricao Estadual",
    "Descrição",
    "Quantidade",
    "Valor Unitario",
    "Valor Total",
]

def carregar_clientes():
    clientes = pd.read_excel(PLANILHA)

    colunas_ausentes = [
        coluna for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in clientes.columns
    ]

    if colunas_ausentes:
        raise ValueError(f"Colunas ausentes na planilha: {colunas_ausentes}")

    clientes = clientes.dropna(subset=["Cliente", "Endereço", "Valor Total"])

    return clientes