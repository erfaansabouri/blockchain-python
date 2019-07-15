import pickle
import datetime
import hashlib

class Transaction:
    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return '[' \
               + 'Sender : ' + self.sender \
               + ' | Receiver : ' + self.receiver \
               + ' | Amount : ' + str(self.amount) + \
               ']'


class Block:
    def __init__(self,index,transaction,previous_hash = ''):
        self.index = index
        self.transaction = transaction
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        dataToHash = str(transaction.amount) + str(index) + str(self.timestamp) + str(self.previous_hash)
        self.hash = hashlib.sha256((dataToHash).encode('utf-8')).hexdigest()
    def hashBlock(self):
        return self.hash

class BlockChain:
    def __init__(self,chain):
        self.chain = chain
        
    def addBlock(self,transaction):
        index = len(self.chain)
        if index == 0:
            newBlock = Block(index,transaction)
            self.chain.append(newBlock)
            print('Block added succesfully.')
            return
        previous_hash = self.chain[index - 1].hashBlock()
        newBlock = Block(index,transaction,previous_hash)
        self.chain.append(newBlock)
        print('Block added succesfully.')
        
        
    def save(self,address):
        output = open(address,'wb')
        pickle.dump(self,output)
        output.close()
        print("The chain dumped succesfully.")
    
    def load(self,address):
        input = open(address,'rb')
        result = pickle.load(input)
        self.chain = result.chain
        print("The chain loaded succesfully.")
    
    def validationCheck(self):
        flag = 0
        for block in self.chain:
            if flag == 0:
                flag = 1
                pre_hash = block.hash
                continue
            if block.previous_hash != pre_hash:
                print('Error.')
            pre_hash = block.hash
        return 'OK'
            

''''
myBC = BlockChain([])


ta = Transaction("erfan" , "saman" , 1000)
tb = Transaction("mamad" , "ali" , 2000)
tc = Transaction("nader" , "soosan" , 3500)
td = Transaction("pooria" , "farhad" , 8900)

print(myBC.addBlock(ta))
myBC.addBlock(tb)
myBC.addBlock(tc)
myBC.addBlock(td)
'''