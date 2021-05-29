print('here are the available bank ussd codes: \n1. Access Bank: *901# \n2. First bank: *894# \n3. UBA: *919# \n4. Unity bank: *7799# \n4. Zenith: *979#: ')
ussd = input('please type in your banks USSD code: ')
def menu():
    option = int(input('1. Check your bal\n2. Transfers\n3. Airtime\n4. Other services \n5. Access money \n6. Diamond xtra \n7. Xtra cash loan \n8. Mobile wallet\n\nPlease select an option: '))
    if(option == 1):
        pin = input('enter your pin: ')  
        print('retriving your bal an sms will be send to you shortly')
        main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
        if(main == 1):
            menu()
        elif(main == 2):
            exit()
        else:
            print('input error!')
    elif(option == 2):
        amount = input('enter amount: ')
        num = input('Enter the Acc number you want to tranfer the money to: ')
        pin = input('Enter four digits pin: ')
        compilation = 'Do you want to send'+amount+'to this account number: '+ num+'?\n1. Yes\n2. No\n'
        assure = input(compilation)
        if(assure == '1'):
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')            
        elif(assure == '2'):
            print('transanction cancelled')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
    elif(option == 3):
        choice = int(input('1. Self\n2. Others\n'))
        if(choice == 1):
            amount = (input('Enter amount: '))
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
        elif(choice == 2):
            amount=(input('Enter amount: '))
            number = input('Enter the phone number: ')
            compilation = 'Do you want to buy '+ amount+ ' naira worth of airtime for '+ number+'?: \n1. Yes\n2. No\n'
            assure = int(input(compilation))
            if(assure == 1):
                print('Transaction successful')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            elif(assure == 2):
                print('Transaction cancelled')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            else:
                print('invalid input')
    elif(option == 4):
        print('An sms would be sent to you shortly')
if(ussd == '*901#'):
    menu()
else:
    print('wrong input')