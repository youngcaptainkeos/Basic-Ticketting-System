# Basic-Ticketting-System

Admin Functions: 
1. Connect to Database 
Function Header: connect_to_database(id) 
Description: This function establishes a connection to the 
database named 'movie'. It prints a message confirming the 
successful connection and redirects to the admin panel. 
Backend Action: Establishes a connection to the 'movie' 
database by utilizing the mysql.connector.connect() function. It 
confirms the successful connection and redirects to the admin 
panel. 
2. View Clients List 
Function Header: view_client_table(n) 
Description: This function retrieves and displays the list of 
clients in a tabular format. It provides details such as ID, 
Username, and Password. 
Backend Action: Executes an SQL query to fetch all client 
details from the 'client' table. Displays the retrieved data in a 
tabular format using the tabulate library. 
3. Create Client Table 
Function Header: create_table_client(id) 

 
Description: This function creates a table named 'client' within 
the 'movie' database. It includes columns for ID, Username, and 
Password. Additionally, it creates an admin account if the 
function is executed with a non-'Dry' parameter. 
Backend Action: Executes an SQL query to create a table 
named 'client' within the 'movie' database. 
4. Create Movie Table 
Function Header: create_movie_table() 
Description: This function creates a table named 'movie' within 
the 'movie' database. It includes columns for Movie ID, Title, 
Genre, Rating, Release Date, and Price. 
Backend Action: Executes an SQL query to create a table 
named 'movie' within the 'movie' database. 
5. Add Movie Details 
Function Header: add_movie(id) 
Description: Allows an admin to input movie details such as 
Title, Genre, Rating, Release Date, and Price. The function 
inserts this information into the 'movie' table. 
Backend Action: Takes user input for movie details and inserts 
this information into the 'movie' table using SQL INSERT 
queries. 

 
6. Remove Movies 
Function Header: remove_movie(id) 
Description: Enables the removal of movies by displaying the 
existing movies' details in a tabular format and prompts the 
admin to enter the Movie ID for deletion. 
Backend Action: Displays existing movie details in a tabular 
format, prompts the admin to select a Movie ID for deletion, 
and executes an SQL DELETE query to remove the selected 
movie from the 'movie' table. 
7. View Movies 
Function Header: view_movies(id, admin_lock) 
Description: Presents the list of movies available in a tabular 
format. The function is accessible both by admins and clients. 
Backend Action: Retrieves movie details from the 'movie' table 
using an SQL query and displays the information in a tabular 
format using the tabulate library. Accessible to both admins 
and clients. 
8. Create Booking CSV File 
Function Header: create_booking_table(id) 
Description: Creates a CSV file named 'booking.csv'. If executed 
with a non-'Dry' parameter, it also initiates an admin session. 

 
Which creates a CSV file which stores all the previous booking 
transactions. 
Backend Action: Creates a CSV file named 'booking.csv to store 
booking details. Using CSV module. 
9. View Finances 
Function Header: disp_finance(id) 
Description: Displays financial statistics such as total revenue, 
total seats booked, and the number of seats booked for 
different seat types (Normal, Ultra, Ultra Pro). 
Backend Action: Reads data from the 'booking.csv' file, 
calculates and displays financial statistics like total revenue, 
total seats booked, and seats booked for different types 
(Normal, Ultra, Ultra Pro). 
10. Remove Client 
Function Header: Remove_client(id) 
Description: Facilitates the removal of a client from the 'client' 
table. It displays client details and prompts the admin to enter 
the ID of the client to be deleted. 
Backend Action: Executes an SQL DELETE query to remove the 
selected client from the 'client' table. 
11. Back 

 
Description: Returns the user to the main menu. 
This overview should provide you with an understanding of 
each admin function's purpose and functionality. 
 
