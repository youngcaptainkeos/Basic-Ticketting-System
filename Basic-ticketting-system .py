import mysql.connector
import tabulate
import csv
import random
import os
from datetime import date
import datetime
import calendar

cnx=mysql.connector.connect(user='root', password='sql123', host='localhost')

if cnx.is_connected():
    print("connection sucessful")


def change_connector_object():
    global cnx
    try:
        cnx=mysql.connector.connect(user='root', password='sql123', host='localhost', database='movie')
    except:
        create_database()



def create_database():
    objectcursor=cnx.cursor()
    objectcursor.execute("create database if not exists movie")
    change_connector_object()


# general functions


def create_table_client(id):
    global cnx
    cnx=mysql.connector.connect(user='root', password='sql123', host='localhost', database='movie')
    objectcursor=cnx.cursor()
    objectcursor.execute("""create table If not exists client(
        ID int NOT NULL AUTO_INCREMENT primary key,
        Username Varchar(200) NOT NULL,
        Password Varchar(200) NOT NULL  
    )""")
    if id!='Dry':
        admin(id)

def create_admin_table():
    global cnx
    cnx=mysql.connector.connect(user='root', password='sql123', host='localhost', database='movie')
    objectcursor=cnx.cursor()
    objectcursor.execute("""create table admin(
        ID int NOT NULL AUTO_INCREMENT primary key,
        Username Varchar(200) NOT NULL,
        Password Varchar(200) NOT NULL
    )""")
    objectcursor.execute("insert into admin(Username, Password) values('admin','admin')")
    cnx.commit()

def create_movie_table():
    global cnx
    cnx=mysql.connector.connect(user='root', password='sql123', host='localhost', database='movie')
    objectcursor=cnx.cursor()
    objectcursor.execute("""create table movie(
        ID int NOT NULL AUTO_INCREMENT primary key,
        Title Varchar(200) NOT NULL,
        Genre Varchar(200) null,
        Rating float null,
        ReleaseDate date null, 
        Price int NULL)""") 

def create_booking_table(id):
    f=open("booking.csv",'w')
    print("booking.csv file created")
    f.close()
    if id!='Dry':
        admin(id)

def dry_start():
    create_database()
    create_admin_table()
    id='Dry'
    create_table_client(id)
    print("client")
    create_movie_table()
    create_booking_table(id)
    main()


def login_client():
    global cnx
    username=input("Enter username: ")
    password=input("Enter password: ")
    objectcursor=cnx.cursor()
    objectcursor.execute('Select * from client')
    data = objectcursor.fetchall()
    c=0
    for i in data:
        if i[1]==username and i[2]==password:
            print(f"welcome {username} to SSPVR")
            c=1
            return i[0]
    if c!=1:
        print("Invalid username or password")
        client()


def login_admin():
    global cnx
    username=input("Enter username: ")
    password=input("Enter password: ")
    objectcursor=cnx.cursor()
    objectcursor.execute('Select * from admin')
    data = objectcursor.fetchall()
    c=0
    for i in data:
        if i[1]==username and i[2]==password:
            print(f"welcome {username} as admin in SSPVR")
            admin(i[0])
    if c!=1:
        print("Invalid username or password")
        main()



def register_client():
    global cnx
    username=input("enter a username you desire: ")
    password=input("enter a easy password: ")
    objectcursor=cnx.cursor()
    objectcursor.execute("insert into client(Username, Password) values('{}','{}')".format(username,password))
    cnx.commit()
    client()

#admin functions

def connect_to_database(id):
    global cnx
    cnx=mysql.connector.connect(user='root', password='sql123', host='localhost', database='movie')
    print("Connection established with database 'movie' ")
    admin(id)

