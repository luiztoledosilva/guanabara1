while True:
    num=int(input("Voce quer ver a tabuada de qual valor? "))
    if num<0:
        break
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")