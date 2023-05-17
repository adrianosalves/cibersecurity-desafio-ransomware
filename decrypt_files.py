from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path[:-10]  # Remove a extensão ".encrypted"
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"Arquivo descriptografado: {decrypted_file_path}")

def decrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".encrypted"):
                decrypt_file(file_path, key)

# Exemplo de uso
key = b'6NAupfi_RZ-sBx-9e8qEsZgS5SzQnhcGP07mBvz-Uzk='  # Insira sua chave manual como uma sequência de bytes
directory = "c:/decrypt/cripto/."

# Descriptografa todos os arquivos criptografados no diretório
decrypt_files_in_directory(directory, key)
