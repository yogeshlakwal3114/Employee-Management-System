import mysql.connector

class DBHelper:
    #Created
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',
                                           port='3306',
                                           user='root',
                                           password='Yogesh@123',
                                           database='pythonsql')
        query = 'create table if not exists emp(empId int primary key, empName varchar(255), phone varchar(12), post varchar(255), salary varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)
        # print("created Database")

    # Add Employee Record(function)
    def insert_emp(self,empId,empName,phone,post,salary):
        query = "insert into emp(empId, empName, phone, post, salary) values({},'{}','{}','{}','{}')".format(empId,empName,phone,post,salary)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()    #permanent Insert in DB
        print("Successfully Added Employee Record")
        print()

    # Function To check if Employee with given Id Exit or not
    def check_emp(self,empId):
        query = "select * from emp where empId={}".format(empId)
        cur = self.con.cursor(buffered=True)
        cur.execute(query)
        r = cur.rowcount
        if r == 1:
            return True
        else:
            return False
           

    #Fetch all Employee Record(Display)
    def fetch_all(self):
        query = "select * from emp"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Employee Id : ", row[0])
            print("Employee Name : ", row[1])
            print("Employee Phone No. : ", row[2])
            print("Employee Post : ", row[3])
            print("Employee Salary : ", row[4])
            print()

    #Update Employee Record
    def update_emp(self, empId, empName, phone):
        query = "update emp set empName='{}', phone='{}' where empId={}".format(empName, phone, empId)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated Employee Record")
        print()

    #Promote Employee
    def promote_emp(self, empId, post, salary):
        query = "update emp set post='{}', salary='{}' where empId={}".format(post, salary, empId)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Promoted Employee Record")
        print()

    #Delete Employee
    def delete_emp(self, empId):
        query="delete from emp where empId={}".format(empId)
        # print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()   #permanent delete from DB
        print("Employee deleted")
        print()
        return True

    #Search Employee
    def search_emp(self,empId):
        query = "select * from emp where empId={}".format(empId)
        cur = self.con.cursor()
        cur.execute(query)
        r = cur.fetchall()
        for row in r:
            print("Employee Name : ", row[1])
            print("Employee Phone No. : ", row[2])
            print("Employee Post : ", row[3])
            print("Employee Salary : ", row[4])
            print()
