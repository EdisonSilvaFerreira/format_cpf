Script de formatação de CPF em uma planilha do Excel
Este script Python tem como objetivo formatar os números de CPF presentes em uma planilha do Excel. Ele utiliza a biblioteca pandas para ler e gravar a planilha, além de aplicar as modificações necessárias nos dados.

Requisitos
Python 3.x
Pandas (instalado via pip install pandas)
Planilha do Excel com a coluna "CPF" a ser formatada

Funcionamento

1. Importação das bibliotecas necessárias:

import pandas as pd

------------------------------------------------------------------------------------------------------------------------------------

2. Definição da função format_cpf(cpf: str):

def format_cpf(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

Esta função recebe um CPF sem formatação como parâmetro e retorna o CPF formatado com pontos e traço.

------------------------------------------------------------------------------------------------------------------------------------


3. Carregamento da planilha do Excel:

df = pd.read_excel('Pasta1.xlsx')

Este trecho carrega a planilha do arquivo 'Pasta1.xlsx' e armazena os dados em um DataFrame do pandas chamado df.

------------------------------------------------------------------------------------------------------------------------------------

4. Conversão da coluna CPF para string:

df['CPF'] = df['CPF'].astype(str)

Neste passo, a coluna "CPF" é convertida para o tipo de dado string, garantindo que a formatação seja aplicada corretamente.

------------------------------------------------------------------------------------------------------------------------------------

5. Adição de zeros à esquerda para completar os números faltantes:

df['CPF_tratado'] = df['CPF'].apply(lambda x: x.zfill(11))

Aqui, é adicionado zeros à esquerda nos números de CPF que possuam menos de 11 dígitos, para que todos tenham o mesmo formato.

------------------------------------------------------------------------------------------------------------------------------------

6. Formatação dos números de CPF com pontos e traço:

df['CPF_tratado'] = df['CPF_tratado'].apply(format_cpf)

Nesta etapa, a função format_cpf é aplicada em cada número de CPF da coluna "CPF_tratado", formatando-os corretamente com pontos e traço.

7. Gravação da planilha modificada em um novo arquivo do Excel:

df.to_excel('planilha_modificada1.xlsx', index=False)

Por fim, o DataFrame atualizado é gravado em um novo arquivo do Excel chamado 'planilha_modificada1.xlsx', sem a inclusão de uma coluna de índices.

------------------------------------------------------------------------------------------------------------------------------------

Utilização

1. Certifique-se de que os requisitos mencionados anteriormente estão satisfeitos.
2. Coloque a planilha do Excel que deseja formatar os CPFs no mesmo diretório do script.
3. Execute o script Python.
4. Um novo arquivo do Excel chamado 'planilha_modificada1.xlsx' será gerado com os CPFs formatados na coluna "CPF_tratado".

Lembre-se de substituir o nome do arquivo de entrada e de saída, conforme necessário, nos trechos pd.read_excel('Pasta1.xlsx') e df.to_excel('planilha_modificada1.xlsx', index=False) respectivamente.

Importante: Este script é fornecido apenas como exemplo e não garante a integridade dos dados. Recom
