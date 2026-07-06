print('Welcome save bank')

name = input('Enter your name:')

balance = 50000

print('Welcome',name)
print('Balance =', balance)

print('1. Check Balance')
print('2. Deposit Money')
print('3. Withdraw Money')
print('4. Exit')

choice = input('Choose an option:')


if choice == '1':
    print('Balance =',balance)
elif choice == '2':
    amount = int(input('Enter amount:'))
    balance = balance + amount
    print('New balance=', balance)
elif choice == '3':
    amount = int(input('Enter amount:'))
    if amount > balance:
        print('Insufficient funds')
    else:
        balance = balance - amount
        print('New balance=',balance)
elif choice == '4':
    print ('Exit')
else:
    print('Invaild number')
