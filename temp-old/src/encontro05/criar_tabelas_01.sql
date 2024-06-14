CREATE TABLE Person(
    person_id SERIAL PRIMARY KEY,
    sex VARCHAR(1) NOT NULL,
    name VARCHAR(100) NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    job VARCHAR(100) NOT NULL,
    company VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    mail VARCHAR(100) NOT NULL,
    blood_group VARCHAR(3) NOT NULL,
    address VARCHAR(200) NOT NULL
);