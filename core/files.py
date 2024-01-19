import os

class File():

    def list_files(path):

        # Lista os arquivos no caminho especificado
        files = os.listdir(path)

        # Filtra apenas os arquivos, excluindo diretórios
        #arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho, arquivo))]

        return files
