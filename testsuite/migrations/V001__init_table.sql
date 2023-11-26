create schema service;

create table service.service_table (
    id bigserial not null primary key,
    name text not null
);
