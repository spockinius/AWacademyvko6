
 CREATE DATABASE world WITH ENCODING 'UTF-8' LC_COLLATE='Finnish_Finland' LC_CTYPE='Finnish_Finland';

CREATE TABLE person (
   Id SERIAL PRIMARY Key,
   name varchar(255) NOT NULL,
   age int NOT NULL,
   student boolean
)

INSERT INTO person (name, age, student) VALUES('Seppo', '4', 'false');

INSERT INTO person (name, age, student) VALUES('Odin', '6', 'false');

INSERT INTO person (name, age, student) VALUES('Robo', '1', 'false');

INSERT INTO person.student WHERE name='Seppo' VALUES False;

INSERT INTO person.student FROM person WHERE name='Seppo' VALUES False;

SELECT name, age FROM person

SELECT * FROM person ORDER BY name DESC;

SELECT count(name) FROM person;

SELECT sum(age) FROM person;

SELECT sum(age)/count(name) FROM person;

UPDATE person
SET student = 'False'
WHERE id = 1 or id = 2 or id = 3;

UPDATE person SET name='Uusi-Robo' WHERE name='Robo';

DELETE FROM person WHERE id=6 or id=1 or id=5;

psql -h localhost -U postgres -d world -f C:\Users\katariina\Downloads\world;

select city.country_code from city where country_code = 'FIN';

select city.country_code, city.name from city where country_code = 'FIN';