from pathlib import Path

file_path = Path("data.txt")

def check_if_already_sent(whole_message):
    if not file_path.exists():
        file_path.touch()
    url = whole_message.split("\n")[0]
    with open("data.txt", "r+") as f:
        file = f.read()
        if url in file:
            return True
        return False


def write_to_file(whole_message):
    url = whole_message.split("\n")[0]
    with open("data.txt", "a") as file:
        file.write(f"{url}\n")


def create_text(olx_link, text, xata_price, xata_date):
    return f"{olx_link}\n{text}\n\n{xata_price}\n\n{xata_date}"