def Remove_client(id):
    con = cnx.cursor()
    con.execute('Select * from client')
    data = con.fetchall()
    heading=["ID","Username","Password","Movie"]
    print(tabulate.tabulate(data, headers=heading))
    id1=input("Enter ID to delete: ")
    con.execute(f'delete from client where ID = {id1}')
    cnx.commit()
    con = cnx.cursor()
    con.execute('Select * from client')
    data = con.fetchall()
    heading=["ID","Username","Password","Movie"]
    print(tabulate.tabulate(data, headers=heading))
    admin(id)


def add_movie(id):
    while True:
        title=input('Title: ')
        genre=input('Genre: ')
        rating=float(input('Rating: '))
        timing=input('Release Date: ')
        price=int(input('Base price: '))
        objectcursor=cnx.cursor()
        objectcursor.execute("insert into movie(Title, Genre, Rating, ReleaseDate, Price) values('{}','{}',{},'{}',{})".format(title,genre,rating,timing,price))
        cnx.commit()
        k=input("Do you want to add one more? (y/n) ")
        if k.lower()=='n':
            admin(id)
        else:
            pass
        
def remove_movie(id):
    con = cnx.cursor()
    con.execute('Select * from movie')
    data = con.fetchall()
    heading=['Title', 'Genre', 'Rating', 'ReleaseDate', 'Price']
    print(tabulate.tabulate(data, headers=heading))
    id1=int(input("Enter Movie Id to delete: "))
    con.execute(f'delete from movie where ID = {id1}')
    cnx.commit()
    con = cnx.cursor()
    con.execute('Select * from movie')
    data = con.fetchall()
    heading=['Title', 'Genre', 'Rating', 'ReleaseDate', 'Price']
    print(tabulate.tabulate(data, headers=heading))
    admin(id)

def view_client_table(n):
    con = cnx.cursor()
    con.execute('Select * from client')
    data = con.fetchall()
    heading=["ID","Username","Password"]
    print(tabulate.tabulate(data, headers=heading))
    admin(n)

def disp_finance(id):
    f=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f)
    sum=sum_tickets=normal=ultra=ultra_pro=0
    for i in csvreader:
        sum+=int(i[7])
        sum_tickets+=int(i[5])
        if i[6]=="Normal":
            normal+=int(i[5])
        if i[6]=="Ultra":
            ultra+=int(i[5])
        if i[6]=="Ultra Pro":
            ultra_pro+=int(i[5])

    print(f"""
** Total Revenue :               {sum} {' '*(30-len(str(sum)))}**
** Total Seats Booked :          {sum_tickets} {' '*(30-len(str(sum_tickets)))}**
** Number of Normal seats :      {normal} {' '*(30-len(str(normal)))}**
** Number of Ultra seats :       {ultra} {' '*(30-len(str(ultra)))}**
** NUmber of Ultra Pro seats :   {ultra_pro} {' '*(30-len(str(ultra_pro)))}**
""")

    f.close()
    admin(id)

# client

def view_movies_booking():
    con = cnx.cursor()
    con.execute('Select * from movie')
    data = con.fetchall()
    heading=['Id','Title', 'Genre', 'Rating', 'ReleaseDate', 'Price']
    print(tabulate.tabulate(data, headers=heading))

def view_movies(id,m):
    con = cnx.cursor()
    con.execute('Select * from movie')
    data = con.fetchall()
    heading=['Id','Title', 'Genre', 'Rating', 'ReleaseDate', 'Price']
    print(tabulate.tabulate(data, headers=heading))
    if m==1:
        admin(id)
    if m==2:
        client_logged(id)
    else:
        print('invalid details')

