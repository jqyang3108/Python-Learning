from enum import Enum
import random
def func1():
    a = 'fuc you'
    return a
#-------------------------------------------------------------------Level
class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4
#-------------------------------------------------------------------student
class Student:
    def __init__(self, ID, firstName, lastName, level):
        #
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        if(type(level) is not Level):
            raise TypeError("The argumen must be an instance of the 'Level' Enum.")
        else:
            self.level = level
    def __str__(self):
        year=''
        if(self.level == Level.freshman):#self.level.value == 1
            year = "Freshman"
        elif(self.level == Level.sophomore):
            year = "Sophomore"
        elif(self.level == Level.junior):
            year = "Junior"
        elif(self.level == Level.senior):
            year = "Senior"
        output = self.ID+', '+self.firstName+" "+self.lastName+', '+year
        return output

#-------------------------------------------------------------------circuit
class Circuit:
    def __init__(self, ID, resistors, capacitors, inductors, transistors):
        self.ID = ID
        for r in resistors:
            if(not r.startswith("R")):
                raise TypeError("The resistors' list contain invalid components")
        for c in capacitors:
            if(not c.startswith("C")):
                raise TypeError("The capacitors' list contain invalid components")
        for l in inductors:
            if(not l.startswith("L")):
                raise TypeError("The inductors' list contain invalid components")
        for t in transistors:
            if(not t.startswith("T")):
                raise TypeError("The transistors' list contain invalid components")
        self.resistors = list(set(resistors))
        self.capacitors = list(set(capacitors))
        self.inductors = list(set(inductors))
        self.transistors = list(set(transistors))

    def __str__(self):
        numRe = len(self.resistors)
        if(numRe < 10):
            numRe = '0'+str(numRe)

        numCa = len(self.capacitors)
        if(numCa < 10):
            numCa = '0'+str(numCa)

        numL = len(self.inductors)
        if(numL < 10):
            numL = '0'+str(numL)

        numT = len(self.transistors)
        if(numT < 10):
            numT = '0'+str(numT)
        output = "{}: (R = {}, C = {}, L = {}, T = {})".format(self.ID,numRe,numCa,numL,numT)
        return output

    def getDetails(self):
        re=self.resistors
        ca = self.capacitors
        ind = self.inductors
        tr = self.transistors

        r = list(set(re))
        r.sort()
        c = list(set(ca))
        c.sort()
        l = list(set(ind))
        l.sort()
        t = list(set(tr))
        t.sort()
        asd = ", ".join(r+c+l+t)

        output = str(self.ID) + ": " + asd
        return output

    def __contains__(self, comp):
        if(not(type(comp) is str)):
            raise TypeError ("Component is not a string.")
        if((not comp.startswith("R"))and(not comp.startswith("C"))and(not comp.startswith("L"))and(not comp.startswith("T"))):
            raise ValueError("Not valid type")
        if(comp.startswith("R")):
            if(comp in self.resistors):
                return True
            else:
                return False
        elif(comp.startswith("C")):
            if(comp in self.capacitors):
                return True
            else:
                return False
        elif(comp.startswith("L")):
            if(comp in self.inductors):
                return True
            else:
                return False
        elif(comp.startswith("T")):
            if(comp in self.transistors):
                return True
            else:
                return False
        return
    def __add__(self, comp):
        if(type(comp) is str):
            if (comp.startswith("R")):
                if (comp in self.resistors):
                    return self
                else:
                    self.resistors.append(comp)
                    return self
            elif (comp.startswith("C")):
                if (comp in self.capacitors):
                    return self
                else:
                    self.capacitors.append(comp)
                    return self
            elif (comp.startswith("L")):
                if (comp in self.inductors):
                    return self
                else:
                    self.inductors.append(comp)
                    return self
            elif (comp.startswith("T")):
                if (comp in self.transistors):
                    return self
                else:
                    self.transistors.append(comp)
                    return self
            else:
                raise ValueError("Not valid component")
        elif(type(comp) is Circuit):
            if (type(comp) is not Circuit):
                raise TypeError("Circuit 2 is not an instance of the Circuit class.")
            newID = random.sample(range(10000, 100000), 1)
            while (newID == self.ID or newID == comp.ID):
                newID = random.sample((10000, 100000), 1)
            newR = list(set(self.resistors + comp.resistors))
            newC = list(set(self.capacitors + comp.capacitors))
            newL = list(set(self.inductors + comp.inductors))
            newT = list(set(self.transistors + comp.transistors))
            newCir = Circuit(newID[0], newR, newC, newL, newT)
            return newCir
        else:
            raise TypeError("Type of argument is incorrect")
        return
    def __radd__(self, comp):
        if(not(type(comp) is str)):
            raise TypeError ("Component is not a string.")
        if((not comp.startswith("R"))and(not comp.startswith("C"))and(not comp.startswith("L"))and(not comp.startswith("T"))):
            raise ValueError("Not valid type")
        if(comp.startswith("R")):
            if(comp in self.resistors):
                return self
            else:
                self.resistors.remove(comp)
                return self
        elif(comp.startswith("C")):
            if(comp in self.capacitors):
                return self
            else:
                self.capacitors.append(comp)
                return self
        elif(comp.startswith("L")):
            if(comp in self.inductors):
                return self
            else:
                self.inductors.append(comp)
                return self
        elif(comp.startswith("T")):
            if(comp in self.transistors):
                return self
            else:
                self.transistors.append(comp)
                return self
        return
    def __sub__(self, comp):
        if(not(type(comp) is str)):
            raise TypeError ("Component is not a string.")
        if((not comp.startswith("R"))and(not comp.startswith("C"))and(not comp.startswith("L"))and(not comp.startswith("T"))):
            raise ValueError("Not valid type")
        if((comp not in self.resistors)and (comp not in self.capacitors)and(comp not in self.inductors)and(comp not in self.transistors)):
            return self

        if(comp.startswith("R")):
            print("aasd")
            self.resistors.remove(comp)
            return self
        elif(comp.startswith("C")):
            self.capacitors.remove(comp)
            return self
        elif(comp.startswith("L")):
            self.inductors.remove(comp)
            return self
        elif(comp.startswith("T")):
            self.transistors.remove(comp)
            return self


