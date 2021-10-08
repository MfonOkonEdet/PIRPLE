# Home Work 9
"""
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
Next an inheritance classes from Vehicle called "Cars".
The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.
It should have another method called "Stop" that sets the value of isDriving to false.
Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter.
And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
Create 3 different cars, using your Cars class, and drive them all a different number of times.
Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance
Extra:
Create a Planes class that is also an inheritance class from Vehicle.
Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), but different in one respect:
Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false),
and an error message should be printed saying that the plane can't fly until it's repaired.
"""


class Vehicle:
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance = "False",TripsSinceMaintenance = 0):
        self.make = Make
        self.model = Model
        self.year = Year
        self.weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def setMake(self,Make):
        self.make = Make

    def setModel(self,Model):
        self.model = Model

    def setYear(self,Year):
        self.year = Year

    def setWeight(self,Weight):
        self.weight = Weight

    def setNeedsMaintenance(self,NeedsMaintenance):
        self.NeedsMaintenance = NeedsMaintenance

    def setTripsSinceMaintenance(self,TripsSinceMaintenance):
        self.TripsSinceMaintenance = TripsSinceMaintenance


class Cars(Vehicle):
    def __init__(self,isDriving,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False

    def getTripsSinceMaintenance(self):
        if self.isDriving == False:
            self.TripsSinceMaintenance += 1
            return self.TripsSinceMaintenance

    def getNeedsMaintenance(self):
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            return self.NeedsMaintenance
        

    def Repair(self):
        self.TripsSinceMaintenance =  0
        self.NeedsMaintenance = False

class Planes(Vehicle):
    def __init__(self,Flying,Landing,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.Flying = Flying
        self.Landing = Landing

    def Fly(self):
        if self.NeedsMaintenance == True:
            self.Flying = False
            print("Plane can't fly until it's repaired")
            return self.Flying

        else:
            self.Flying = True

    def Land(self):
        self.Landing = True


Car1 = Cars(False,"BMW","x6",2021,"250kg",False,2)

Car2 = Cars(False,"LEXUS","350",2016,"500kg",False,50)

Car3 = Cars(False,"HONDA","v6",2019,"400kg",False,100)

Car1.Drive()
print(Car1.make)
print(Car1.model)
print(Car1.year)
print(Car1.weight)
Car1.Stop()
Car1.getTripsSinceMaintenance()
Car1.getNeedsMaintenance()
print(Car1.NeedsMaintenance)
print(Car1.TripsSinceMaintenance,"\n")

Car2.Drive()
print(Car2.make)
print(Car2.model)
print(Car2.year)
print(Car2.weight)
Car2.Stop()
Car2.getTripsSinceMaintenance()
Car2.getNeedsMaintenance()
print(Car2.NeedsMaintenance)
print(Car2.TripsSinceMaintenance,"\n")

Car3.Drive()
print(Car3.make)
print(Car3.model)
print(Car3.year)
print(Car3.weight)
Car3.Stop()
Car3.getTripsSinceMaintenance()
Car3.getNeedsMaintenance()
print(Car3.NeedsMaintenance)
print(Car3.TripsSinceMaintenance,"\n")

Plane1 = Planes(False,True,"Arik Air","Boeing 312",2017,"5000LBS",False,40)
Plane1.setNeedsMaintenance(True)
Plane1.Fly()
print(Plane1.Flying)