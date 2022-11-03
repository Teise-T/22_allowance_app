def isfloat(num):
    try:
        float(num)
        return 
    except ValueError:
        return False


print(isfloat('s12'))
print(isfloat('1.123'))
