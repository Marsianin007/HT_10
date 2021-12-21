import requests
import datetime

def exit_from_func():
    None

def check_date():
    global date
    date_now = datetime.date.today()
    year_today = int(str(date_now)[0:4])
    month_today = int(str(date_now)[5:7])
    day_today = int(str(date_now)[8:10])
    date = input("Ваша дата у форматі yyyy-mm-dd: ")
    if not date[0:4].isdigit() or not date[5:7].isdigit() or not date[8:10].isdigit():
        print("Невірна дата \n")
        check_date()
    if len(date) > 10:
        print("Невірна дата \n")
        check_date()
    year_start = int(str(date)[0:4])
    month_start = int(str(date)[5:7])
    day_start = int(str(date)[8:10])
    if year_start < year_today - 4:
        print("В цьому році неможливо знайти курс\n")
        check_date()
    if month_start > 12 or month_start < 1:
        print("Такого місяці не існує\n")
        check_date()
    if day_start > 31 or day_start < 1:
        print("У місяці не існує такого дня\n")
        check_date()
    if month_start == 2 and year_start % 4 == 0 and year_start % 400 != 0 and day_start > 29:
        print("В цьому році у лютому 29 днів\n")
        check_date()
    if month_start == 2 and year_start % 4 != 0 and day_start > 28:
        print("В цьому році у лютому 28 днів\n")
        check_date()
    if month_start in [4, 6, 9, 11] and day_start > 30:
        print("Некоректна дата, у цьомі місяці лише 30 днів\n")
        check_date()
    if year_start > year_today:
        print("Нажаль ми не навчилися знаходити курс у майбутньому\n")
        check_date()
    if year_start == year_today and month_start > month_today:
        print("Нажаль ми не навчилися знаходити курс у майбутньому\n")
        check_date()
    if year_start == year_today and month_start == month_today and day_start > day_today:
        print("Нажаль ми не навчилися знаходити курс у майбутньому\n")
        check_date()
    if year_start == year_today and month_start == month_today and day_start == day_today:
        print("Щоб переглянути курс сьогодні, перейдіть у відповідне меню:")

    return (year_start, month_start, day_start)


def create_list_of_dates(day_start, month_start, year_start, day_today, month_today, year_today):
    list = []
    check_month = False
    while year_start <= year_today:
        while month_start <= 12:
            if month_start == month_today and year_start == year_today:
                check_month = True
            if month_start in [1, 3, 5, 7, 8, 10, 12]: #дней в месяце 31
                while day_start <= 31:
                    tmp = str(year_start) + "-" + str(month_start) + "-" + str(day_start)
                    list.append(tmp)
                    day_start += 1
                    if check_month and day_start == day_today:
                        return list
                    if day_start > 31:
                        month_start += 1
                day_start = 1

            if month_start == 2 and year_start % 4 == 0 and year_start % 400 != 0: #высокосный год, дней в месяце 29
                 while day_start <= 29:
                    tmp = str(year_start) + "-" + str(month_start) + "-" + str(day_start)
                    list.append(tmp)
                    day_start += 1
                    if check_month and day_start == day_today:
                        return list
                    if day_start > 29:
                        month_start += 1
                 day_start = 1

            if month_start == 2 and year_start % 4 != 0 : #обычный год, дней в месяец 28
                while day_start <= 28:
                    tmp = str(year_start) + "-" + str(month_start) + "-" + str(day_start)
                    list.append(tmp)
                    day_start += 1
                    if check_month and day_start == day_today:
                        return list
                    if day_start > 28:
                        month_start += 1

                day_start = 1

            if month_start in [4, 6, 9, 11]: #дней в месяце 30
                while day_start <= 30:
                    tmp = str(year_start) + "-" + str(month_start) + "-" + str(day_start)
                    list.append(tmp)
                    day_start += 1
                    if check_month and day_start == day_today:
                        return list
                    if day_start > 30:
                        month_start += 1
                day_start = 1


        month_start = 1
        year_start += 1


def print_rate(year_start = 0, month_start = 0, day_start = 0):
    date_now = datetime.date.today()
    year_today = int(str(date_now)[0:4])
    month_today = int(str(date_now)[5:7])
    day_today = int(str(date_now)[8:10])
    if year_start == 0:
        year_start, month_start, day_start = check_date()
    old_buy, old_sale = 0, 0
    my_list = create_list_of_dates(day_start, month_start, year_start, day_today, month_today, year_today)
    try:
        i = my_list[0]
    except:
        return


    i = i[8:10] + "." + i[5:7] + "." + i[0:4]
    link_rate = "https://api.privatbank.ua/p24api/exchange_rates?json&date={}".format(i)
    page = requests.get(link_rate)
    rate = page.json()
    rate = rate["exchangeRate"]
    str_of_valutes = ""
    for i in rate:
        try:
            str_of_valutes += str(i["currency"])
            str_of_valutes += " "
        except:
            None
    print(str_of_valutes)
    valute = input("Введіть потрібну валюту: ")
    today_check = False
    try:
        for i in my_list:
            i = i[8:10] + "." + i[5:7] + "." + i[0:4]
            link_rate = "https://api.privatbank.ua/p24api/exchange_rates?json&date={}".format(i)
            page = requests.get(link_rate)
            rate = page.json()
            check = False
            for r in rate["exchangeRate"]:
                if 'currency' in r.keys() and r['currency'] == valute:
                    if old_buy != 0 and old_sale != 0:
                        difference_buy = old_buy - r['purchaseRateNB']
                        difference_sale = old_sale - r['saleRateNB']
                        print(i)
                        print("Купівля: " + str(r['purchaseRateNB']) + "    " + str(difference_buy))
                        print("Продаж: " + str(r['saleRateNB']) + "    " + str(difference_sale))
                        old_buy = r['purchaseRateNB']
                        old_sale = r['saleRateNB']
                    else:
                        print(i)
                        print("Купівля: " + str(r['purchaseRateNB']))
                        print("Продаж: " + str(r['saleRateNB']))
                        old_buy = r['purchaseRateNB']
                        old_sale = r['saleRateNB']
                    check = True

            if check is not True:
                print("Нажаль такої валюти немає\n")
                print_rate(year_start, month_start, day_start)



        link_rate_now = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        page = requests.get(link_rate_now)
        rate = page.json()
        for i in rate:
            if i['ccy'] == valute:
                difference_buy = old_buy - float(i['buy'])
                difference_sale = old_sale - float(i['sale'])
                print("Сьгодні")
                print("Купівля: " + str(i['buy']) + "   " + str(difference_buy))
                print("Продаж: " + str(i['sale']) + "   " + str(difference_sale) )
                today_check = True


        if 'ccy' not in rate.keys():
            print("Сталася помилка, курсу цієї валюти на цю дату немає")
            #print_rate()
    except:
        if today_check:
            None
        else:
            print("Якщо ви бажаєте подивитися курс на сьогодні, перейдіть у відповідний пункт меню")


