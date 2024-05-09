import hashlib
import time

from tqdm import tqdm
from matplotlib import pyplot as plt
import multiprocessing as mp

cores = mp.cpu_count()


def search(bin: str, mid: str, num_end: str, hash: str) -> bool:
    """check is the hash of our num == card hash

    Args:
        bin (str): first 6 digits of card number
        mid (str): middle 6 digits of card number
        num_end (str): last 4 digits of card number
        hash (str): hash of card to find collizion

    Returns:
        bool: is hashes equal
    """
    cur_card_number = f"{bin}{str(mid).zfill(6)}{num_end}"
    cur_hash = hashlib.md5(cur_card_number.encode()).hexdigest()
    return int(cur_card_number) if cur_hash == hash else False


def write_file(file_path: str, data: str) -> None:
    """write data to file
    Args:
        file_path: path to file
        data: data we need to write
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as error:
        print(error)


def read_file(file_path: str) -> str:
    """get file data
    Args:
        file_path: path to file
    Returns:
        file data
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception as error:
        print(error)


def sum_of_digits(num: str | int) -> int:
    """digits sum in number

    Args:
        num (str|int): number

    Returns:
        int: sum of digits
    """
    return sum(int(digit) for digit in str(num))


def luna_check(card_num: str | int) -> bool:
    """Luna algorithm

    Args:
        card_num (str | int): card number

    Returns:
        bool: true, if card number can be real
    """
    s = sum(
        sum_of_digits(int(d) * 2) if not i % 2 else int(d)
        for i, d in enumerate(str(card_num)[-2::-1])
    )
    control_num = 10 - (s % 10) % 10
    return control_num == int(card_num) % 10


def card_num_bruteforce(
    last_4_digits: str,
    card_num_hash: str,
    tinkoff_credit_mastercard_bins: list,
    path_to_result: str,
    cores_count: mp.Value = mp.cpu_count(),
) -> tuple:
    """collizions ounf algorithm

    Args:
        bin (str): first 6 digits of card number
        num_end (str): last 4 digits of card number
        hash (str): hash of card to find collizion
        path_to_result (str): path to save real card number
        cores_count (mp.Value, optional): count of processes we want to use. Defaults to mp.cpu_count().

    Returns:
        tuple: _description_
    """
    start_time = time.time()
    with mp.Pool(processes=cores_count) as p:
        for result in p.starmap(
            search,
            [
                (val1, val2, last_4_digits, card_num_hash)
                for val1 in tinkoff_credit_mastercard_bins
                for val2 in range(0, 1000000)
            ],
        ):
            if result:
                write_file(path_to_result, str(result))
                p.terminate()
                end_time = time.time()
                return (end_time - start_time, result)
    return


def search_time_visualization(
    last_4_digits: str,
    card_num_hash: str,
    tinkoff_credit_mastercard_bins: list,
    path_to_result: str,
    path_to_png: str,
) -> None:
    """Vizualization of collizion search process

    Args:
        bin (str): first 6 digits of card number
        num_end (str): last 4 digits of card number
        hash (str): hash of card to find collizion
        path_to_result (str): path to save card number
        path_to_png (str): path to save plot
    """
    results = []
    for cores_count in tqdm(range(1, int(cores * 1.5)), desc="Collizion search"):
        results.append(
            card_num_bruteforce(
                last_4_digits,
                card_num_hash,
                tinkoff_credit_mastercard_bins,
                path_to_result,
                cores_count,
            )[0]
        )
    fig = plt.figure(figsize=(10, 5))
    plt.xlabel("Process count")
    plt.ylabel("Search time")
    plt.plot(
        list(range(1, int(mp.cpu_count() * 1.5))),
        results,
        color="blue",
        linestyle="-",
        marker="o",
        linewidth=2,
        markersize=5,
    )
    plt.savefig(path_to_png)
    plt.show()
