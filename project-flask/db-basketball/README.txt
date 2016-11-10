SQL Source Instructions

setup.sh is a script to initialize the small set of sample data
into a database called basketball. 

It first runs create.sql which creates the tables and triggers
for the database.

It then runs load.sql which loads the sample data from the .dat 
files in the \data folder. The load.sql file also contains three
test insert queries (currently commented out) that test the 
trigger functionality.

test-sample.sql contains a set of sample queries to test out our
database.