money = input('how much money do you want to save every month: ')

if not money.isdigit():
    print('Invalid amount')
else:
    money = int(money)
    year_saved = money * 12
    interest_total = year_saved * 1.008
    
    print(f'you will save £{year_saved} in a year')
    print(f'with interest you will save £{interest_total}')