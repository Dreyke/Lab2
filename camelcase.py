__author__ = 'Dreyke Boone'

def convert(word):
    output = ''.join(x for x in word.title() if x.isalnum())
    return output[0].lower() + output[1:]

convertString = input("Enter a string: ")
print(convert(convertString))

def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n',  stars, '\n')

    display_banner()