def book_ticket(id):
    view_movies_booking()
    con = cnx.cursor()
    
    con.execute('Select * from movie')
    data = con.fetchall()
    f=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f)
    k=random.randint(1000,9999)
    movie_id=int(input("Enter Movie Id to book: "))
    c=0
    while c==0:
        for i in range(len(data)):
            if movie_id==data[i][0]:
                c=1
                movie_name=data[i][1]
                print("movie name:",movie_name)
                index=i
        if c==0:
            print('Ínvalid Choice')     
            movie_id=int(input("Enter Movie Id to book: "))
    l=[]
    print("Please enter a day after",date.today())
    y=int(input("choose preferable year (4 digits): "))
    m=int(input("enter choice of month (2 digits): "))
    cal = calendar.monthcalendar(y, m)
    print("\nSelect a date from the calendar:")
    print(calendar.month_name[m], y)
    print("Mon Tue Wed Thu Fri Sat Sun")
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                print(f" {day:2}", end="")
        print()
    d=int(input("enter choice of date (2 digit): "))
    try:
        datetime.date(y,m,d)
        if (datetime.date(y,m,d)>date.today()):
            print("Your Chosen date is: ",str(d)+'/'+str(m)+'/'+str(y))
            day=str(d)+'/'+str(m)+'/'+str(y)
        else:
            while True:
                print("Please enter a day after",date.today())
                y=int(input("choose preferable year (4 digits): "))
                m=int(input("enter choice of month (2 digits): "))
                cal = calendar.monthcalendar(y, m)
                print("\nSelect a date from the calendar:")
                print(calendar.month_name[m], y)
                print("Mon Tue Wed Thu Fri Sat Sun")
    
                for week in cal:
                    for day in week:
                        if day == 0:
                            print("   ", end="")
                        else:
                            print(f" {day:2}", end="")
                    print()
                d=int(input("enter choice of date (2 digit): "))
                if (datetime.date(y,m,d)>date.today()):
                    print("Your Chosen date is: ",str(d)+'/'+str(m)+'/'+str(y))
                    day=str(d)+'/'+str(m)+'/'+str(y)
                    break
    except ValueError:
            print("\nValues entered are non-existent \n")
            while True:
                print("Please enter a day after",date.today())
                y=int(input("choose preferable year (4 digits): "))
                m=int(input("enter choice of month (2 digits): "))
                cal = calendar.monthcalendar(y, m)
                print("\nSelect a date from the calendar:")
                print(calendar.month_name[m], y)
                print("Mon Tue Wed Thu Fri Sat Sun")
    
                for week in cal:
                    for day in week:
                        if day == 0:
                            print("   ", end="")
                        else:
                            print(f" {day:2}", end="")
                    print()
                d=int(input("enter choice of date (2 digit): "))
                if (datetime.date(y,m,d)>date.today()):
                    print("Your Chosen date is: ",str(d)+'/'+str(m)+'/'+str(y))
                    day=str(d)+'/'+str(m)+'/'+str(y)
                    break

    timings=float(input("prefered timings in 24 hour format: "))
    while timings>=24 or timings<0:
        print("Invalid timings")
        timings=float(input("prefered timings in 24 hour format: "))

    f=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f)
    seats_occupied=0
    for i in csvreader:
        if i[2]==movie_name and  str(i[3])==day and float(i[4])==timings:
            seats_occupied+=int(i[5])
            print(seats_occupied)
    if seats_occupied==50:
        print("HOUSE FULL!!! Try Another Time")
        client_logged(id)
    print("Total seats in theater = 50")
    print(f"Total seats available = {50-seats_occupied}")        
    f.close()

    no_seats=int(input("Enter no of seats: "))

    while no_seats<0 or no_seats>50-seats_occupied:
        print("Invalid number of seats")
        no_seats=int(input("Please enter again: "))
    seat=int(input("""select
    no. seat type       Price
    1.  Normal          $--
    2.  Ultra           $50
    3.  Ultra Pro       $100
    please select seat type: """))
    while seat not in [1,2,3]:
        print('invalid seats')
        seat=int(input("""select
    no. seat type       Price
    1.  Normal          $--
    2.  Ultra           $50
    3.  Ultra Pro       $100
    """))
    if seat==1:
        seat='Normal'
        price=data[index][5]*no_seats
    if seat==2:
        seat='Ultra'
        price=(data[index][5]+50)*no_seats
    if seat==3:
        seat='Ultra Pro'
        price=(data[index][5]+100)*no_seats
    list=[k,id,data[index][1],day,timings,no_seats,seat,price]
    print(f"""
{'*'*(66)}
{'*'*(66)}
**                             SSPVR                            **                                            
**                                                              **              
**                      Your Local Theater                      **              
** _____________________________________________________________**
** Reference ID :               {k} {' '*(30-len(str(k)))} **
** Client ID :                  {id} {' '*(30-len(str(id)))} **
** Movie Name :                 {data[index][1]} {' '*(30-len(str(data[index][1])))} **
** Date :                       {day} {' '*(30-len(str(day)))} **
** Timings :                    {timings} {' '*(30-len(str(timings)))} **
** {' '*(60)} **
** _______________________________________________________________
** Number of Seats :            {no_seats} {' '*(30-len(str(no_seats)))} **
** Price per seat :             {int(price)/int(no_seats)} {' '*(30-len(str(int(price)/int(no_seats))))} **
** Type of seat :               {seat} {' '*(30-len(str(seat)))} **
** Total Price :                {price} {' '*(30-len(str(price)))} **
{'*'*(66)}
{'*'*(66)}""")
    ans=input("Is this information correct? (Y/N): ")
    if ans.capitalize()=='Y':
        f=open("booking.csv",'a+')
        csvobject=csv.writer(f)
        csvobject.writerow(list)
        f.close()
        print("TICKET HAS BEEN BOOKED, THANK YOU")
        client_logged(id)
    if ans.capitalize()=="N":
        print("Please book the ticket again")
        client_logged(id)


        

