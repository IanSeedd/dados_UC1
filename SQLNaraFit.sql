CREATE DATABASE Narafit;

USE Narafit;

CREATE TABLE alunos (
aluno VARCHAR(50),
idade INT,
estado VARCHAR(50),
peso DECIMAL(5, 2)); -- o número de digitos leva em conta os decimais, por isso 5

INSERT INTO alunos (aluno, idade, estado, peso)
VALUES ('Matikanetanhauser', 19, 'Tokyo', 67.70),
		('Oguri Cap', 19, 'Osaka', 75.90),
        ('Bungas', 900, 'Bungas City', 900),
        ('Agnes Tachyon', 20, 'Tokyo', 70),
        ('All for One', 67, 'Shibuya', 80),
        ('Toshinori', 50, 'Tokyo', 55);
        
SELECT * FROM alunos;

SELECT aluno, idade, estado, peso
FROM alunos
WHERE idade > 40;