def twofer(who='you'):
    return f'One for {who}, one for me'


def limerick():
    lim_list = ['Był skrzypek rodem z Prabutów,',
                'miał nogi za duże do butów.',
                'Wszystkie go uwierały,',
                'więc nosił futerały',
                'od skrzypiec zamiast butów.']
    for line in lim_list:
        print(line)


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
        limerick()
        prompt = input('Do u want to continue? [y]/[n]: ')
        if prompt.lower() != 'y':
            break
