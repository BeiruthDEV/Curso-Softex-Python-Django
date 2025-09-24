class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
            return
        print("Acervo da Biblioteca:")
        for livro in self.acervo:
            print(f"- {livro.titulo}, de {livro.autor}")


if __name__ == "__main__":

    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")
    livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

    biblioteca = Biblioteca()

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    print("\nListando livros da biblioteca:")
    biblioteca.listar_livros()
