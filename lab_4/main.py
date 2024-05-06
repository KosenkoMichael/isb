import hashlib
import time

import multiprocessing as mp

import CONST


cores = mp.cpu_count()


tinkoff_credit_mastercard_bins = CONST.TINKOFF_CREDIT_MASTERCARD_BINS
last_4_digits = CONST.LAST_4_DIGITS
card_num_hash = CONST.CARD_NUM_HASH
path_to_result = CONST.PATH_TO_RESULT


def search(bin, mid, num_end, hash):
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


def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


def luna_check(card_num):
    s = sum(
        sum_of_digits(int(d) * 2) if not i % 2 else int(d)
        for i, d in enumerate(str(card_num)[-2::-1])
    )
    control_num = 10 - (s % 10) % 10
    return control_num == card_num % 10


if __name__ == "__main__":

    def card_num_bruteforce():
        start_time = time.time()
        with mp.Pool(processes=cores) as p:
            for result in p.starmap(
                search,
                [
                    (val1, val2, last_4_digits, card_num_hash)
                    for val1 in tinkoff_credit_mastercard_bins
                    for val2 in range(0, 1000000)
                ],
            ):
                if result:
                    print(f"we have found {result} and have terminated pool")
                    write_file(path_to_result, str(result))
                    print(luna_check(result))
                    p.terminate()
                    break
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения кода: {execution_time} секунд")

    card_num_bruteforce()
