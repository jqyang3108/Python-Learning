class Action:
    def __init__(self,actionType, amount):
        if(actionType == "W" or actionType == "D"):
            self.act = actionType
            self.amount = amount
        else:
            raise ValueError("Action type is not correct")
        return

class Client:
    def __init__(self, firstName, lastName):
        self.first = firstName
        self.last = lastName
    def __str__(self):
        output = self.first + " " + self.last
        return output

class Account:
    def __init__(self,accountNumber, client, amount, minThreshold):
        self.account = accountNumber
        self.client = client
        self.amount = amount
        self.thre = minThreshold
    def __str__(self):
        if(self.amount >= 0):
            output = self.account + ", " + str(self.client) + ", Balance = $"+ str(round(self.amount,2))
        else:
            output = self.account + ", " + str(self.client) + ", Balance = ($"+ str(abs(round(self.amount,2))) + ")"
        return output
    def performAction(self,action):
        if(action.act == "D"):
            self.amount += action.amount
        elif(action.act == "W"):

            if((self.amount - action.amount) > self.thre):
                amount = round(self.amount - action.amount,2)
            else:
                amount = round(self.amount - action.amount -10,2)
            if(amount < 0):
                raise ValueError("Invalid action, amount is less than 0")
            else:
                self.amount = round(amount,2)
        return
class Institute:
    def __init__(self,accounts):
        self.dict = accounts

    def createNew(self,firstName, lastName, account):
        if(account not in self.dict):
            client = Client(firstName,lastName)
            a = Account(account,client, 500.00, 1000.00)
            self.dict[account] = a

    def performAction(self,account, action):
        if((account in self.dict)):
            if(action.act == "D"):
                self.dict[account].amount += action.amount
            elif(action.act == "W"):

                if((self.dict[account].amount - action.amount) > self.dict[account].thre):
                    amount = round(self.dict[account].amount - action.amount,2)
                else:
                    amount = round(self.dict[account].amount - action.amount -10,2)
                if(amount < 0):
                    raise ValueError("Invalid action, amount is less than 0")
                else:
                    self.dict[account].amount = round(amount,2)

if __name__ == "__main__":

    first = "Jssd"
    last = "Lasts"
    num = float(12343.11)
    thre = float(123123.22)

    action = Action("W",200)
    client = Client(first,last)
    account1 = Account("123123-123123",client, num, thre)
    account2 = Account("123233-123123",client, 320, 1000)
    dict = {account1.account:account1, account2.account:account2}

    account1.performAction(action)

    inst = Institute(dict)
    inst.createNew("asd","asd","123123-165123")

    inst.performAction("123233-123123",action)

    #print(account1)

