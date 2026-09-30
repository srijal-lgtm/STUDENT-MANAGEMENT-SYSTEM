Student Record Management System
A console-based Python application for creating, viewing, searching and deleting
By using a straightforward numbered menu.
Overview
Schools and colleges generally record students' information in paper form or in separate files.
This project provides a small, easy-to-use command-line tool that keeps student
records (ID, name, age and marks) in memory and lets the user manage them from a
It had a single menu and was designed as part of the VITyarthi 'Build Your Own Project' evaluation.
Features
To add a student, input their ID, name, age, and marks; the record will then be stored immediately.
List all the stored records or display a message if no records exist.
To search for a student, enter the student's ID and then show the complete record.
To delete a student — enter the ID and confirm the action with a yes/no question.
To exit, close the program properly.
The menu operates in a loop and displays a friendly message when invalid choices are made.
Technologies / Tools Used
Python 3 (standard library only - no external packages needed)
Git and GitHub for version control
Any Python 3 editor / online compiler / terminal to run the program
Project Structure
Steps to Install and Run
Get Python 3.8 or a later version from https://www.python.org/downloads/
Clone the repository:
git clone https://github.com//student-record-management.git
Move into the folder:
cd student-record-management
Run the program:
python main.py      (use python3 main.py on Linux or macOS)
Select an item from the menu by keying in its number (1-5) and then pressing Enter.
Sample Usage
Instructions for Testing
The program is manually tested by running main.py and carrying out these cases:
Start the program and the five-option menu should then appear.
Add a student (for example: 1897, Srijal, 18, 80). "Student added successfully!"
The list of students with no data shows 'No student records available'.
When you have added them, view the students — all the fields for each record are displayed.
Look up a current ID—'Student found!' together with the details.
Look up a missing ID — 'Student not found'.
To delete an existing ID you must type yes - "Record deleted successfully!".
To delete an existing ID, enter no - the deletion will then be cancelled.
Delete the ID that is missing - "Student not found".
If an invalid menu option is entered (for example, 9), then the message displayed is "Invalid choice. Please try again."
The program will stop and the exit message will be displayed.
Screenshots
�
Load image
Author
Srijal Binod Ojha  - 26BEC10099 - VIT
