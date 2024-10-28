# Your code here(づ ᴗ _ᴗ)づ♡

dict_id_price = {'001' : 70, '002' : 45, '003' : 64, '004' : 33}
cash = 0
def print_table():
    print('''| ID  | ProductName | Цена |
|-----|-------------|------|
| 001 | Батончик    | 70   |
| 002 | Вода        | 45   |
| 003 | Газировка   | 64   |
| 004 | Булочка     | 33   |''')

def read_id(str_):
    global inp_id
    if str_ == "ОТМЕНА":
        exit()
    if str_ not in dict_id_price:
        print("Товара с таким ID не существует")
        inp_id = input()
        read_id(inp_id)
    else:
        print(f"Внесите {dict_id_price[str_]} тугриков")

def check_bill_validity(str_):
    global cash
    if str_ == "ОТМЕНА":
        exit()
    str_ = int(str_)
    banknotes = [10, 50, 100, 500]
    if str_ not in banknotes:
        print("Внесена фальшивая куплюра")
        check_bill_validity(input())
    else:
        cash += int(str_)
        if dict_id_price[inp_id] > cash:
            print(f"Осталось внести {dict_id_price[inp_id] - cash} тугриков")
            check_bill_validity(input())
        else:
            print(f"Ваша сдача: {abs(dict_id_price[inp_id] - cash)} тугриков")

print_table()
inp_id = input()
read_id(inp_id)
check_bill_validity(input())