import requests

def convert_valute():

    link_rate_now = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    page = requests.get(link_rate_now)
    rate = page.json()
    print("Список валют: USD, EUR, RUR, BTC на сьогодні\n")
    valute = input("Введіть будь-ласка валюту, яку потрібно конвертувати: ")
    sum_to_convert = input("Введіть сумму у валюті, яку треба конвертувати: ")
    valute_end = input("Введіть будь-ласка валюту, у яку треба конвертувати: ")
    if not sum_to_convert.isdigit():
        print("Введіть коретну сумму")
        convert_valute()

    check = False
    print("Ваша сумма: {} {}\n".format(sum_to_convert, valute))
    global sum_uah
    for i in rate:
        if i['ccy'] == valute:
            sum_uah = float(i['sale']) * int(sum_to_convert)
            check = True

    if check is not True:
        print("Нажаль такої валюти немає")
        return

    for i in rate:
        if i['ccy'] == valute_end:
            res = sum_uah / float(i['sale'])
            print(sum_to_convert + " " + valute + " = " + str(float(res)) + " " + valute_end)
