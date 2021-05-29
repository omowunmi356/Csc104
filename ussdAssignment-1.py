print("Type Your Bank USSD CODE: ")

Banks = {'*894#' : 'First Bank\n'}
for key in Banks:
    print(key,'::',Banks[key])
Bank_Options = input("Select an option: ")

if Bank_Options in Banks.keys():
    print("You Have Selected",Banks[Bank_Options])
            
    if Bank_Options == '*894#':
        first_services = {'1': 'Quick Banking',
                    '2': 'Open an accounts',
                    '3': 'Loans',
                    '4': 'First Monie'}
        for key in first_services:
            print(key,first_services[key])
        quick = input("Select an option: ")
        
        if quick == '4':
            first_monie = input('1. Link account with first monie: ')
            if first_monie != '1':
                print('Wrong Selection')
            monie_account = input('1. 232xxxx192: ')
            if monie_account != '1':
                print('Incorrect selection')
            print('SuccessFul, Thanks For banking with us!')
        
        if quick == '3':
            loan = input('1. firstAdvance: ')
            if loan != '1':
                print('Invalid input')
            loans = {'1' : 'Get loan',
                     '2' : 'repay loan'}
            for key in loans:
                print(key, loans[key])
            loans_opt = input("select: ")
            
            if loans_opt == '2':
                print('You Haven\'t borrowed from us thank you!')
            
            if loans_opt == "1":
                print("accept our terms and conditions")
                condition = {"1":"accept",
                             "2":"decline"}
                for key in condition:
                    print(key, condition[key])
                    
                my_condition = input('Accept Or Decline: ')
                
                if my_condition == "1":
                    print("you are eligible for the following amount:")
                    eligible_amount = {'1' : '#800,000,000',
                                       '2' : '#500,000,000',
                                       '3' : '#10,000,000',
                                       '4' : '#1,000,000',
                                       '5' : '500,000'}
                    for key in eligible_amount:
                        print(key, eligible_amount[key])
                    
                    my_eligible = input('Select an amount: ')
                    if my_eligible in eligible_amount:
                        loan_pin = input('Enter your pin: ')
                        if loan_pin != '2021':
                            print('incorrect pin')
                        print('Loan Successful!, Thank You for Banking With Us!')
                else:
                    print('Thank You for Banking With Us!')
                    
        
        if quick == '2':
            print('You already have a first bank account')
            
        if quick == '1':
            q_bank = {'1' : 'Transfers',
                      '2' : 'Airtime Self',
                      '3' : 'Airtime Others',
                      '4' : 'Enquiry Services',
                      '5' : 'Data\n'}
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
                    if trans_pin != '2021':
                        print("invalid pin")
                    else:
                        print('Transaction SuccessFull')
                else:
                    print('Invalid Option')
            
            if trans == '2':
                airtime = input('Enter amount: ')
                air_pin = input('Enter pin to confirm: ')
                if air_pin != '2021':
                    print('Invalid Code')
                else:
                    print('Transaction Successful!')    
            
            if trans == '3':
                other = input('Enter Phone number: ')
                air_other = input('Enter Amount: ')
                other_pin = input('Enter pin to confirm: ')
                if other_pin != '2021':
                    print('Invalid pin')
                else:
                    print('Transaction Successful!')
                    
            if trans == '4':
                enquiry = {'1':'Balance enquiry',
                           '2' : 'Bvn enquiry',
                           '3' : 'Account Number',
                           '4' : 'Mini statement'}
                
                for key in enquiry:
                    print(key, enquiry[key])
                    
                enquire_balance = input('Select an option: ')
                if enquire_balance == '1':
                    print('Your account Balace is 989,000,000,000')
                if enquire_balance == '2':
                    print('Your BVN Number is 92019283749')
                if enquire_balance == '3':
                    print('Your Acccount Number is 0033789347')
                if enquire_balance == '4':
                    print('please wait... fetching account statement')
            
            if trans == '5':
                data = {'1' : 'Self',
                        '2' : 'third party'}
                for key in data:
                    print(key,data[key])
                
                self_s = input('Select option: ')
                if self_s == '1':
                    data_amount = {'1':"""40GB #1000, 30days""",
                                   '2' : """35GB #500 3days""",
                                   '3' : """80GB #50 2hrs""",
                                   '4' : """72MB #100, 7days""",
                                   '5' : """500MB #30"""}
                    for key in data_amount:
                        print(key,data_amount[key])
                    
                    select_amount = input('Enter option: ')
                    if select_amount in data_amount:
                        data_pin = input('Input pin: ')
                        if data_pin != '2021':
                            print('wrong pin')
                
                if self_s == '2':
                    party = input('Enter phone number: ')
                    data_amount = {'1':"""40GB #1000, 30days""",
                                   '2' : """35GB #500 3days""",
                                   '3' : """80GB #50 2hrs""",
                                   '4' : """72MB #100, 7days""",
                                   '5' : """500MB #30"""}
                    for key in data_amount:
                        print(key,data_amount[key])
                    
                    select_data_amount = input('Enter option: ')
                    if select_data_amount in data_amount:
                        data_pin = input('Input pin: ')
                        if data_pin != '2021':
                            print('wrong pin')

else:
    print("Invalid USSD CODE") 