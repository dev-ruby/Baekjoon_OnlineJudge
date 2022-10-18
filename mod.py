import clipboard
import datetime
import os
import requests
import subprocess
from bs4 import BeautifulSoup
from typing import List, Tuple, Union

CODE_PRESET = """# {0} - {1}\n# {2}-{3}-{4}\n\n\nimport sys\n\n\ndef input() -> str:\n    return sys.stdin.readline().rstrip()\n\n\ndef solve():\n    pass\n\n\nsolve()\n"""
PATH = r"problems\{0}.py"


class ServerConnectionError(Exception):
    def __init__(self):
        super().__init__("백준 서버에 연결할 수 없습니다.")


def clear_terminal() -> None:
    os.system("cls")


def read_file(path: str) -> List[str]:
    with open(path, mode="r", encoding="utf-8") as file:
        context = file.readlines()
    return context


def print_bar() -> None:
    print("===================")


def print_lines(number: int) -> None:
    print("\n" * number, end="")


def initialize_prompt(title: str) -> None:
    clear_terminal()
    print(title)
    print_bar()
    print_lines(2)


def wait_for_any_key() -> None:
    input("Enter eny key to continue")


def get_problem_page(id: int) -> requests.Response:
    problem_url = f"https://www.acmicpc.net/problem/{id}"
    response = requests.get(problem_url)
    return response


def check_response(response: requests.Response) -> None:
    is_connection_ok = response.status_code == 200

    if not is_connection_ok:
        raise ServerConnectionError


def parse_problem_page(response: requests.Response) -> str:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("#problem_title").text
    return title


def get_problem_title(id: str) -> str:
    response = get_problem_page(id)
    check_response(response)
    title = parse_problem_page(response)

    return title


def get_year_month_day() -> Tuple[str, str, str]:
    now = datetime.datetime.now()
    return (str(now.year), str(now.month), str(now.day))


def create_code_file(id: str, title: str, path: str) -> None:
    year, month, day = get_year_month_day()
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(CODE_PRESET.format(id, title, year, month, day))


def get_problem_title_from_file(path: str) -> str:
    context = read_file(path)
    return context[0][2:]


def run_code(path: str) -> Union[None, str]:
    print_lines(2)
    print_bar()
    print_lines(2)

    try:
        subprocess.call(path, shell=True)
    except Exception as exception:
        return str(exception)

    print_lines(2)
    print_bar()


def commit_code(path: str, title: str) -> None:
    os.system(f"black {path}")
    os.system(f"git add {path}")
    os.system(f'git commit -m "{title}" ')


def main():
    clear_terminal()
    problem_id = input(" >>> ")
    problem_code_path = PATH.format(problem_id)

    if not os.path.exists(problem_code_path):
        try:
            problem_title = get_problem_title(problem_id)
        except ServerConnectionError:
            print("백준 서버에 연결할 수 없습니다.")
            return
        create_code_file(problem_id, problem_title, problem_code_path)

    problem_title = get_problem_title_from_file(problem_code_path)

    while True:
        initialize_prompt(problem_title)
        command = input(" >>> ")

        if command == "exit":
            return

        elif command == "test":
            run_error = run_code(problem_code_path)
            if run_error is not None:
                print(run_error)
            wait_for_any_key()

        elif command == "commit":
            commit_code(problem_code_path, problem_title)
            wait_for_any_key()

        elif command == "copy":
            context = "".join(read_file(problem_code_path))
            clipboard.copy(context)
            print("copied!")
            wait_for_any_key()


if __name__ == "__main__":
    while True:
        main()