#------------------------------------------------------------------project
class Project:

    def __init__(self,ID,participants,circuits):
        if(not participants):
            raise ValueError("The participants' list is empty")
        if(not circuits):
            raise ValueError("The circuits' list is empty")
        self.ID = ID
        self.participant = participants
        self.circuit = circuits
    def __str__(self):
        numPar = len(self.participant)
        if(numPar < 10):
            numPar = '0'+str(numPar)

        numCir = len(self.circuit)
        if(numCir < 10):
            numCir = '0'+str(numCir)
        output = "{}: {} Circuits, {} Participants".format(self.ID,numCir,numPar)
        return output
    def getDetails(self):
        par =[]
        cir = []
        for s in self.participant:
            par.append(s.__str__())
        for s in self.circuit:
            cir.append(s.getDetails())
        par.sort()
        cir.sort()
        output = self.ID+"\n\n"+"Participants: \n"
        for s in par:
            output += str(s) + "\n"
        output += "\nCircuits: "
        for s in cir:
            output +='\n'+str(s)
        return output

    def __contains__(self, comp):         #comp in Proj
        if(type(comp) is str):
            if ((not comp.startswith("R")) and (not comp.startswith("C")) and (not comp.startswith("L")) and (not comp.startswith("T"))):
                raise ValueError("Not valid type")
            count = 0
            for s in self.circuit:
                if (comp in s):
                    count += 1
            if (count == 0):
                return False
            else:
                return True
        elif(type(comp) is Circuit):
            if (comp not in self.circuit):
                return False
            else:
                return True
        elif(type(comp) is Student):
            if(comp not in self.participant):
                return False
            else:
                return True
        else:
            raise TypeError("Type of argument is incorrect")

        return
    def __add__(self, add):
        if(type(add) is Circuit):
          #  print("add circuit")
            if(add in self.circuit):
                return self
            else:
              #  print("add")
                self.circuit.append(add)
                return self
        elif(type(add) is Student):
           # print("add student")
            if(add in self.participant):
                return self
            else:
              #  print("add")
                self.participant.append(add)
                return self
        else:
            raise TypeError("Type of argument is incorrect")
        return
    def __sub__(self, add):
        if(type(add) is Circuit):
            if(add not in self.circuit):
                return self
            else:
                self.circuit.remove(add)
                return self
        elif(type(add) is Student):
            if(add not in self.participant):
                return self
            else:
                self.participant.remove(add)
                return self
        else:
            raise TypeError("Type of argument is incorrect")
        return

