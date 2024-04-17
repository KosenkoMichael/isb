import sys

sys.path.append("algoritms")


from algoritms.asymmetric_cipher import (
    asymmetric_key_generation,
    asymmetric_encryption,
    asymmetric_decryption,
)
from algoritms.symmetric_cipher import (
    symmetric_key_generation,
    symmetric_encryption,
    symmetric_decryption,
)
from algoritms.serialization import (
    symmetric_key_serialization,
    private_key_serialization,
    public_key_serialization,
)
from algoritms.functional import read_json


def main():
    settings = read_json("settings.json")

    # Symmetric key generation and serialization
    symmetric_key = symmetric_key_generation(32)
    symmetric_key_serialization(settings["symmetric_key"], symmetric_key)

    # Asymmetric key generation and serialization
    public_key, private_key = asymmetric_key_generation()
    public_key_serialization(settings["public_key"], public_key)
    private_key_serialization(settings["private_key"], private_key)

    # Text encryption
    encrypted_text = symmetric_encryption(
        settings["initial_file"],
        settings["symmetric_key"],
        settings["nonce"],
        settings["encrypted_file"],
    )
    # print(f"Encrypted text: {encrypted_text}")

    # Text decryption
    decrypted_text = symmetric_decryption(
        settings["symmetric_key"],
        settings["nonce"],
        settings["encrypted_file"],
        settings["decrypted_file"],
    )
    # print(f"Decrypted text: {decrypted_text}")

    # Symmetric key encryption
    asymmetric_encryption(
        settings["public_key"],
        settings["symmetric_key"],
        settings["encrypted_symmetric_key"],
    )

    # Symmetric key decryption
    asymmetric_decryption(
        settings["private_key"],
        settings["encrypted_symmetric_key"],
        settings["decrypted_symmetric_key"],
    )


if __name__ == "__main__":
    main()
