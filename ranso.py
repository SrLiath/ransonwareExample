from cryptography.fernet import Fernet
import os

def generate_key():
    Key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_:
        key_.write(Key)
    return Key
    
def load_key():
  return open("encryption.key", "rb").read()

def criptografar(diretorio, key):
    fernet = Fernet(key)
    for root, dirs, files, in os.walk(diretorio):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file:
                data = file.read()
            encrypted = fernet.encrypt(data)
            with open(file_path, "wb") as file:
                file.write(encrypted)
            print(f"{file_path} foi criptografado...")
            
def descriptografar(diretorio, key):
    fernet = Fernet(key)
    for root, dirs, files, in os.walk(diretorio):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file:
                data = file.read()
            encrypted = fernet.decrypt(data)
            with open(file_path, "wb") as file:
                file.write(encrypted)
            print(f"{file_path} foi descriptografado...")
            
if __name__ == "__main__":
    Key = load_key()
    descriptografar('./arquivos/', Key)