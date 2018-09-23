from databaseConnector import DBConnect as connect
from abc import ABCMeta, abstractmethod
from executive import Executive
from manager import Manager
from salaried import Salaried
from hourly import Hourly

class Employee(metaclass=ABCMeta):
    @abstractmethod
    def RegisterEmployee(self,Efname,Elname,Edob,Econtact,EmployeeBasicPay):
        print("all good")
    @abstractmethod
    def RaiseEmployee(self,Efname,Elname,Edob):
        print("Raised Employee")

class Company:
    print("Welcome to the Company Manager system".center(100,'*'))
    userSelect = int(input("Please enter the operation you wish to perform\n1.Add/Hire Employee\n2.Raise Employee\n3.Fire Employee\n"))
    if(userSelect == 1):        
        empTypeSelect = int(input("\nPlease enter the employee type:\n1.Hourly Employee\n2.Salaried Employee\n3.Manager\n4.Executive\n"))
        if(empTypeSelect == 1):
            try:
                print("New Hourly Employee Details".center(100,"*"))
                Efname = str(input("Please enter the firstname of the Employee: "))
                Elname = str(input("Please enter the lastname of the Employee: "))
                Edob = str(input("Please enter the DOB of the Employee in DD/MM/YYYY format: "))
                Econtact = str(input("Please enter the contact number of the Employee: "))
                EmployeeBasicPay = str(input("Please enter the basic pay of the Employee: "))
                hourly = Hourly()
                hourly.RegisterEmployee(Efname,Elname,Edob,Econtact,EmployeeBasicPay)
            except Exception as e:
                print("Something went wrong")
                raise e
        elif(empTypeSelect == 2 ):
            try:
                print("New Salaried Employee Details".center(100,"*"))
                Efname = str(input("Please enter the firstname of the Employee: "))
                Elname = str(input("Please enter the lastname of the Employee: "))
                Edob = str(input("Please enter the DOB of the Employee in DD/MM/YYYY format: "))
                Econtact = str(input("Please enter the contact number of the Employee: "))
                EmployeeBasicPay = str(input("Please enter the basic pay of the Employee: "))
                salaried = Salaried()
                salaried.RegisterEmployee(Efname,Elname,Edob,Econtact,EmployeeBasicPay)
            except Exception as e:
                print("Something went wrong")
                raise e        
        elif(empTypeSelect == 3 ):
            try:
                print("Details of new manager".center(100,"*"))
                Efname = str(input("Please enter the firstname of the Manager: "))
                Elname = str(input("Please enter the lastname of the Manager: "))
                Edob = str(input("Please enter the DOB of the Manager in DD/MM/YYYY format: "))
                Econtact = str(input("Please enter the contact number of the Manager: "))
                EmployeeBasicPay = str(input("Please enter the basic pay of the Manager: "))
                manager = Manager()
                manager.RegisterEmployee(Efname,Elname,Edob,Econtact,EmployeeBasicPay)
            except Exception as e:
                print("Something went wrong")
                raise e        
        elif(empTypeSelect == 4):
            try:
                print("Executive Details".center(100,"*"))
                Efname = str(input("Please enter the firstname of the Executive: "))
                Elname = str(input("Please enter the lastname of the Executive: "))
                Edob = str(input("Please enter the DOB of the Executive in DD/MM/YYYY format: "))
                Econtact = str(input("Please enter the contact number of the Executive: "))
                EmployeeBasicPay = str(input("Please enter the basic pay of the Executive: "))
                e = Executive()
                e.RegisterEmployee(Efname,Elname,Edob,Econtact,EmployeeBasicPay)   
            except Exception as e:
                print("Something went wrong")
                raise e
    
    elif(userSelect == 2):
        empTypeSelect = int(input("\nPlease enter the employee type to which you want to give raise:\n1.Hourly Employee\n2.Salaried Employee\n3.Manager\n4.Executive\n"))
        if(empTypeSelect == 1):
            try:
                print("Updation of salary of Hourly Employee".center(100,'*'))
                Efname = str(input("Please enter the first name of the Hourly Employee: "))
                Econtact = str(input(f"Please enter the contact number of the {Efname}: "))
                EnewSal = int(input(f"Please enter the amount of rise of the basicpay of {Efname}: "))
                h = Hourly()
                h.RaiseEmployee(Efname,Econtact,EnewSal)
            except Exception as e:
                print("Something went wrong.")
        elif(empTypeSelect == 2):
            try:
                print("Updation of salary of Salaried Employee".center(100,"*"))
                Efname = str(input("Please enter the first name of the Salaried Employee: "))
                Econtact = str(input(f"Please enter the contact number of the {Efname}: "))
                EnewSal = int(input(f"Please enter the amount of rise of the basicpay of {Efname}: "))
                s = Salaried()
                s.RaiseEmployee(Efname,Econtact,EnewSal)
            except Exception as e:
                print("Something went wrong.")
        elif(empTypeSelect == 3):
            try:
                print("Updation of salary of Manager".center(100,'*B'))
                Efname = str(input("Please enter the first name of the Manager: "))
                Econtact = str(input(f"Please enter the contact number of the {Efname}: "))
                EnewSal = int(input(f"Please enter the amount of rise of the basicpay of {Efname}: "))
                m = Manager()
                m.RaiseEmployee(Efname,Econtact,EnewSal)
            except Exception as e:
                print("Something went wrong.")
        elif(empTypeSelect == 4):
            try:
                print("Updation of salary of Executive")
                Efname = str(input("Please enter the first name of the executive: "))
                Econtact = str(input(f"Please enter the contact number of the {Efname}: "))
                EnewSal = int(input(f"Please enter the amount of rise of the basicpay of {Efname}: "))
                e = Executive()
                e.RaiseEmployee(Efname,Econtact,EnewSal)
            except Exception as e:
                print("Something went wrong.")
                    
    elif(userSelect == 3):
        empTypeSelect = int(input("\nPlease enter the employee type to which you want to fire:\n1.Hourly Employee\n2.Salaried Employee\n3.Manager\n4.Executive\n"))
        if(empTypeSelect == 1):
            pass
        elif(empTypeSelect == 2):
            pass
        elif(empTypeSelect == 3):
            pass
        elif(empTypeSelect == 4):
            pass
        
