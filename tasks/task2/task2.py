def fizzBuzz():
    for i in range(11, 80):
        if i%5==0 and i%3==0:
            print('$$@@')
        elif i%5==0:
            print('@@')
        elif i%3==0:
            print('$$')
        else: print(i)

        
# fizzBuzz()

def fizzBuzzMap():
    return(list(map(lambda x: '$$'*(x%3==0)+'@@'*(x%5==0) or str(x), range(11, 80))))

print(fizzBuzzMap())