n=int(input("Enter the number of rout:"))
class buses:
    def __init__(self,bus,rout,mark,year,probeg):
        self.bus=bus
        self.rout=rout
        self.mark=mark
        self.year=year
        self.probeg=probeg


    def list_of_bus(bus_list,rout):
        print("number of", n)
        for bus in bus_list:
            if bus.rout==n:
                print(bus.bus)

# def list_of_bus(bus_list,rout):
#     print("number of rout", rout)
#     for bus in bus_list:
#         if bus.rout==43:
#             print(bus.bus)


def data(bus_list):
    print("year")
    for bus in bus_list:
         if 2017- bus.year > 10:
             print(bus.bus)

def long(bus_list):
    print("probeg > 10000 ")
    for bus in bus_list:
        if bus.probeg > 10000:
            print(bus.bus)

class model_of_buses(buses):
    def __init__(self,bus,rout,mark,year,probeg,model):
         buses.__init__(self,bus,rout,mark,year,probeg)
         self.model=model

#Полиморфизм
def display_more_info(self):
    buses.list_of_bus(self,43)
    print("number of buses on rout",n,"has model")
    for bus in self:
        if bus.rout == n:
            print("Model:",bus.model,"|","Number:",bus.bus)

#Superclass
A=buses(33,43,2,1999,10100)
B=buses(25,21,2,2010,10500)
C=buses(76,43,2,2008,9000)
D=buses(55,56,2,2013,12000)
E=buses(21,43,2,2005,8000)
F=buses(65,65,2,2014,13000)
G=buses(43,65,2,2003,8900)

#Subclass
A1=model_of_buses(33,43,2,1999,10100,"Horse")
B2=model_of_buses(25,21,2,2010,10500,"The Best")
C3=model_of_buses(76,43,2,2008,9000,"Power")
D4=model_of_buses(55,56,2,2013,12000,"Metal")
E5=model_of_buses(21,43,2,2005,8000,"Fire")
F6=model_of_buses(65,65,2,2014,13000,"Speed")
G7=model_of_buses(43,65,2,2003,8900,"Mega")

c=[A,B,C,D,E,F,G]
k=[A1,B2,C3,D4,E5,F6,G7]

#Начальный метод
#list_of_bus(c)
#Полиморфизм
display_more_info(k)
#дополнительные методы для 2 ого сохранения
data(c)
long(c)




