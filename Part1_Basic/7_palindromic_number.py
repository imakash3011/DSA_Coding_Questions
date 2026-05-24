def check_palin(var):
    var1 = var
    if var <=0:
        print("Not Palindromic")
        return
    new_var = 0
    while var>0:
        rem = var%10
        new_var = new_var*10 + rem
        var = var//10
        # print(rem, new_var)
    print(new_var, var1)
    if new_var==var1:
        print("Palindromic Number")
    else:
        print("Not Palindromic")


var = 12421
check_palin(var)