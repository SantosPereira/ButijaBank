CREATE SCHEMA butija_db;

USE butija_db;

CREATE TABLE main (
    nome varchar(150),
    cpf bigint(11),
    saldo double(102,2),
    PRIMARY KEY (cpf)
) CHARACTER SET utf8;

