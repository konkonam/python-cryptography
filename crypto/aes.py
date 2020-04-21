from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.backends import default_backend
from hashlib import sha1

class AES:
    def __init__(self, shared):      
        hash = sha1()
        hash.update(shared)
        key_raw = hash.hexdigest()[:32]

        self.key = key_raw.encode()

        iv_raw = hash.hexdigest()[16:32]
        iv = iv_raw.encode()
        mode = CTR(iv)
        self.cipher = Cipher(algorithms.AES(self.key), mode, backend=default_backend())

    def encrypt(self, data):
        encryptor = self.cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()

    def decrypt(self, data):
        decryptor = self.cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()

if __name__ == "__main__":
    aes = AES("dasgepboimtbüp0ifm34pgn534iügon45or423fg345g345gg4ng45".encode())

    encrypted = aes.encrypt(b"Hello World, This is a secured message")
    decrypted = aes.decrypt(encrypted)

    print("-------- Encrypted --------")

    print(encrypted)

    print("-------- Decrypted --------")

    print(decrypted)