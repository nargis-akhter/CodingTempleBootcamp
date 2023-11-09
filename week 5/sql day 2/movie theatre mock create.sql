CREATE TABLE IF NOT EXISTS customer(
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
email_id VARCHAR(150),
phone_no VARCHAR(15)
);

-- Concession Table Creation
CREATE TABLE IF NOT EXISTS concession(
c_id SERIAL PRIMARY KEY,
c_category VARCHAR(100),
c_name VARCHAR(100),
c_count VARCHAR(50)
);

-- Tickets Table Creation
CREATE TABLE IF NOT EXISTS tickets(
ticket_id SERIAL PRIMARY KEY,
ticket_no INTEGER,
price INTEGER,
seat_id INTEGER,
hall_id INTEGER
);

-- Movie Table Creation
CREATE TABLE IF NOT EXISTS movie(
movie_id SERIAL PRIMARY KEY,
movie_name VARCHAR(100),
movie_genre VARCHAR(100),
movie_date DATE DEFAULT CURRENT_DATE
);