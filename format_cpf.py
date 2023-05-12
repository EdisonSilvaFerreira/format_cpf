import pandas as pd

def format_cpf(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

# Carrega a planilha do Excel
df = pd.read_excel('Pasta1.xlsx')

# Converte a coluna CPF para string
df['CPF'] = df['CPF'].astype(str)

# Adiciona zeros à esquerda para completar os números faltantes
df['CPF_tratado'] = df['CPF'].apply(lambda x: x.zfill(11))

# Formata os números de CPF com pontos e traço
df['CPF_tratado'] = df['CPF_tratado'].apply(format_cpf)

# Grava a planilha de volta no Excel
df.to_excel('planilha_modificada1.xlsx', index=False)
