CREATE DATABASE Papelaria; -- Ponto e vírgula boa pratica(além de separar os comandos), mesma coisa de pular linha

USE Papelaria; -- Sempre rode esse comando para escolher o banco que quer usar, é como selecionar o banco

-- Literalmente a mesma coisa do que criar objetos em Django, digite o tipo e o limite
CREATE TABLE vendas ( 
produto VARCHAR(50),
cidade VARCHAR(50),
quantidade INT,
preco_unitario DECIMAL(10,2));

-- Diga quais colunas quer preencher depois digite o que quer que preencha, bem parecido com django
INSERT INTO vendas (produto, cidade, quantidade, preco_unitario)
VALUES ('caderno', 'Rio de Janeiro', 34, 12.50);

-- Adicionar mais dados em um comando só 
INSERT INTO vendas (produto, cidade, quantidade, preco_unitario)
VALUES ('lapis', 'Rio de Janeiro', 10, 2.50),
		('caderno inteligente', 'Rio de Janeiro', 5, 80.80);

SELECT * FROM vendas;

SELECT produto, preco_unitario FROM vendas;

-- Lembrar que o diferente é <> diferente do python 
SELECT produto, quantidade, preco_unitario 
FROM vendas
WHERE quantidade >= 10;

UPDATE vendas SET preco_unitario = 13.00 WHERE produto = 'caderno';

-- O 1 é apenas uma regra no caso ele libera os arquivos locais e o 0 travaria os arquivos locais
SET GLOBAL local_infile = 1;

-- Local do arquivo, e não pode ser \ tem que ser /
LOAD DATA INFILE 'C:/Users/ian.iannacconi/Desktop/vendas_bruto.csv' 
INTO TABLE vendas
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' -- Quebra linha quando preenche tudo
IGNORE 1 ROWS -- Ignora a primeira linha do CSV, o cabeçalho 
(produto, cidade, quantidade, preco_unitario); -- Nome das colunas conforme a tabela criada pelo SQL, ordena os dados na tabela 

-- Separa os valores e retorna todos os que são parecidos, no caso iguais porém escritos diferetes.
SELECT DISTINCT cidade
FROM vendas;

LOAD DATA INFILE 'C:/Users/ian.iannacconi/Documents/tratando_dados/vendas_bruto.csv' 
INTO TABLE vendas
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(produto, cidade, quantidade, preco_unitario); 