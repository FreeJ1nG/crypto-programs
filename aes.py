from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


class AES:
    def __init__(self, key: bytes):
        """
        Initialize AES with a 16, 24, or 32-byte key.
        """
        self.key = key
        print(f"Key: {self.key.hex()}")

    def encrypt(self, plaintext: bytes) -> (bytes, bytes):
        """
        Encrypt plaintext using AES in CBC mode.
        Returns the ciphertext and the IV used for encryption.
        """
        print(f"Plaintext before encryption: {plaintext}")

        iv = os.urandom(16)  # Generate a random 16-byte IV
        print(f"Generated IV: {iv.hex()}")

        cipher = Cipher(algorithms.AES(self.key),
                        modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Pad plaintext to be a multiple of the block size (16 bytes)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()
        print(f"Padded plaintext: {padded_plaintext}")

        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        print(f"Ciphertext: {ciphertext.hex()}")

        return ciphertext, iv

    def decrypt(self, ciphertext: bytes, iv: bytes) -> bytes:
        """
        Decrypt ciphertext using AES in CBC mode.
        Returns the original plaintext.
        """
        print(f"Ciphertext to decrypt: {ciphertext.hex()}")
        print(f"IV used for decryption: {iv.hex()}")

        cipher = Cipher(algorithms.AES(self.key),
                        modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        print(f"Padded plaintext after decryption: {padded_plaintext}")

        # Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext


# Example usage
if __name__ == "__main__":
    key = os.urandom(32)  # Generate a random 32-byte key
    aes = AES(key)

    plaintext = b"Secret message that needs encryption"
    print(f"Original plaintext: {plaintext}")

    ciphertext, iv = aes.encrypt(plaintext)
    print(f"IV: {iv.hex()}")

    decrypted_plaintext = aes.decrypt(ciphertext, iv)
    print(f"Decrypted plaintext: {decrypted_plaintext}")
