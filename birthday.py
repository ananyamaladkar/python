def birthday(name):
    if name == 'albert':
        print(name, 'birthday is', data['albert'])
    elif name == 'benjamin':
        print(name,'birthday is', data['benjamin'])
    elif name == 'frank':
        print(name,'birthday is', data['frank'])
    else:
        print("the name is not in our dictionary")
data = {
        'albert': '03/14/1879',
        'benjamin': '01/17/1706',
        'frank': '12/10/1815',
       }
print('Welcome to the birthday dictionary. We know the birthdays of:albert,benjamin,frank')
name = str(input('Who\'s birthday do you want to look up?'))
birthday(name)