from databaseConnector import DBConnect as connect
from abc import ABCMeta, abstractmethod
import executive
# from manager import *
# from salaried import *
# from hourly import *

class Employee(metaclass=ABCMeta):
    @abstractmethod
    def RegisterEmployee(self,Efname,Elname,Edob,Econtact,EmployeeBasicPay):
        print("all good")

class Executive():    
    def RegisterEmployee(self,Efname,Elname,Edob,Econtact,EmployeeBasicPay):
        try:
            flag = 0
            db,cursor = connect()
            insert_query = f"insert into executive(executive_fname,executive_lname,executive_dob,executive_contact,executive_basicpay) values('{Efname}','{Elname}','{Edob}','{Econtact}','{EmployeeBasicPay}')"
            search_query = f"select * from executive where executive_fname like '{Efname}' and executive_contact like '{Econtact}'"
            cursor.execute(search_query)
            rs = cursor.fetchall()
            if(len(rs)>0):
                flag = 1
            else:
                cursor.execute(insert_query)
                db.commit()
        except Exception as e:
            db.rollback()
            raise e
        else:
            if(flag == 0):
                print("inserted successfully")
            else:
                print("record already exist")
        finally:
            db.close()

class Company():
    print("Welcome to the Company Manager system".center(100,'*'))
    userSelect = int(input("Please enter the operation you wish to perform\n1.Add/Hire Employee\n2.Raise Employee\n3.Fire Employee\n"))
    if(userSelect == 1):
        empTypeSelect = int(input("\nPlease enter the employee type:\n1.Hourly Employee\n2.Salaried Employee\n3.Manager\n4.Executive\n"))
        if(empTypeSelect == 4):
            try:
                Efname = str(input("Please enter the firstname of the Executive: "))
                Elname = str(input("Please enter the lastname of the Executive: "))
                Edob = str(input("Please enter the DOB of the Executive in DD/MM/YYYY format: "))
                Econtact = str(input("Please enter the contact number of the Executive: "))
                EmployeeBasicPay = str(input("Please enter the basic pay of the Executive: "))
                Executive.RegisterEmployee(Efname,Elname,Edob,Econtact,EmployeeBasicPay)                                              
            except Exception as e:
                print("Something went wrong")
                raise e