num = 0
total = 0.0
while True :
    val = input('Enter a number: ')
    if val == 'done' :
        break
    try:
        fval = float(val)
    except:
        print('Invalid input')
        continue
    print(fval)
    num += 1
    total += fval
print(total, num, (total / num))