Client / User functions: 
1. Register 
Function Header: register_client() 
Description: Allows a new user to register by inputting a 
desired username and password. It inserts this information 
into the 'client' table. 
Backend Action: Takes user input for username and password, 
then executes an SQL INSERT query to add this information 
into the 'client' table. 
2. Login 
Function Header: login_client() 
Description: Facilitates user login by verifying the entered 
username and password against the 'client' table. Upon 
successful login, it welcomes the user to SSPVR. 
Backend Action: Fetches all client details from the 'client' table 
and verifies the entered username and password. Upon 
successful validation, grants access to the SSPVR system. 

 
3. Purchase Ticket 
Function Header: book_ticket(id) 
Description: Allows a logged-in user to book tickets by 
selecting a movie, date, timing, number of seats, and seat type. 
It calculates the price and generates a reference ID for the 
booking. 
Backend Action: Allows the user to select movie, date, timings, 
seat type, and number of seats. Calculates the price and 
generates a reference ID for the booking. Writes this booking 
information to the 'booking.csv' file. 
4. View Movies 
Function Header: view_movies(client_id, m) 
Description: Presents the list of movies available in a tabular 
format. This function is accessible for both admins and clients. 
Backend Action: Retrieves movie details from the 'movie' table 
and displays the information in a tabular format. 
5. Review Purchases 
Function Header: view_booking(id) 
Description: Displays the user's booking history, including 
details like reference ID, movie name, date, timings, seat type, 
and total price. 

 
Backend Action: Fetches booking history for the logged-in user 
from the 'booking.csv' file and displays it in a tabular format. 
6. Cancel Ticket 
Function Header: cancel_booking(id) 
Description: Allows a user to cancel a booking by entering the 
reference ID of the booking they wish to cancel. 
Backend Action: Allows the user to cancel a specific booking 
by entering the reference ID. Updates the 'booking.csv' file by 
removing the cancelled booking. 
7. Back 
Description: Provides an option to return to the previous menu. 
 

 
 
Modules and Functions Used  
 
 
 
Modules: 
1. mysql.connector 
This module enables connectivity and interaction with a MySQL 
database. It allows the program to establish connections to the 
local MySQL server and executes SQL queries, and perform 
database related operations like creating tables, inserting 
data, and retrieving information. 
 
2. tabulate 
The tabulate module facilitates the presentation of data in a 
tabular format. It's utilized to neatly display fetched data from 
the database (such as client lists, movie details) in a 
structured and visually appealing manner. 
 
3. csv 
 
The csv module assists in reading from and writing to CSV 
(Comma-Separated Values) files. In this context, it's used to 
manage a file named 'booking.csv', storing booking information 
including reference IDs, movie details, dates, timings, seat 
types, and prices. 
 
4. random 
The random module provides functionalities to generate 
random numbers. Within the program, it's employed to create a 
unique reference ID for each booking made by a user. 
 
5. os 
The os module provides a way to interact with the operating 
system. In this program, it's used to perform file-related 
operations such as renaming and removing files. For instance, 
when canceling a ticket, it renames and removes entries in the 
'booking.csv' file. 
 
6. datetime and calendar 
These modules handle date and time-related operations. They 
enable the program to manage dates for booking tickets, 

 
ensuring that bookings can only be made for future dates and 
providing a calendar view for date selection. 
 
Key Functions: 
Book_ticket(id): 
The booking function lets users reserve movie tickets by 
picking the movie, date, timing, seat type, and number of seats. 
It calculates the total cost and gives a unique booking ID. It 
helps users by showing a calendar for date selection and 
checking seat availability for future dates. While choosing the 
dates it shows a calendar of the month to help customers 
choose the right dates. If someone enters wrong details, like 
too many seats or an invalid date, the system guides them to 
fix it. It uses clear instructions and checks to make sure users 
enter the right info, like valid timings and future dates, to avoid 
mistakes. Overall, it's made to be easy to use and helps users 
avoid errors while booking tickets. 
 
Dry_start(): 
The "dry start" function serves as a setup tool, creating the 
initial database structure and essential tables like client, 
admin, movie, and booking. It's particularly useful during the 
 
system's first launch or when starting from scratch, setting up 
the entire database and necessary tables without existing data. 
This always the system to be initialized without any admin’s 
inputs. This creates a clean environment, ensuring all 
essential tables are in place and ready for use. During a "dry 
start," it establishes the database, creates admin and client 
tables, initializes an admin account, sets up the movie table 
structure, and prepares the booking CSV file for future use. 
This function streamlines the initial setup process, ensuring 
the system is ready to handle user registrations, movie details, 
and ticket bookings right from the start.
