"""
Crie a class BlogModel seguindo o exemplo da UserModel;
BlogModel deve ter os atributos:
 - conn do tipo DatabaseConnection
 - criar a tabela quando instanciado

tabela blogs:
 - id;
 - titulo;
 - conteudo;
 - data_criacao;
 - data_atualizacao;
 - id_user (chave estrangeira referente a tabela usuarios);

Faça um CRUD para:
- criar postagem
- ler todas as postagens
- ler postagens pelo id
- ler postagens pelo id_user
- atualizar postam (pelo id da postagem)
- deletar postagem (pedo id da postagem)

**Consulte o UserModel para se guiar
"""

import sqlite3
from datetime import datetime

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

class BlogModel:
    def __init__(self, db_connection: DatabaseConnection):
        self.conn = db_connection
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            data_atualizacao TEXT NOT NULL,
            id_user INTEGER,
            FOREIGN KEY (id_user) REFERENCES usuarios(id)
        )
        """
        self.conn.execute(query)

    def create_post(self, titulo, conteudo, id_user):
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_atualizacao = data_criacao
        query = """
        INSERT INTO blogs (titulo, conteudo, data_criacao, data_atualizacao, id_user)
        VALUES (?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (titulo, conteudo, data_criacao, data_atualizacao, id_user))

    def read_all_posts(self):
        query = "SELECT * FROM blogs"
        return self.conn.fetchall(query)

    def read_post_by_id(self, post_id):
        query = "SELECT * FROM blogs WHERE id = ?"
        return self.conn.fetchone(query, (post_id,))

    def read_posts_by_user(self, user_id):
        query = "SELECT * FROM blogs WHERE id_user = ?"
        return self.conn.fetchall(query, (user_id,))

    def update_post(self, post_id, titulo=None, conteudo=None):
        data_atualizacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if titulo:
            query = "UPDATE blogs SET titulo = ?, data_atualizacao = ? WHERE id = ?"
            self.conn.execute(query, (titulo, data_atualizacao, post_id))
        if conteudo:
            query = "UPDATE blogs SET conteudo = ?, data_atualizacao = ? WHERE id = ?"
            self.conn.execute(query, (conteudo, data_atualizacao, post_id))

    def delete_post(self, post_id):
        query = "DELETE FROM blogs WHERE id = ?"
        self.conn.execute(query, (post_id,))

if __name__ == "__main__":
    db_connection = DatabaseConnection("blog.db")
    
    blog_model = BlogModel(db_connection)
    
    blog_model.create_post("Meu primeiro post", "Conteúdo do post", 1)
    
    posts = blog_model.read_all_posts()
    print("Todas as postagens:", posts)
    
    post = blog_model.read_post_by_id(1)
    print("Postagem pelo ID:", post)
    
    user_posts = blog_model.read_posts_by_user(1)
    print("Postagens do usuário 1:", user_posts)
    
    blog_model.update_post(1, titulo="Meu primeiro post atualizado", conteudo="Conteúdo do post atualizado")
    
    blog_model.delete_post(1)
    
    posts_after_delete = blog_model.read_all_posts()
    print("Postagens após a exclusão:", posts_after_delete)
