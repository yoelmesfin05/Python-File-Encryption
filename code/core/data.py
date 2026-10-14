"""File input/output helpers for the File Encryption Tool.

Handles saving and loading the encryption key, and reading and writing
the bytes of the file being encrypted or decrypted.
"""


def save_key_to_file(key, filename = "secret.key"):     # saves key for future use (decryption)
    """Save the encryption key to a file so it can be used later for decryption.

    Args:
        key: The Fernet key as bytes.
        filename: Path of the key file to write. Defaults to "secret.key".
    """
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key_from_file(filename = "secret.key"):    # used in the decryption stage to match keys when previously encrypted
    """Load the encryption key from a file.

    Args:
        filename: Path of the key file to read. Defaults to "secret.key".

    Returns:
        The Fernet key as bytes.
    """
    with open(filename, "rb") as key_file:
        key = key_file.read()
    return key

def read_target_file(file_path):
    """Read a file and return its contents as bytes.

    Args:
        file_path: Path of the file to read.

    Returns:
        The raw bytes of the file.
    """
    with open(file_path, "rb") as file:   #action read the file in focus
        file_data = file.read()
    return file_data

def write_target_file(file_path, data):     # action to write about the file in focus
    """Write bytes to a file, replacing its existing contents.

    Args:
        file_path: Path of the file to write.
        data: The bytes to write.
    """
    with open(file_path,"wb") as file:
        file.write(data)