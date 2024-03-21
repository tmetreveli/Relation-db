import sqlite3


conn = sqlite3.connect('../sqlite3.db')

# Create cursor object
cursor = conn.cursor()

# Create and populate tables
cursor.executescript(''' 
CREATE TABLE IF NOT EXISTS Advisor( 
AdvisorID INTEGER NOT NULL, 
AdvisorName TEXT NOT NULL, 
PRIMARY KEY(AdvisorID) 
); 

CREATE TABLE IF NOT EXISTS Student( 
StudentID NUMERIC NOT NULL, 
StudentName NUMERIC NOT NULL,  
PRIMARY KEY(StudentID) 
); 

CREATE TABLE IF NOT EXISTS StudentAdvisor( 
StudentID INTEGER NOT NULL,
AdvisorID INTEGER NOT NULL,
PRIMARY KEY(StudentID, AdvisorID),
FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID) 
); 

INSERT INTO Advisor (AdvisorID, AdvisorName) VALUES (1, 'Dr. Smith');
INSERT INTO Advisor (AdvisorID, AdvisorName) VALUES (2, 'Prof. Johnson');
INSERT INTO Advisor (AdvisorID, AdvisorName) VALUES (3, 'Dr. Williams');


INSERT INTO Student (StudentID, StudentName) VALUES (101, 'Alice Brown');
INSERT INTO Student (StudentID, StudentName) VALUES (102, 'Bob White');
INSERT INTO Student (StudentID, StudentName) VALUES (103, 'Charlie Green');
INSERT INTO Student (StudentID, StudentName) VALUES (104, 'Dana Black');

-- Alice and Bob -> Dr. Smith
INSERT INTO StudentAdvisor (StudentID, AdvisorID) VALUES (101, 1);
INSERT INTO StudentAdvisor (StudentID, AdvisorID) VALUES (102, 1);

-- Charlie -> Prof. Johnson and Dr. Williams
INSERT INTO StudentAdvisor (StudentID, AdvisorID) VALUES (103, 2);
INSERT INTO StudentAdvisor (StudentID, AdvisorID) VALUES (103, 3);

-- Dana -> Dr. Williams
INSERT INTO StudentAdvisor (StudentID, AdvisorID) VALUES (104, 3);


''')
cursor.execute("""
SELECT Student.StudentName, Advisor.AdvisorName
FROM Student
JOIN StudentAdvisor ON Student.StudentID = StudentAdvisor.StudentID
JOIN Advisor ON Advisor.AdvisorID = StudentAdvisor.AdvisorID;
""")
for row in cursor.fetchall():
    print(row)

# Commit changes to database
conn.commit()

# Closing the connection
conn.close()
