def twofer(who='you'):
    return f'One for {who}, one for me'


def fizzbuzz():
    for i in range(1, 101):
        if not i % 3 and not i % 5:
            print('fizzbuzz')
        elif not i % 3:
            print('fizz')
        elif not i % 5:
            print('buzz')

        else:
            print(i)


if __name__ == '__main__':
    while True:
        fizzbuzz()
        prompt = input('Do u want to continue? [y]/[n]: ')
        if prompt.lower() != 'y':
            break
