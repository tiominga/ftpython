################################################################
#Rename this file to ftp.py after add the correct data
################################################################

from ftplib import FTP

# Configurações de conexão FTP
ftp_host = 'ftp.example.com'
ftp_user = 'seu_usuario'
ftp_password = 'sua_senha'

# Cria uma instância do objeto FTP
ftp = FTP()

# Conecta ao servidor FTP
ftp.connect(ftp_host)

# Faz login com as credenciais
ftp.login(user=ftp_user, passwd=ftp_password)

# Lista os arquivos no diretório remoto
lista_arquivos = ftp.nlst()

# Exibe os arquivos
print("Arquivos no diretório remoto:")
for arquivo in lista_arquivos:
    print(arquivo)

# Fecha a conexão FTP
ftp.quit()
