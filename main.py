import random
# import timeit

HELP_MESSAGE = '''USAGE :
Enter first digits to get a list of phone numbers;\n
Enter 'fill' to add random 5000 numbers to db;\n
Enter 'clear' to delete all numbers from db;\n
Enter 'exit' to exit;\n
Enter 'help' to see this message again.
'''
numbers_db = set()


def fill_db(*args) :
    old_len = len(numbers_db)
    for _ in range(5000) :
        numbers_db.add('380'+random.choice(('50','63','67','91','95','97'))+''.join(["%s" % random.randint(0, 9) for _ in range(7)]))
    new_len = len(numbers_db)
    print('New DB count : ', new_len)
    return new_len - old_len


def clear_db(*args):
    print('Clearing DB...')
    numbers_db.clear()
    new_len = len(numbers_db)
    print('New DB count : ', new_len)
    return new_len

def display_help(*args) :
    print(HELP_MESSAGE)
    return True

def process_digits(digits):
    if not digits.isdigit() :
        print('Ivalid digits. You probably entered some letters. Try again or use help for more information.')
        return 13
    if len(digits) > 12 :
        print('Too many digits. Phone numbers consist only of 12 digits. Try again or use help for more information.')
        return 12
    i = 0
    for number in numbers_db :
        if number.startswith(digits) :
            if i == 0 :
                print('\nYour number(s) :')
            print(number)
            i += 1
        if i == 10 :
            return 10
    if i == 0 :
        print('No match')
        return 0
    return i

# def time_test(*args):
#     print(timeit.timeit("process_digits_a('38091')",number=10000,globals=globals()))
#     print(timeit.timeit("process_digits_b('38091')",number=10000,globals=globals()))


if __name__ == '__main__':
    random.seed()
    commands = {
    'help': display_help,
    'fill': fill_db,
    'clear': clear_db,
    # 'time': time_test,
     }
    user_input = 'help'
    while  user_input != 'exit' :
        commands.get(user_input,process_digits)(user_input)
        user_input = input('\nEnter first digits or command : ').lower()


