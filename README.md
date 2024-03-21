# Academic Advisor Database Management System

This simple database management system is designed to facilitate the management of academic advisors and their assigned students within an educational institution. Built with SQLite3, it offers a straightforward approach to creating and populating tables for advisors, students, and their relationships.

## Features

- Advisor Management: Allows for the creation of advisor records, including their unique IDs and names.
- Student Management: Facilitates the creation of student records, capturing their unique IDs and names.
- Advisor-Student Relationships: Supports the association of students with their academic advisors, maintaining a clear record of which student is advised by which faculty member.
- Data Retrieval: Includes functionality to retrieve and display the relationships between students and their advisors, making it easy to see who advises whom.

## How to Use

### Prerequisites: Ensure you have Python and SQLite3 installed on your system.

- Database Connection: The script automatically connects to an SQLite3 database named sqlite3.db located one directory above the script's folder. Ensure this database exists or adjust the path as needed.

- Creating and Populating Tables: The script initially creates three tables if they do not already exist: Advisor, Student, and StudentAdvisor. It then populates the Advisor and Student tables with initial data.

- Establishing Relationships: After creating and populating the advisor and student tables, the script establishes relationships between students and their advisors by populating the StudentAdvisor table.

- Retrieving Data: The script includes a query to retrieve and print the names of students along with their advisors, showcasing the relationships established in the previous step.

- Committing Changes: Changes made to the database are committed, ensuring that the database is updated with the new tables, records, and relationships.

- Closing the Connection: Finally, the script closes the connection to the database to ensure no resources are left hanging.

## Example Usage

After running the script, it will output the relationships between students and their advisors based on the initial data provided. This output is intended to demonstrate the successful creation and population of the database tables and the establishment of relationships between students and advisors.

## Customization

- Modifying Initial Data: The initial data inserted into the Advisor and Student tables can be customized by modifying the INSERT INTO statements within the script.
- Adding More Relationships: Additional relationships can be established by inserting more records into the StudentAdvisor table
