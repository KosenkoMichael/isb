import json


def read_file(file_path: str, mode: str) -> str:
    """get file data
    Args:
        file_path: path to file
        mode: file open modification
    Returns:
        file data
    """
    try:
        with open(file_path, mode, encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception as error:
        print(error)


def write_file(file_path: str, data: str, mode: str) -> None:
    """write data to file
    Args:
        file_path: path to file
        data: data we need to write
        mode: file open modification
    """
    try:
        with open(file_path, mode, encoding="utf-8") as file:
            file.write(data)
    except Exception as error:
        print(error)


def read_json(path: str) -> dict:
    """get data from json file
    Args:
        path: path to json file
    Returns:
        file data
    """
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)
