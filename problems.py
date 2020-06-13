x = 99
try:
    x+=1
except NameError as error:
    x = -1
finally:
    print("pruvet nPiBeT", x)