class Capstone(Project):
    def __init__(self,ID,participant, circuit):
        for s in participant:
            if(s.level is not Level.senior):
                raise ValueError("Student is not senior.")
        Project.__init__(self,ID,participant, circuit)
    def __add__(self, student):
        if(student.level is not Level.senior):
            raise ValueError("Student is not senior.")
        else:
            Project.__add__(student)
        return

if __name__ == "__main__":

    stu1 = Student("48745-44785",'John','Wick',Level.senior)
    stu2 = Student("45323-87657", 'Qiwei', 'Ye', Level.senior)
    stu3 = Student("32105-44785", 'Yu', 'Cai', Level.senior)
    stu4 = Student("24568-29637", 'Shulin', 'Wang', Level.senior)
    stu5 = Student("21312-21626",'Jiaqi','Yang', Level.senior)
    component = "C12321321311.111"

    #---------------------------------------------------
    resistor = ['R333.333',"R222.222","R111.111","R111.121","R111.421","R111.123","R111.111","R111.111","R111.311","R111.111","R111.111"]
    capacitor = ['C333.333',"C222.222","C111.111"]
    inductor = ['L333.333',"L222.222","L111.111"]
    transistor = ['T333.333',"T222.222","T111.111"]
    ID = "13458"
    cir1 = Circuit(ID, resistor, capacitor, inductor, transistor)


    #print(cir1.__add__(component).getDetails())
    #print(cir1.__sub__(component).getDetails())

#--------------------------------------------------------------------------------------

    resistor2 = ['R333.113',"R222.442","R111.111","R111.121","R111.421","R111.123","R111.111","R111.111","R111.111","R111.111","R111.111","R111.111","R111.111"]
    capacitor2 = ['C333.743',"C262.222","C611.511"]
    inductor2 = ['L323.381',"L812.222","L912.111"]
    transistor2 = ['T723.333',"T122.222","T321.151"]
    ID2 = "12450"
    cir2 = Circuit(ID2,resistor2,capacitor2,inductor2,transistor2)

#--------------------------------------------------------------------

    resistor2 = ['R323233.113',"R222.442","R111.111","R123111.121","R1sdafsdf11.421","R111.123","R111.111","R111.111","R111.111","R111.111","R111.111","R111.111","R111.111"]
    capacitor2 = ['C333.743',"C262.222","C61sasad1.511"]
    inductor2 = ['L323.381',"L8332312.222","L912222.111"]
    transistor2 = ['T722143.333',"T122.222322","T321.151"]
    ID2 = "14550"
    cir3 = Circuit(ID2,resistor2,capacitor2,inductor2,transistor2)

#-------------------------------------------
    id = "12345687-a1s2-c2v2-d2dd-dhg84jyms945"
    component = "C333.333"
    empty = []
    stu = [stu1,stu2,stu3,stu4]
    project = [cir1,cir2]
    proj1 = Project(id, stu, project)


    print("output here-------------------")
    #print(cir1)
    pro2 = Capstone(id,stu,project)

    print(pro2.getDetails())
