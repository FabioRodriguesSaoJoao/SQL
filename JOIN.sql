SELECT * FROM tabela_de_vendedores;
SELECT * FROM notas_fiscais;

SELECT * FROM tabela_de_vendedores A INNER JOIN notas_fiscais B ON A.MATRICULA = B.MATRICULA;

SELECT A.MATRICULA, A.NOME, COUNT(*) FROM tabela_de_vendedores A INNER JOIN 
notas_fiscais B ON A.MATRICULA = B.MATRICULA GROUP BY A.MATRICULA, A.NOME;

SELECT A.MATRICULA, A.NOME, COUNT(*) FROM tabela_de_vendedores A , notas_fiscais B where
 A.MATRICULA = B.MATRICULA GROUP BY A.MATRICULA, A.NOME;
 
SELECT COUNT(*) FROM tabela_de_clientes;

SELECT CPF, COUNT(*) FROM notas_fiscais group by CPF;

SELECT DISTINCT A.CPF, A.NOME, B.CPF FROM tabela_de_clientes A INNER JOIN notas_fiscais
B ON A.CPF = B.CPF;

SELECT DISTINCT A.CPF, A.NOME, B.CPF FROM tabela_de_clientes A LEFT JOIN notas_fiscais
B ON A.CPF = B.CPF;

SELECT DISTINCT A.CPF, A.NOME, B.CPF FROM tabela_de_clientes A LEFT JOIN notas_fiscais
B ON A.CPF = B.CPF WHERE B.CPF IS NULL;
 
SELECT DISTINCT A.CPF, A.NOME, B.CPF FROM tabela_de_clientes A LEFT JOIN notas_fiscais
B ON A.CPF = B.CPF WHERE B.CPF IS NULL AND YEAR(B.DATA_VENDA) = 2015;

SELECT DISTINCT A.CPF, A.NOME, B.CPF FROM notas_fiscais B right JOIN  tabela_de_clientes
A ON A.CPF = B.CPF WHERE B.CPF IS NULL;


SELECT * FROM tabela_de_vendedores INNER JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
 SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, tabela_de_vendedores.DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores INNER JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
 
 SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores INNER JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
 
 SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, tabela_de_vendedores.DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores LEFT JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
 
  SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, tabela_de_vendedores.DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores right JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, tabela_de_vendedores.DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores FULL JOIN tabela_de_clientes ON
 tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
 
SELECT tabela_de_vendedores.BAIRRO, tabela_de_vendedores.NOME, tabela_de_vendedores.DE_FERIAS,
 tabela_de_clientes.BAIRRO, tabela_de_clientes.NOME
 FROM tabela_de_vendedores, tabela_de_clientes;
 
 
 
 