def cancel_booking(id):
    f=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f)
    id1=str(id)
    k=1
    for i in csvreader:
        if i[1]==id1:
            print('Sl no.',k)
            print(f"""
{'*'*(66)}
{'*'*(66)}         
** _____________________________________________________________**
** Reference ID :               {i[0]} {' '*(30-len(i[0]))} **
** Movie Name :                 {i[2]} {' '*(30-len(i[2]))} **
** Date :                       {i[3]} {' '*(30-len(i[3]))} **
** Timings :                    {i[4]} {' '*(30-len(i[4]))} **
** {' '*(60)} **
** _______________________________________________________________
** Number of Seats :            {i[5]} {' '*(30-len(i[5]))} **
** Price per seat :             {int(i[7])/int(i[5])} {' '*(30-len(str(int(i[7])/int(i[5]))))} **
** Type of seat :               {i[6]} {' '*(30-len(i[6]))} **
** Total Price :                {i[7]} {' '*(30-len(i[7]))} **
{'*'*(66)}
{'*'*(66)}""")
            k+=1
    if k==1:
        print("Please make a purchase first!")
        client_logged(id)
    ref_id=input("Enter Reference Id of booking to cancel: ")
    print("")
    print(ref_id, "Has been Deleted")
    f.close()
    f=open('booking1.csv','w')
    csvwriter=csv.writer(f)
    f1=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f1)
    for i in csvreader:
        if i[0]!=ref_id:
            csvwriter.writerow(i)
    f.close()
    f1.close()
    os.remove('booking.csv')
    os.rename('booking1.csv','booking.csv')
    client_logged(id)


