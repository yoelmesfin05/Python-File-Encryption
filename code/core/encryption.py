"""Encryption logic for the File Encryption Tool.

Uses Fernet (symmetric encryption) from the cryptography library to
generate keys and to encrypt and decrypt raw file bytes.
"""
import os
from cryptography.fernet import Fernet, InvalidToken

DEFAULT_KEY_FILE = "secret.key"

def generate_key(key_filename: str = DEFAULT_KEY_FILE) -> bytes:
    """Return the project's Fernet key, generating one if it doesn't exist."""
    if os.path.exists(key_filename):
        with open(key_filename, "rb") as f:
            return f.read()
    return Fernet.generate_key()

def encrypt_data(key: bytes, raw_data: bytes) -> bytes:
    """Encrypt the raw bytes of a file with the given Fernet key."""
    return Fernet(key).encrypt(raw_data)

def decrypt_data(key: bytes, encrypted_bytes: bytes) -> bytes:
    """Decrypt Fernet-encrypted bytes."""
    try:
        return Fernet(key).decrypt(encrypted_bytes)
    except InvalidToken as e:
        raise ValueError(
            "Wrong key or corrupted/unauthorized file — cannot decrypt."
        ) from e
