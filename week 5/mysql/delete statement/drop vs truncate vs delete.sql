/* 
drop - you will lose everything
	-you won't be able to roll back to its initial state, or to the last commit statement
    -use when you're sure you aren't going to use the table anymore
    
truncate - removes all records in table
	-delete without where
    -when truncating, auto-increment values will be reset
    
delete - removes records row by row
	-only the rows corresponding to the where clause will be deleted
    -auto-increment values will not reset
