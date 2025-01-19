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
col_name	data_type	comment
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
Table Properties	[delta.minReaderVersion=1,delta.minWriterVersion=2]	


