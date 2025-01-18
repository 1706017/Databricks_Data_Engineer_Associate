##Using %run magic command to refer the other notebook from current notebook
==============================================================================

%run /Users/amritmanash9@gmail.com/reference
print(my_name)  #here the my_name is defined in the reference notebook as mentioned above



#Creation of Delta Lake Tables as we do not need to specify explicitly as delta as it is the default format
=============================================================================================================
%sql
CREATE TABLE employees(id INT,name STRING,salary DOUBLE);


#Now we will insert some records into our delta table using INSERT INTO VALUES() statement
===========================================================================================
%sql
INSERT INTO employees
VALUES
 (1,'Amrit',50000.0),
 (2,'Manash',40000.0),
 (3,'Nasim',60000.0),
 (4,'Ayush',70000.0),
 (5,'Kumar',50000.0);


#To Fetch all the records from a Delta table named employees
=============================================================
%sql
SELECT * FROM employees;



#To Know the meta data about the delta table named as employees
================================================================
%sql
DESCRIBE DETAIL employees;



#To Update the column of the employees table by adding 100 to the salary
=========================================================================
%sql
UPDATE employees
SET salary = salary + 100;



#To see all the changes that has happened on to the delta table we use HISTORY command
=======================================================================================
%sql
DESCRIBE HISTORY employees;



