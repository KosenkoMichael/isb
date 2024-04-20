import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from serialization import symmetric_key_deserialization, symmetric_key_serialization
from functional import read_file, read_file_bytes, write_file, write_file_bytes


def symmetric_key_generation(bytes_num: int) -> bytes:
    """generate symmetric key

    Args:
        bytes_num (int):key_len

    Returns:
        bytes: symmetric key
    """
    return os.urandom(bytes_num)


def symmetric_encryption(
    text_file_path: str,
    path_to_symmetric: str,
    path_to_nonce: str,
    encrypted_text_file_path: str,
) -> bytes:
    """encryption by symmetric key

    Args:
        text_file_path (str): path to origin text
        path_to_symmetric (str): path to symmetric key
        path_to_nonce (str): path to nonce for ChaCha20
        encrypted_text_file_path (str): file path for encrypted text

    Returns:
        str: encrypted text
    """
    nonce = symmetric_key_generation(16)
    symmetric_key_serialization(path_to_nonce, nonce)
    origin_text = read_file(text_file_path)
    symmetric_key = symmetric_key_deserialization(path_to_symmetric)
    cipher = Cipher(
        algorithms.ChaCha20(symmetric_key, nonce), None, backend=default_backend()
    )
    padder = padding.PKCS7(256).padder()
    text_to_bytes = bytes(origin_text, "UTF-8")
    padded_text = padder.update(text_to_bytes) + padder.finalize()
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
    write_file_bytes(encrypted_text_file_path, encrypted_text)
    return encrypted_text


def symmetric_decryption(
    path_to_symmetric: str,
    path_to_nonce: str,
    path_to_encrypted_text: str,
    path_to_decrypted_text: str,
) -> str:
    """decryption by symmetric key

    Args:
        path_to_symmetric (str): path to key
        path_to_nonce (str): path to nonce for ChaCha20
        path_to_encrypted_text (str): path to ebcrypted file
        path_to_decrypted_text (str): path to decrypted file

    Returns:
        str: decrypted text
    """
    nonce = read_file_bytes(path_to_nonce)
    encrypted_text = read_file_bytes(path_to_encrypted_text)
    symmetric_key = symmetric_key_deserialization(path_to_symmetric)
    cipher = Cipher(
        algorithms.ChaCha20(symmetric_key, nonce), mode=None, backend=default_backend()
    )
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = padding.PKCS7(256).unpadder()
    unpadded_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()
    dec_unpad_text = unpadded_dc_text.decode("UTF-8")
    write_file(path_to_decrypted_text, dec_unpad_text)
    return dec_unpad_text
