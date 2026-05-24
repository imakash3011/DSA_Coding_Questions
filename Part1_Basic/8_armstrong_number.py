import math
def check_armstrong(var):
    var1  = var
    if var<0:
        return "Enter Valid Number"
    len_var = math.floor(math.log10(var)+1)
    temp = 0
    # print(len_var)
    while var>0:
        rem = var%10
        var = var//10
        temp = temp + rem**len_var
        print(var, temp)
    if temp == var1:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"

var = 1634
print(check_armstrong(var))