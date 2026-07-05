import pandas as pd
class employee_data:
    def __init__(self, name,age,salary):
        self.__name, self.__age,self.__salary=name,age,salary
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self,nName):
        self.__name= nName
    
    def set_age(self,nAge):
        self.__age= nAge
    
    def set_salary(self,nSalary):
        self.__salary= nSalary
    
    def __str__(self):
        return f"Employee name: {self.__name}, age is {self.__age}, salary {self.__salary}"
employees_list=[]


def menu_display():
    print("Enter your choice: ")
    print("1) Add new employee ")
    print("2) Print all employees ")
    print("3) Delete by age ")
    print("4) Update salary by name ")
    print("5) End the program ")


def add_new_employee():
    name=input("Enter name: ")
    age= int(input("Enter age: "))
    salary= float(input("Enter the salary: "))

    new_employee=employee_data(name, age, salary)
    employees_list.append(new_employee)
    print(f"{name} is succsefull added")


def print_all_employees_name():
    if  len(employees_list)==0:
        print("No Employees yet")
    else:
        for i in employees_list:
         print(i)

def delete_by_age():
    start_age=int(input("Enter the terget age to delete "))
    end_age=int(input("Enter the terget age to delete "))

    for del_age in range(len(employees_list)-1,-1,-1):
        em =employees_list[del_age]

        if start_age <=em.get_age() <= end_age:
            del employees_list[del_age]

def save_to_excel():
    manage_data=[{"Name":em.get_name(), "Age":em.get_age(), "Salary":em.get_salary()} for em in employees_list]
    file= pd.DataFrame(manage_data)
    file.to_excel("Employees_data.xlsx" , index=False)
    print("Employees data saved succesfully")

def Update_salary_by_name():
    name=input("Enter the name: ")
    new_salary=float(input("Enter the new salary"))
   
    for em in employees_list:
        if em.get_name()== name:
           em.set_salary(new_salary)
           break
            

def menu_choose():

    while True:
        menu_display()
        choice=int(input())


        if choice >=1 and choice <=5: 
            if choice == 1:
                add_new_employee()
            
            elif choice == 2:
                print_all_employees_name()
            elif choice == 3:
                delete_by_age()
            elif choice == 4:
                Update_salary_by_name()
            elif choice == 5:
                save_to_excel()
                print(f"End the program")
                break
        else:
            print("enter valid number")

menu_choose()