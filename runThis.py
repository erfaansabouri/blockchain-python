from core import *

def main():
    system = BlockChain([])
    choice = int(input('Enter a Choice :\n\t1.Add new transaction\n\t2.Check Validity of the chain\n\t3.Show the current chain\n\t4.Save\n\t5.Load\n\t6.Exit\n>>'))
    while(choice != 6):
        if choice == 1:
            sender = str(input("Enter sender's name : ")) 
            receiver = str(input("Enter receiver's name : ")) 
            amount = int(input("Enter amount : ")) 
            transaction = Transaction(sender , receiver , amount)
            system.addBlock(transaction)
        if choice == 2:
            print(system.validationCheck())
        if choice == 3:
            res = []
            for item in system.chain:
                print(item.transaction)
        if choice == 4:
            fileName = str(input("Enter file's name : "))
            system.save(fileName)
        if choice == 5:
            fileName = str(input("Enter file's name : "))
            system.load(fileName)
        choice = int(input('Enter a Choice :\n\t1.Add new transaction\n\t2.Check Validity of the chain\n\t3.Show the current chain\n\t4.Save\n\t5.Load\n\t6.Exit\n>>'))
    print('Exit succesfully.')
        

if __name__ == '__main__':
    main()