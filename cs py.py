import mysql.connector
lib=mysql.connector.connect(host="localhost",user="root",password="root")
cursor=lib.cursor()

if (lib.is_connected()==True):
    print ("connected successfully to mysql database")

else:
    cursor.execute("create database if not exists library")
    cursor.execute("use library")
    cursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")


while True:
    print("1:Signup")
    print("2:Login")
    ch=int(input("enter your choice(SIGNUP/LOGIN(1,2))"))
    if(ch==1):
        username=input("enter USERNAME")
        pw=input("enter PASSWORD")
        cursor.execute(("insert into signup values('{}','{}')").format(username,pw))
        lib.commit()


    elif(ch==2):
        username=input("enter USERNAME")
        query=("select username from signup where username='{}'").format(username)
        cursor.execute(query)
        p=cursor.fetchone()
        if(p is not None):
            print("VALID USERNAME")
            pw=input("enter PASSWORD")
            cursor.execute(("select password from signup where password='{}'").format(pw))
            a=cursor.fetchone()
            if(a is not None):
                print("LOGIN SUCCESSFULL")

                print("******************** Library Record ********************")




                cursor.execute("create table if not exists book_rec(BookName varchar(30)primary key,AuthorName varchar(30),Genre varchar(20),Date-of-issue varchar(20),Publication varchar(30),Price int(5))")
                cursor.execute("create table if not exists stu_rec(studentName varchar(30),admissionnumber int(10) unique key, Patron varchar(30),BookName varchar(30) foreign key)")

                cursor.execute("create table if not exists fee_rec(studentName varchar(30) foreign key, date-of-borrow varchar(20),Amount paid int(3), fee due int(10)")
                lib.commit()

                while(True):
                    print("""1:Books Details
                             2:Student Details
                             3:Fee Record""")



                    c=int(input("Enter your choice"))


                    
                    if (c==1):
                        print("""1:New book entry
                                 2:Remove book record
                                 3:Search for a book entry""")
                        
                        s=int(input("Search by?"))

                        
                        #to add book
                        if (s==1):
                            Bookname=input("Enter Book Name")
                            AuthorName=input("Enter author name")
                            Genre=input("Enter the total number of pages of the book")
                            Date_of_issue=int(input("Enter the date when book was issued"))
                            publication=input("Enter the name of the publication house")
                            Price=int(input("Enter the price"))
                            cursor.execute(("SELECT*FROM book_rec WHERE bookname='{}'").format(Bookname))
                            r=cursor.fetchone()
                            print("****SUCCESSFULLY ADDED****")



                        #to delete books 
                        elif(s==2):
                            d=input("Enter book name to remove")
                            cursor.execute(("SELECT name FROM book_rec WHERE name='{}'").format(d))
                            o=cursor.fetchone()
                            if(o is not None):
                                cursor.execute(("DELETE from book_rec WHERE name='{}'").format(d))
                                print("****BOOK RECORD IS SUCCESSFULLY REMOVED****")
                                lib.commit()
                            else:
                                print("****BOOK DOESNOT EXIST****")

                                


                        #to search books
                        elif(s==3):
                            print("""1:Search by name
                                 2:Search by genre
                                 3:Search by author""")
                        
                            j=int(input("Search by?"))

                            

                            
                            #by name of book
                            if(j==1):
                                o=input("Enter Book to search")
                                cursor.execute(("SELECT BookName FROM book_rec WHERE BookName='{}'").format(o))
                                b=cursor.fetchone()
                                if(b!=None):
                                    print("****BOOK IS IN RECORD****")
                                else:
                                    print("****BOOK IS NOT IN RECORD****")



                            #by genre of book

                            elif(j==2):
                                o=input("Enter Book to search")
                                cursor.execute(("SELECT Genre FROM book_rec WHERE Genre='{}'").format(o))
                                b=cursor.fetchone()
                                if(b!=None):
                                    print("****BOOK IS IN RECORD****")
                                else:
                                    print("****BOOK IS NOT IN RECORD****")

                            
                                    

                        
                           #by name of author

                                    
                            else:
                                o=input("Enter Book to search")
                                cursor.execute(("SELECT AuthorName FROM book_rec WHERE AuthorName='{}'").format(o))
                                b=cursor.fetchone()
                                if(b!=None):
                                    print("****BOOK IS IN RECORD****")
                                else:
                                    print("****BOOK IS NOT IN RECORD****")




                                    


                    if c==2:
                        print("""1.add student record
                                 2.delete student record
                                 3.search student record""")
                        a=int(input("search by?"))

                            
                            #to add record
                        if a==1:
                            studentName=input("enter student name:")
                            admissionnumber=int(input("enter the admission number"))
                            Patron=input("enter class and section")
                            cursor.execute(("SELECT*FROM student_rec WHERE studentname='{}'").format(studentName))
                            r=cursor.fetchone()
                            print("****SUCCESSFULLY ADDED****")

                                
                            #to delete record

                        elif(a==2):
                            w=input("Enter student name to remove")
                            cursor.execute(("SELECT name FROM student_rec WHERE name='{}'").format(w))
                            o=cursor.fetchone()
                            if(o is not None):
                                cursor.execute(("DELETE from student_rec WHERE name='{}'").format(w))
                                print("****STUDENT RECORD IS SUCCESSFULLY REMOVED****")
                                lib.commit()

                            else:
                                print("****RECORD DOESNOT EXIST****")


                            #to search record
                        else:
                            o=input("Enter student record to search")
                            cursor.execute(("SELECT studentName FROM student_rec WHERE studentName='{}'").format(o))
                            b=cursor.fetchone()
                            if(b!=None):
                                print("****STUDENT IS IN RECORD****")
                            else:
                                print("****STUDENT IS NOT IN RECORD****")



                    if c==3:
                        print("""1.add record
                                 2.search  record
                                 3.delete record""")
                        t=int(input("enter choice"))
                        if t==1:
              #add record
                            name_of_borrower=input("enter name of the student who has borrowed the book")
                            date_of_borrowing=int(input("enter the date"))
                            amount_paid=int(input("enter the amount paid"))
                            late_return_fine=int(input("enter the fine"))
                            cursor.execute(("SELECT*FROM fee_rec WHERE borrower_name='{}'").format(borrowername))
                            r=cursor.fetchone()
                            print("****SUCCESSFULLY ADDED****")


                        if t==2:
              #search record
                            o=input("enter fee  record to search")
                            cursor.execute(("SELECT borrowerName FROM fee_rec WHERE borrowerName='{}'").format(o))
                            b=cursor.fetchone()
                            if(b!=None):
                                print("****BORROWER IS IN RECORD****")

                            else:
                                print("****BORROWER IS NOT IN RECORD****")

                        if t==3:
                             
             #delete record
                            g=input("Enter record to remove")
                            cursor.execute(("SELECT name FROM fee_rec WHERE borrowername='{}'").format(g))
                            o=cursor.fetchone()
                            if(o is not None):
                                cursor.execute(("DELETE from fee_rec WHERE name='{}'").format(g))
                                print("**** RECORD IS SUCCESSFULLY REMOVED****")
                                lib.commit()
                            else:
                                print("****RECORD DOESNOT EXIST****")
            else:
                print("PASSWORD INCORRECT")


        else:
            print("invalid username")


    else:
        break
    