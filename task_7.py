# Your code here (づ๑•ᴗ•๑)づ♡

inp = int(input())

def F(int_):
    if int_ == 0:
        return 0
    int_2 = int_
    count = 0
    while int_2 != 0:
        int_2 = int_2 // 10
        count += 1
    return int_%10*10**count + F(int_ // 10)
def Y(int_):
    if int_ % 10 == 0 and int_ != 0:
        return Y(int_ // 10)
    return int_
print(int(F(Y(inp))/10))