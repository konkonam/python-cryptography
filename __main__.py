from crypto.exchange import Exchange
from crypto.aes import AES

if __name__ == "__main__":
    print("testing cryptography without socket connection:")

    print("setting up server...")
    server = Exchange()

    print("---------- Private-key ----------")
    print(str(server.priv_key))
    
    print("---------- Public-key -----------")
    print(server.prepare_pub())

    print("---------- End of server --------")

    print("setting up client ...")
    client = Exchange()

    print("---------- Private-key ----------")
    print(str(client.priv_key))
    
    print("---------- Public-key -----------")
    print(client.prepare_pub())

    print("---------- End of client --------")

    print("calculating Shared-Keys...")

    print("---------- Shared-Server ---------")
    print(server.calc_shared(client.pub_key))

    print("---------- Shared-Client ---------")
    print(client.calc_shared(server.pub_key))

    print("---------- End of ECDH -----------")
    aes = AES(server.prepare_pub())

    encrypted = aes.encrypt(b"Hello World, This is a secured message")
    decrypted = aes.decrypt(encrypted)

    print("-------- Encrypted --------")

    print(encrypted)

    print("-------- Decrypted --------")

    print(decrypted)
    