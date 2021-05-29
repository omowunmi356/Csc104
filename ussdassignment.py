print("Type Bank USSD CODE: ")

Banks = { '*894#' : 'First Bank\n'}
for key in Banks:
    print(key,'::',Banks[key])
Bank_Options = input("Select an option: ")

if Bank_Options in Banks.keys():
    print("You Have Selected",Banks[Bank_Options])
    
    if Bank_Options == '*894#':
        first_services = {'1': 'Quick Banking',
                    '2': 'Open an account',
                    '3': 'Loans',
                    '4': 'First Monie'}
        for key in first_services:
            print(key,first_services[key])
        quick = input("Select an option: ")
        if quick == '1':
            q_bank = {'1' : 'Transfers',
                      '2' : 'Airtime Self',
                      '3' : 'Airtime Others',
                      '4' : 'Enquiry Services',
                      '5' : 'Data'}
            for key in q_bank:
                print(key, q_bank[key])
            trans = input('Select an option: ')
            if trans == '1':
                bank_trans = {'1' : 'Access Bank',
                              '2' : 'GT Bank',
                              '3' : 'Skye Bank',
                              '4' : 'First Bank',
                              '5' : 'Fidelity Bank',
                              '6' : 'Diamond Access',
                              '7' : 'FCMB',
                              '8' : 'UBA',
                              '9' : 'Wema Bank',
                              '10': 'Key Stone Bank',
                              '11': 'Zenith Bank\n'}
                for key in bank_trans:
                    print(key,bank_trans[key])
                bank_trans_option = input('Select Bank: ')
                if bank_trans_option in bank_trans:
                    transf = input('Enter Amount: ')
                    tran_sf = input('Enter Account Number: ')
                    trans_pin = input('Enter Your Pin: ')
                    if trans_pin != '2121':
                        print("invalid pin")
                    else:
                        print('Transaction SuccessFull')
                else:
                    print('Invalid Option')
            
            elif trans == '2':
                airtime = input('Enter amount: ')
                air_pin = input('Enter pin to confirm: ')
                if air_pin != '2121':
                    print('Invalid Code')
                else:
                    print('Transaction Successful!')
            else:
                print('Invalid Option Selected')
            
                
else:
    print("Invalid USSD CODE") 