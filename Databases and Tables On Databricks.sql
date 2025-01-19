--Creation of managed table in default database in hive metastore
=================================================================
CREATE TABLE managed_default
(width INT,length INT,height INT);

INSERT INTO managed_default 
VALUES
  (12,10,11);

-- To know the metadata about the table 
========================================
DESCRIBE EXTENDED managed_default;

--Output:
/*col_name	data_type	comment
width	int	null
length	int	null
height	int	null
		
# Detailed Table Information		
Catalog	  spark_catalog	
Database	default	
Table	    managed_default	
Created Time	Sun Jan 19 04:46:47 UTC 2025	
Last Access	UNKNOWN	
Created By	Spark 3.3.2	
Type	MANAGED	
Location	dbfs:/user/hive/warehouse/managed_default	
Provider	delta	
Owner	root	
Is_managed_location	true	
Table Properties	[delta.minReaderVersion=1,delta.minWriterVersion=2]	*/

--Creation of External Table using LOCATION keyword
====================================================
CREATE TABLE external_default
(width INT,length INT,height INT)
LOCATION 'dbfs:/mnt/demo/external_default';

INSERT INTO external_default
VALUES
(12,56,89)

DESCRIBE EXTENDED external_default;
--Output:
/*col_name	data_type	comment
width	int	null
length	int	null
height	int	null
		
# Detailed Table Information		
Catalog	spark_catalog	
Database	default	
Table	external_default	
Created Time	Sun Jan 19 05:11:55 UTC 2025	
Last Access	UNKNOWN	
Created By	Spark 3.3.2	
Type	EXTERNAL	
Location	dbfs:/mnt/demo/external_default	
Provider	delta	
Owner	root	
Table Properties	[delta.minReaderVersion=1,delta.minWriterVersion=2]	*/

--Creation of New database apart from default database
=======================================================
CREATE DATABASE new_default;

--Creation of Managed Table Inside a new database created Apart from default database in Hive Metastore
========================================================================================================
USE new_default;

CREATE TABLE new_managed_table
(id INT,name STRING);

INSERT INTO new_managed_table
VALUES
(1,'Amrit'),
(2,'Manash');





