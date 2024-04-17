import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from algoritms.serialization import symmetric_key_deserialization
from algoritms.functional import read_file, write_file