def view_booking(id):
    f=open("booking.csv",'r',newline='\r\n')
    csvreader=csv.reader(f)
    id1=str(id)
    k=1
    c=0
    for i in csvreader:
        if i[1]==id1:
            print('Sl no.',k)
            temp=int(i[7])/int(i[5])
            c=1
            print(f"""
{'*'*(67)}
{'*'*(67)}
**                  SSPVR                                       **                                            
**                                                              **              
**              Your Local Theater                              **              
** _____________________________________________________________**
** Reference ID :               {i[0]} {' '*(30-len(i[0]))} **
** Movie Name :                 {i[2]} {' '*(30-len(i[2]))} **
** Date :                       {i[3]} {' '*(30-len(i[3]))} **
** Timings :                    {i[4]} {' '*(30-len(i[4]))} **
** {' '*(60)} **
** _______________________________________________________________
** Number of Seats :            {i[5]} {' '*(30-len(i[5]))} **
** Price per seat :             {int(i[7])/int(i[5])} {' '*(30-len(str(int(i[7])/int(i[5]))))} **
** Type of seat :               {i[6]} {' '*(30-len(i[6]))} **
** Total Price :                {i[7]} {' '*(30-len(i[7]))} **
{'*'*(67)}
{'*'*(67)}""")
            k+=1
    f.close()
    if c==0:
        print("""
**                   Please Make a purchase FIRST!              **
**                                                              **                                            
**______________________________________________________________**
          
          """)

    client_logged(id)
    



def admin(id):
    print("""
**                   What would you like to do TODAY?           **
**                                                              **                                            
**    1.  Connect To database                                   **
**    2.  View clients list                                     **
**    3.  Create client table                                   **
**    4.  Create movie table                                    **
**    5.  Add Movie details                                     **
**    6.  Remove Movies                                         **
**    7.  View Movies                                           **
**    8.  Create Booking CSV file                               **
**    9.  View Finances                                         **
**   10.  Remove client                                         **
**   11.  Back                                                  **
**______________________________________________________________**
""")

    k=int(input(" Enter : "))
    while k not in [1,2,3,4,5,6,7,8,9,10,11]:
        k=int(input("Please enter a valid answer: "))
    if k==1:
        connect_to_database(id)
    if k==2:
        view_client_table(id)
    if k==3:
        create_table_client(id)
    if k==4:
        create_movie_table(id)
    if k==5:
        add_movie(id)
    if k==7:
        admin_lock=1
        view_movies(id,admin_lock)
    if k==6:
        remove_movie(id)
    if k==8:
        create_booking_table(id)
    if k==9:
        disp_finance(id)
    if k==10:
        Remove_client(id)
    if k==11:
        main()

def client_logged(client_id):
    print("""
**                 What would you like to do TODAY?             **
**                                                              **                                            
**                1. Purchase Ticket                            **
**                2. View movies                                **
**                3. Review purchases                           **
**                4. Cancel Ticket                              **
**                5. Back                                       **
**______________________________________________________________**
          
          """)

    k=int(input(" Enter : "))
    while k not in [1,2,3,4,5]:
        k=int(input("Please enter a valid answer: "))
    if k==1:
        book_ticket(client_id)
    if k==2:
        m=2
        view_movies(client_id,m)
    if k==3:
        view_booking(client_id)
    if k==4:
        cancel_booking(client_id)    
    if k==7:
        pass    
    if k==6:
        pass
    if k==5:
        client()

def client():
    print("""
**                1. Register                                 **
**                2. Login                                    **
**                3. Back                                     **
**____________________________________________________________**
""")

    k=int(input(" Enter : "))
    while k not in [1,2,3]:
        k=int(input("Please enter a valid answer: "))
    if k==1:
        register_client()
    if k==2:
        client_id=login_client()
        client_logged(client_id)
    if k==3:
        main()

def main():
    print("""
**                  Welcome TO                      **
**                    SSPVR                         **                                            
**                                                  **              
**               Your Local Theater                 **              
** _________________________________________________**
**                    MENU                          **
**                1. Purchse Ticket                 **
**                2. Admin Controls                 **
**                3. Exit Program                   **
**                4. Dry Run                        **
**__________________________________________________**
          
          """)
    k=int(input(" Enter : "))
    if k==1:
        change_connector_object()
        client()
    if k==2:
        change_connector_object()
        login_admin()
    if k==3:
        quit()
    if k==4:
        dry_start()

main()