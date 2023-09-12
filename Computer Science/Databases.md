## Definitions

* Database 
    - an organized persistent store of information of records pertaining to an individual data item or collection of data

* Entity (aka Database Table)
     - a collection of related fields or attributes relating to a real world object eg. customers, members cars

* Attribute 
    - A single unit of storage / field in a Entity

* Record 
    - A collection of related attributes pertaining to a subject

* Primary Key
	    - A unique identifier for each record in a Database entity

* Flat file database 
    - A database consisting of just one entity with a large number of attributes.
	- Problems Include:
		- Very long access time
		- Large memory usage to hold in RAM
		- No possible access levels for individual data items
		- Data Redundancy (repeated data)
		- Data Consistency (Data is inconsistent across the database eg. multiple spellings)

* Foreign Key
    - A primary key for an entity appearing in an entity that it does not belong to

* Relational Database
    - Consists of more than one entity where the attributes within are linked via foreign keys. 

* Normalization 
    - The Process of structuring the database entities. The aim of normalization is to ensure that the data structure is optimized 
	    > (No repeating attributes, Data is consistent, Attributes held within the entity are dependent on the primary key)
	- There are 3 stages to database normalization called 'normal form'

- Referential Integrity
	- A programmable set of relationships that maintain the integrity and consistency of data items across the database.
	- This ensures that when records are created, updated or removed, related records are dealt with properly. This may include deleting orphaned records.

## Normalization

Database normalization is the process of structuring entities and attributes in the most efficient and optimized way.  
Data structures should not have long access times. There should also be no data duplication or redundancy

* Data consistency
    - When data is entered, it is entered just once and is always consistent
    - Database normalization takes an entity from a flat file database consisting of one large entity with many attributes
to a relational database liked by foreign keys where each attribute therein is dependant on the key, and nothing else.
(so help me Codd)

Database normalization consists of 3 different stages
an entity is in 1st normal form if it contains no repeating attributes or groups of attributes

- eliminate duplicate columns
- create separate entities for each group of related data
- identify a field within

### Nature of database relationships
- one-to-one : one person may only have a relationship with one other person
- one-to-many : one teacher may teach many pupils
- many-to-many : many courses having many pupils each

1. First normal form
    - There must be no repeated attributes of groups of attributes

2. Second normal from
    - Must be in 1NF and contains only partial key dependency (some links are made without the use of keys)

3. Third normal form
    - Must be in 1NF and contains no key dependencies (all links between records are made with keys)

#### Standard Notation
>TableName(<u>PrimaryKey</u>, <span style = "text-decoration:overline">ForeignKey</span>, DataAttribute)  

#### Entity relationship Modelling 
>object ------------- object		one-to-one		(simple)  
   object ------------< object		one-to-many		(good)  
   object >-----------< object     many-to-many	(bad)

Database integrity is the process of ensuring records held in databases are consistent and held in place.
Any changes made to the database / data structure is made of entire records.
When data and records are updated or deleted, the entire record is altered. 
There should be no residual of data records are left in the database. In relational databases, there should be no references to unused foreign keys.

Relational databases in large organizations are accessed by many users. Therefore, keeping data consistent is important these are accessible through database management systems. These are the software that gives users the rights to access and view data at certain levels

### Transaction processing
- There are four different types of processing that takes place:
	- CRUD 
		- Create a database entity
		- Read (Query the database for data)
		- Update the database's records
		- Delete records from the database

	- Pass By Value
        - A read-only copy of the value is passed. No changes are made to the original. (**Returns a TUPLE - Immutable Array**)
		
	- Pass By Reference
		- A pointer to the original is passed. Changes may be made to the original.

		- ACID (All database structures and records must follow these principles - they help maintain the integrity of database structures)
		    - ***A***tomicity (A change to a record in the database is performed entirely, or not at all.)
			- ***C***onsistency (A change to the database must maintain the overall structure of the database)
			- ***I***solation (Records that are currently being accessed are locked during the period of transaction (basic async. / race condition stuff - called a MUTEX / lock) - the lock is removed after the transaction has taken place)
			- ***D***urability (Once a change has been made, it cannot be lost due to system failure. Transactions are updated in real-time and must be written to permanent secondary storage.)
			  