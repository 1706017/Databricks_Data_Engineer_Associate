#To see the changes that has been done till now on to the delta table
=======================================================================
%sql
CREATE TABLE student(id INT,name STRING,marks DOUBLE);

%sql
INSERT INTO student
VALUES
(1,'Amrit',75.5),
(2,'Manash',89.9),
(3,'Kumar',90),
(4,'Nasim',89.97),
(5,'Ayush',100);


%sql
UPDATE student 
SET marks = marks+10;


%sql
DESCRIBE HISTORY student;

#Using the timestamp to access the specific timestamp delta table
==================================================================
%sql
SELECT * FROM student TIMESTAMP AS OF '2025-01-18T13:47:11.000+00:00';

%sql
SELECT * FROM student TIMESTAMP AS OF '2025-01-18T13:45:08.000+00:00';


#Using the Version of delta lake table to access specifc version of delta lake table
=======================================================================================
%sql
SELECT * FROM student VERSION AS OF 1;

Output:
id	name	  marks
1	  Amrit 	75.5
2	  Manash	89.9
3	  Kumar	  90
4	  Nasim 	89.97
5	  Ayush	  100

%sql
SELECT * FROM student VERSION AS OF 2;

Output:
id	name  	marks
1	  Amrit	  85.5
2	  Manash	99.9
3	  Kumar 	100
4	  Nasim	  99.97
5	  Ayush 	110

#To Restore delta lake table to specific version if by mistake table is deleted
=================================================================================
%sql
DELETE FROM student;

%sql
SELECT * FROM student;

Output:
id name marks

%sql
RESTORE TABLE student TO VERSION AS OF 2;

%sql
SELECT * FROM student;

Output:
id	name	  marks
1	  Amrit	  85.5
2	  Manash	99.9
3	  Kumar	  100
4	  Nasim	  99.97
5	  Ayush	  110

#Compacting smaller files to create larger files with Zorder Indexing for faster reading
=========================================================================================
OPTIMIZE student 
ZORDER BY id;

#Vacuum a delta tables so as to remove the uncommited files and to remove the older version of delta tables
============================================================================================================
VACUUM student;










