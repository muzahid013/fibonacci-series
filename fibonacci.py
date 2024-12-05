def fib(first, second):
    return first+second

while True:
    print('1. Generate Fibonacci series by number of terms:  ')
    print('2. Generate Fibonacci series by maximum value: ')
    print('3. Exit.')
        
    choice = input("Enter your choice: ")
    text = ""
    if choice == "1":
        first = 0
        second = 1
        text = text + str(first)
        term = int(input('Enter the number of terms: '))
        # print(first, end=', ')
        for fib in range(term-1):
            # print(second, end=', ')
            text = text + ', ' + str(second)
            first,second = second, first+second
        print(f'{text}\n')


    elif choice == "2":
        first = 0
        second = 1
        max = int(input('Enter the maximum value: '))
        # print(first, end=', ')
        text = text + str(first)
        for fib in range(max):
            if second < max:
                # print(second, end=', ')
                text = text + ', ' + str(second)
                first,second = second, first+second
            else:
                break
        print(f'{text}\n')


    elif choice == "3":
        break
        
    