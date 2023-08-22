create database google_yelp;
use google_yelp;

drop table review;

create table review (
reviewID int not null ,
clienteID int not null,
gmapID int not null,
date datetime,
rating int,
text varchar(255), 
primary key (reviewID)
);

create table restaurant (
gmapID int,
name varchar(255),
address varchar(255),
latitude decimal(9,6),
longitude decimal(9,6),
state varchar(255),
delivery varchar(255),
permanently_closed varchar(255)		
);

create table comentarios (
commentID int,
reviewID int,
text varchar(255),
date datetime
);

create table delivery (
CompanyID int,
delivery_rating  int,
delivery_feedback varchar(255)
);

create table cliente (
clienteID int,
name varchar(255)
);

create table estado (
stateID int,
state varchar(255)
);

create table categoria (
categoriaID int,
categoria varchar(255)
);

alter table comentarios 
add primary key (commentID);

alter table restaurant 
add primary key (gmapID);

alter table cliente 
add primary key (clienteID);


alter table review 
add foreign key (clienteID) references cliente(clienteID) ;

alter table review 
add foreign key (gmapID) references restaurant(gmapID) ;

alter table comentarios
add foreign key (reviewID) references review(reviewID) ;

alter table estado 
add primary key (stateID);

alter table categoria
add primary key (categoriaID);

alter table delivery
add primary key (CompanyID);

ALTER TABLE restaurant CHANGE COLUMN state stateID 
int;

alter table restaurant
add foreign key (stateID) references estado(stateID) ;

alter table categoria
add column gmapID int;

alter table categoria
add foreign key (gmapID) references restaurant(gmapID) ;

