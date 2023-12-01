#create a table - add at least one column, otherwise sql will display error

CREATE TABLE sales (
    purchase_number 	INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    date_of_purchase 	DATE NOT NULL,
    customer_id 		INT,
    item_code 			VARCHAR(10) NOT NULL
);

CREATE TABLE customers
(
	customer_id 			INT,
    first_name 				VARCHAR(255),
    last_name 				VARCHAR(255),
    email_address 			VARCHAR(255),
    number_of_complaints	INT
);