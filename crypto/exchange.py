from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.dh import DHParameterNumbers
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key

p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 2

class Exchange:
    def __init__(self):
        params_numbers = DHParameterNumbers(p,g)
        parameters = params_numbers.parameters(default_backend())
        self.priv_key =  parameters.generate_private_key()
        self.pub_key = self.priv_key.public_key()

    def prepare_pub(self):
        return self.pub_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

    def calc_shared(self, key):
        return self.priv_key.exchange(key)

    @staticmethod
    def transform_pub(pub_key):
        return load_der_public_key(pub_key, default_backend())

if __name__ == "__main__":
    a = Exchange()
    b = Exchange()

    a_shared = a.calc_shared(b.pub_key)
    b_shared = b.calc_shared(a.pub_key)

    print(a_shared)
    print(b_shared)

    if a_shared == b_shared:
        print("shared-keys are identical!")
    else:
        print("shared-keys are not identical, something went wrong!")