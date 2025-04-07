import requests
from bs4 import BeautifulSoup

from utils import check_if_already_sent

url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kremenchug/q-оренда-квартири/?currency=UAH&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=dvuhkomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B1%5D=trehkomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B2%5D=chetyrehkomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B3%5D=pyatikomnatnye&search%5Border%5D=created_at%3Adesc'
def parse():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []

        target_divs = soup.find_all('div', class_='css-l9drzq')

        for div in target_divs:
            inner_divs = div.find_all('div', class_='css-1apmciz')
            for inner_div in inner_divs:
                link = inner_div.find("a", class_='css-1tqlkj0', href=True)
                if check_if_already_sent(link["href"]):
                    continue
                xata_data = {}
                xata_data["link"] = f"https://www.olx.ua{link["href"]}"
                xata_data["text"] = link.get_text()

                price = inner_div.find("p", class_='css-uj7mm0')
                xata_data["price"] = price.get_text()
                date = inner_div.find("p", class_='css-vbz67q')
                xata_data["date"] = date.get_text()
                data.append(xata_data)
        return data
    else:
        return f"Failed to retrieve page. Status code: {response.status_code}"
