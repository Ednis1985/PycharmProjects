price = 0
while True:
    try:
        ticket_number = input('Количество билетов, которые Вы хотите приобрести на мероприятие? ')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_ticket = input(f'Для какого возраста билет №{i}? ')
            age_ticket = int(age_ticket)
            if age_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_ticket >= 18:
                price += 990
                print('Стоимость билета: 990 руб.')
            else:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом дополнительной скидки на полную стоимость заказа 10%')
else:
    print(f'Сумма к оплате {price} руб.')