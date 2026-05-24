num = 6743

def extract_num(num):
    if num == 0:
        print(0)
        return
    while num>0:
        rem = num%10
        print(rem)
        num = num//10
        
extract_num(num)
