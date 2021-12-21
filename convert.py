import requests

def convert_valute():
    link_rate_now = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    page = requests.get(link_rate_now)
    rate = page.json()
    print("Список валют: USD, UER, RUR, BTC\n")
    valute = input("Введіть будь-ласка потрібну валюту: ")
    sum_to_convert = input("Введіть сумму у валюті, яку треба конвертувати: ")
    if not sum_to_convert.isdigit():
        print("Введіть коретну сумму")
        convert_valute()

    check = False
    print("Ваша сумма: {} {}\n".format(sum_to_convert, valute))
    for i in rate:
        if i['ccy'] == valute:
            print("Продаж: " + str(i['sale']))
            res = float(i['sale']) * int(sum_to_convert)
            print(str(int(res)) + " uah при купівлі валюти\n")

            print("Купівля: " + str(i['buy']))
            res = float(i['buy']) * int(sum_to_convert)
            print(str(int(res)) + " uah при продажу валюти")
            check = True

    if check is not True:
        print("Нажаль такої валюти немає")
        return

