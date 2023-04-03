drop table if exists people;

create table people (
    given_name varchar(255),
    family_name varchar(255),
    date_of_birth DATE,
    place_of_birth varchar(255),
    primary key (given_name, family_name, date_of_birth)
);

