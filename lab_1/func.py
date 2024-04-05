import operator
import json
import sys
import argparse
import os


def write_txt(file_path: str, data: str) -> None:
    """function, which can write data to .txt file

    Args:
        file_path (str): path to file, which we need to fill
        data (str): what we need to write in file
    """
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            file.write(data)
    except Exception as e:
        print("Произошла ошибка:", e)


def read_json(file_path: str) -> dict[str:str]:
    """function, which can get dict from .json file

    Returns:
        dict[str:str]: dictionary with pare (key - value)
    """
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except Exception as e:
        print("Произошла ошибка:", e)


def write_json(file_path: str, key: dict) -> None:
    """function, which can write data to .json file

    Args:
        file_path (str): path to file, which we need to fill
        key (dict): what we need to write in file
    """
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump(key, file)
    except Exception as e:
        print("Произошла ошибка:", e)


def read_txt(file_path: str) -> str:
    """function, which can read data from .txt file

    Args:
        file_path (str): path to file with data

    Returns:
        str: what the file contains
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read().replace("\n", " \n")
    except Exception as e:
        print("Произошла ошибка:", e)


def text_process(text: str, key: dict) -> str:
    """function, which can decipher the text by key

    Args:
        text (str): text, we need to process
        key (dict): key for the cipher

    Returns:
        str: result text
    """
    result = ""
    for i in text:
        if (i in key) and (len(key[i])):
            result += key[i]
        else:
            result += i
    return result


def get_freq(text: str) -> dict:
    """function, which can calculate frequency in text

    Args:
        text (str): text, which we need to process

    Returns:
        dict: dictionary with frequency dor current text
    """
    return dict(sorted({i: text.count(i)/len(text) for i in set(text)}.items(), key=operator.itemgetter(1), reverse=True))


def key_update(dict_key: dict, key: str, val: str) -> None:
    """function, which can update current key for decipher

    Args:
        dict_key (dict): old key-dict
        key (str): new key
        val (str): new value
    """
    if key in dict_key:
        dict_key[key] = val


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='text cipher',
        description='cipher the text by the key')
    parser.add_argument('dir', type=str, help="dirrectory with files")
    parser.add_argument('key', type=str, help=".json file with key")
    parser.add_argument('original_file', type=str,
                        help=".txt file with ciphered text")
    parser.add_argument('result_file', type=str,
                        help=".txt file with UNciphered text")
    args = parser.parse_args()
    write_txt(os.path.join(args.dir, args.result_file), text_process(
        read_txt(os.path.join(args.dir, args.original_file)), read_json(os.path.join(args.dir, args.key))))


if __name__ == '__main__':
    main()
