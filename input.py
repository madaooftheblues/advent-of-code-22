from sys import exit, argv
from pathlib import Path


def open_file(path: str | Path):
    try:
        file = open(path)
        return file

    except FileNotFoundError:
        print(f'Error: File at path "{path}" not found')
        exit(1)

    except Exception as e:
        print(f"Exception: {e}")


def open_argv():
    if len(argv) < 2:
        print("Error: No commandline arguments passed")
        exit(1)
    path = Path(argv[1])
    return open_file(path)


def read_argv():
    file = open_argv()
    assert file is not None
    read = file.read()
    file.close()
    return read


def gen_line():
    file = open_argv()
    assert file is not None
    while True:
        line = file.readline()
        if not line:
            break
        yield line
    file.close()
