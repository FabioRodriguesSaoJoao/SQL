import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect("bancoDados.db")


# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
cursor.execute(sql_query)

# # Visualiza o resultado
# print(cursor.fetchall())

# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(nomes_colunas)

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(dados)

# ## **Aplicando Linguagem SQL Direto no Banco de Dados com Linguagem Python**

# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa' #??AVG para calcular media 

# Executa a query no banco de dados
cursor.execute(query2)

# Visualiza o resultado
print(cursor.fetchall())

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto' #GROUP BY agrupar, a coluna que nao esta com a função avg vai para o GROUP BY

# Executa a query no banco de dados
cursor.execute(query3)


# Visualiza o resultado
print(cursor.fetchall())

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto"""# where para filtrar e depois vc passa a coluna e por ultimo o parametro

# Executa a query no banco de dados
cursor.execute(query4)

# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.
# Esta query está ERRADA!
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 and AVG(Unidades_Vendidas) > 10
            GROUP BY Nome_Produto """

# Executa a query no banco de dados
cursor.execute(query5)

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10""" # vc nao pode usar where depois o AVG, temos que usar o where pra filtrar, depois o group by , para ai sim usar o AVG obrigatoriamente com o Having



# Executa a query no banco de dados
cursor.execute(query5)

# Visualiza o resultado
print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# ##!! Aplicando Linguagem SQL na Sintaxe do Pandas com Linguagem Python

# Conecta no banco de dados
con = sqlite3.connect("bancoDados.db")

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# > A query abaixo retorna todas as linhas e todas as colunas da tabela.
# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query)

# Retorna os dados da execução da query
dados = cursor.fetchall()

print(dados)

# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())

# # Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# # A query abaixo retorna a média de unidades vendidas.

# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()

print(type(media_unidades_vendidas))

print(media_unidades_vendidas)

# A query abaixo retorna a média de unidades vendidas por produto.

# !!Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()# a coluna Nome_produto é a que eu quero agrupar, e a coluna 'Unidades_Vendidas' vamos usar para calcular a media

# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))

# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean())            # começamos com [df['Valor_Unitario'] > 199] para fazer o fatiamento ,depois fazemos o agrupamento e tiramos a media

# # # ??A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# # Alternativa A
print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10) )      # [df['Valor_Unitario'] > 199] para fatiamento, groupby('Nome_Produto') agrupamento pelo nome_produto,filter(lambda x: x['Unidades_Vendidas'].mean() fazemos um filtro e verificamos se a media de unidades_vendidas sao maiores que 10, se for nós retornamos

# Alternativa B
print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean())
# #** usamos a \ para fazer quebra de linhas em python. [df['Valor_Unitario'] > 199] para fatiamento, groupby('Nome_Produto') agrupamento pelo nome_produto,filter(lambda x: x['Unidades_Vendidas'].mean() fazemos um filtro e verificamos se a media de unidades_vendidas sao maiores que 10, se for nós retornamos. Por ultimo trazemos somente o agrupamento entre o Nome_Produto com a media Unidades_Vendidas


# ## !!Sintaxe SQL x Sintaxe Pandas

# # ??As duas instruções abaixo retornam o mesmo resultado!

# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10""" # aqui podemos usar em qlqr SGBD, linguagem mais acessivel.

# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean() # ja esse é uma biblioteca do python, logo nao podemos usar em todos os SGBD. AQUI temos uma melhor performance.