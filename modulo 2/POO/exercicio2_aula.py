class Midia:
    def __init__(self,titulo,duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg


    def exibir(self):
        print(f'O titulo da Midia é {self.titulo}, e a duração é {self.duracao_seg}')



class Musica(Midia):
    def __init__(self, titulo, duracao_seg,artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista


    def exibir(self):
         print(f'O titulo da Música é {self.titulo}, e a duração é {self.duracao_seg}, e o artista é {self.artista}')



class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao



    def exibir(self):
         print(f'O titulo do Vídeo é {self.titulo}, e a duração é {self.duracao_seg}, e a resolução é {self.resolucao}')




if __name__ == "__main__":
    varias_midias = {
        'musicas': [],
        'videos': []
    }

    musica1 = Musica("Apagar", 354, "Ferrugem")
    musica2 = Musica("Talking to the Moon", 183, "Bruno Mars")

    video1 = Video("Curso Python Básico", 1200, "1080p")
    video2 = Video("Curso Java Básico", 900, "720p")

    varias_midias['musicas'].append(musica1)
    varias_midias['musicas'].append(musica2)

    varias_midias['videos'].append(video1)
    varias_midias['videos'].append(video2)

    print(" Músicas:")
    for musica in varias_midias['musicas']:
        musica.exibir()

    print("\n Vídeos:")
    for video in varias_midias['videos']:
        video.exibir()