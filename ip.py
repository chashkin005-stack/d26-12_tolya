import requests


def get_public_ip():
    services = ["https://api.ipify.org"]

    for service in services:
        try:
            response = requests.get(service, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            continue

    return "Не удалось определить внешний IP"


print(f"Внешний IP: {get_public_ip()}")


def get_ip():
    url = f"http://ip-api.com/json/{get_public_ip()}?lang=ru"
    response = requests.get(url)
    data = response.json()
    return data


def get_inf(get_ip):
    print("Страна:", get_ip["country"])
    print("Регион:", get_ip["regionName"])
    print("Город:", get_ip["city"])
    print("Почтовый индекс:", get_ip["zip"])
    print("Широта:", get_ip["lat"])
    print("Долгота:", get_ip["lon"])


get_inf(get_ip())

