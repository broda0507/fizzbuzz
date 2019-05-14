def fizzbuzz():
    for i in range(1, 101):
        if i % 3:
            print('fizz')
        elif i % 5:
            print('buzz')
        else:
            print(i)
