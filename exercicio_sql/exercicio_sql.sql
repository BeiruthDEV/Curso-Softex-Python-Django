CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);


CREATE TABLE Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
);

CREATE TABLE Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra DATETIME DEFAULT CURRENT_TIMESTAMP,
    total REAL,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

CREATE TABLE Itens_Pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id)
);

INSERT INTO Clientes (nome, email) VALUES 
('João', 'joao@email.com'),
('Maria', 'maria@email.com'),
('Ana', 'ana@email.com');

INSERT INTO Produtos (nome, preco, estoque) VALUES 
('Teclado', 150.00, 50),
('Mouse', 80.00, 100),
('Monitor', 900.00, 10);

INSERT INTO Pedidos (id_cliente, total) VALUES (2, 310.00); 

INSERT INTO Itens_Pedido (id_pedido, id_produto, quantidade) VALUES 
(1, 1, 1),
(1, 2, 2);

SELECT * FROM Produtos WHERE preco > 100;

SELECT 
    c.nome, 
    p.id, 
    p.data_compra
FROM Pedidos p
JOIN Clientes c ON p.id_cliente = c.id
WHERE c.nome = 'Maria';

UPDATE Produtos SET preco = preco * 1.10 WHERE nome = 'Mouse';

UPDATE Produtos SET estoque = estoque - 2 WHERE nome = 'Mouse';

DELETE FROM Clientes WHERE nome = 'João';

DELETE FROM Itens_Pedido WHERE id_pedido = 1 AND id_produto = 1;