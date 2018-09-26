class Element():
    def __init__(self,IntegerKey, StringValue):
        if(type(IntegerKey) is not int):
            raise TypeError("IntegerKey must be an int")
        else:
            self.IntegerKey = IntegerKey
        if(type(StringValue) is not str):
            raise TypeError("StringValue must be a str")
        else:
            self.StringValue = StringValue
    def __str__(self):
        return '('+str(self.IntegerKey)+': "'+self.StringValue+'")'

    def __hash__(self):
        element = (self.IntegerKey,self.StringValue)
        return hash(element)

class StrongDictionary():
    def __init__(self,_name):
        if(type(_name) is not str):
            raise TypeError('_name must be a str')
        elif(_name is ""):
            raise ValueError('_name is empty')
        else:
            self._name = _name
            self._backend = set()

    def __str__(self):
        num = len(self._backend)
        digit = str(num).zfill(2)

        return '["'+self._name+'": '+ str(digit) + ' Elements]'

    def add(self,add):

        for elements in self._backend:
            keyAdd = elements.IntegerKey
            if keyAdd == add.IntegerKey:
                raise ValueError("key already in dict!")
        self._backend.add(add)

    def remove(self,remove):
        removed = False
        for elements in self._backend:
            key1 = elements.key
            if key1 == remove.IntegerKey:
                removed = True
                self._backend.remove(elements)
                break
        if removed is False:
            raise KeyError("element {} does not exist".format(str(remove)))

    def get(self,key):
        get = False
        for element in self._backend:
            if element.IntegerKey == key:
                get = True
        if(get == False):
            raise KeyError("element does not exist")

    def getAll(self):
        output = {}
        for element in self._backend:
            output[element.IntegerKey] = element.StringValue
        return output



if __name__ == "__main__":

    dict = {Element(123,"PanzerII"), Element(456,'PanzerIII'),Element(789,'PanzerIV'),Element(10,'Panther'),Element(11,'Tiger')}
    a = Element(123,"ASS WE CAN")
    print(a)

    b = StrongDictionary("asd")
    b.add(Element(123,"PanzerII"))

    print(b)
