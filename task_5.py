def process_items(str_):
    pass

# Your code here (づ｡◕‿‿◕｡)づ

ls = []
count = 0
while count != 3:
    inp = input()
    tr = True
    for i in inp.split():
        if i not in ['меч', 'лук', 'топор', 'щит', 'зелье']:
            print("Неверный предмет, попробуйте снова")
            tr = False
    if tr:
        for i in inp.split():
            ls.append(i)
        count += 1
#print(ls)
count = 0
ls_set = set(ls)
for i in ls_set:
    if ls.count(i) == 3:
        count += 1
print(count)