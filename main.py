from dbcode import DBHelper
import re

#for validating an phone number
pattern = re.compile("(0|91)?[6-9][0-9]{9}")

def main():
    db=DBHelper()
    while True:
        print("{:>63}".format("************************************"))
        print("{:>63}".format("-->> Employee Management System <<--"))
        print("{:>63}".format("************************************"))
        print()
        print("1. Add Employee")
        print("2. Display Employee Record")
        print("3. Update Employee Record")
        print("4. Promote Employee Record")
        print("5. Remove Employee Record")
        print("6. Search Employee Record")
        print("7. Exit/")
        print()
        print("{:>67}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))
        try:
            choice=int(input("Enter your Choice:"))
            if(choice==1):
                #insert emp
                print()
                print("{:>60}".format("-->> Add Employee Record <<--"))
                id=int(input("Enter Employee Id: "))
                if(db.check_emp(id) == True):
                    print("Employee Id Already Exist\n Try Again..")
                    press = input("Press Any Key To Continue..")
                    main()
                name=input("Enter Employee Name: ")
                phone=input("Enter Employee phone No.: ")
                if(pattern.match(phone)):
                    pass
                else:
                    print("Invalid Phone no.\n Try Again..")
                    press = input("Press Any Key To Continue..")
                    main()
                post=input("Enter Employee Post: ")
                salary=input("Enter Employee Salary: ")
                db.insert_emp(id,name,phone,post,salary)
                press = input("Press Any Key To Continue..")
                main()
            elif choice==2:
                #display employees
                print()
                print("{:>60}".format("-->> All Employee Record <<--"))
                db.fetch_all()
                pass
            elif choice==3:
                #update emp
                print()
                print("{:>60}".format("-->> Update Employee Record <<--"))
                id=int(input("Enter Employee Id: "))
                if(db.check_emp(id) == False):
                    print("Employee Not Exist\n Try Again..")
                    press = input("Press Any Key To Continue..")
                    main()
                name=input("Enter New Name: ")
                phone=input("Enter New phone No.: ")
                if(pattern.match(phone)):
                    pass
                else:
                    print("Invalid Phone no.\n Try Again..")
                    press = input("Press Any Key To Continue..")
                    main()
                db.update_emp(id,name,phone)
            elif choice==4:
                #promote emp
                print()
                print("{:>60}".format("-->> Promote Employee Record <<--"))
                id=int(input("Enter Employee Id: "))
                if(db.check_emp(id) == False):
                    print("Employee Not Exist\n Try Again..")
                    press = input("Press Any Key To Continue..")
                    main()
                post=input("Enter New Post: ")
                salary=input("Enter New Salary: ")
                db.promote_emp(id,post,salary)
            elif choice==5:
                #delete emp
                print()
                print("{:>60}".format("-->> Delete Employee Record <<--"))
                id=int(input("Enter Employee id : "))
                if(db.check_emp(id) == False):
                    print("Employee Not Exist\n Put Right Id..")
                    press = input("Press Any Key To Continue..")
                    main()
                db.delete_emp(id)
            elif choice==6:
                #search emp
                print()
                print("{:>60}".format("-->> Search Employee Record <<--"))
                id=int(input("Enter Employee id : "))
                if(db.check_emp(id) == False):
                    print("Employee Not Exist\n Put Right Id..")
                    press = input("Press Any Key To Continue..")
                    main()
                db.search_emp(id)
            elif choice==7:
                #exit program
                break
            else:
                print("Invalid input !")
                press = input("Press Any Key To Continue..")
                main()
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again ")

if __name__ == "__main__":
    main()
