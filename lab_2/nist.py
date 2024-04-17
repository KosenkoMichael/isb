import json
import math
import mpmath

from constants import PI


def read_data(file_path: str) -> dict[str, str]:
    """function which can read data from json file

    Args:
        file_path (str): path to .json file

    Returns:
        dict[str, str]: data from file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Error:", e)


def frequency_bit(sequence: str) -> float:
    """frequency bit test

    Args:
        sequence (str): random sequence

    Returns:
        float: P-value
    """
    try:
        if len(sequence):
            sum = 0
            for bit in sequence:
                if bit == "1":
                    sum -= 1
                else:
                    sum += 1
        else:
            return None
        S = math.fabs(sum / (len(sequence) ** 0.5))
        return math.erfc(S / (2**0.5))
    except Exception as e:
        print("Error:", e)


def identical_consecutive_bits(sequence: str) -> float:
    """identical consecutive bits test

    Args:
        sequence (str): random sequence

    Returns:
        float: P-value
    """
    try:
        if len(sequence):
            one_freq = sequence.count("1") / len(sequence)
            if abs(one_freq - 0.5) < (2 / (len(sequence) ** 0.5)):
                V_n = 0
                for i in range(len(sequence) - 1):
                    if sequence[i] != sequence[i + 1]:
                        V_n += 1
                return math.erfc(
                    abs(V_n - 2 * len(sequence) * one_freq * (1 - one_freq))
                    / (2 * (2 * len(sequence)) ** 0.5 * one_freq * (1 - one_freq))
                )
            else:
                return 0
        else:
            return 0
    except Exception as e:
        print("Error:", e)


def longest_sequence_of_ones_in_block(sequence: str) -> float:
    """longest sequence of ones in block

    Args:
        sequence (str): random sequence

    Returns:
       float: P-value
    """
    try:
        block_max_len = {}
        length = len(sequence)
        for step in range(0, length, 8):
            block = sequence[step: step + 8]
            block_length = longest_sequence(block, "1")
            if block_length not in block_max_len:
                block_max_len[block_length] = 1
            else:
                block_max_len[block_length] += 1
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for i in block_max_len:
            if i <= 1:
                v[1] += block_max_len[i]
            elif i == 2:
                v[2] += block_max_len[i]
            elif i == 3:
                v[3] += block_max_len[i]
            else:
                v[4] += block_max_len[i]
        xi_square = 0
        for i in range(4):
            xi_square += ((v[i + 1] - 16 * PI[i + 1]) ** 2) / (16 * PI[i + 1])
        return mpmath.gammainc(3 / 2, xi_square / 2)
    except Exception as e:
        print("Error:", e)


def longest_sequence(sequence: str, elem: str) -> int:
    """function which count the longest sequence of elem in sequense

    Args:
        sequence (str): sequence to process
        elem (str): count-elem

    Returns:
        int: count of elem in sequence
    """
    try:
        max = 0
        count = 0
        for i in range(len(sequence)):
            if sequence[i] == elem:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0
        return max
    except Exception as e:
        print("Error:", e)
