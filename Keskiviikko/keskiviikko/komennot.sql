CREATE TABLE certificates (
    Id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    person_id int,
    CONSTRAINT fk_person
        FOREIGN KEY(person_id)
            REFERENCES person(id)
);

SELECT certificates.name, person.name FROM certificates, person WHERE certificates.person_id = person.id;

psql -h localhost -U postgres -d world -f C:\Users\katariina\Downloads\world;

select city.country_code where country_code = 'fin';
