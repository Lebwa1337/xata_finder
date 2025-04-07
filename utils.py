def check_if_already_sent(url):
    with open("data.txt", "r+") as f:
        file = f.read()
        if url in file:
            return True
        return False


def write_to_file(url):
    with open("data.txt", "a") as file:
        file.write(f"{url}\n")


def create_text(data):
    return f"{data.get('link')}\n{data.get('text')}\n\n{data.get("price")}\n\n{data.get("date")}"