import requests


def rate_today():
    link_rate_now = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    page = requests.get(link_rate_now)
    rate = page.json()
    print("Список валют: USD, UER, RUR, BTC\n")
    valute = input("Введіть будь-ласка потрібну валюту: ")

    check = False
    for i in rate:
        if i['ccy'] == valute:
            print("Купівля: " + str(i['buy']))
            print("Продаж: " + str(i['sale']))
            check = True

    if check is not True:
        print("Нажаль такої валюти немає")
        rate_today()
