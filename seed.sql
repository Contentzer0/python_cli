TRUNCATE TABLE CONTACTS;


ALTER SEQUENCE contacts_id_seq RESTART WITH 1;

INSERT INTO contacts(name, email, phone_number) VALUES ('Conzer Seiei', 'conzer.seiei@gmail.com', 9018328808);
INSERT INTO contacts(name, email, phone_number) VALUES ('Mike Scuderi', 'mike.scuderi@yahoo.com', 5164040788);
INSERT INTO contacts(name, email, phone_number) VALUES ('Tim Metzger', 'tim.metzger@gmail.com', 911);
INSERT INTO contacts(name, email, phone_number) VALUES ('Demetri Geras', 'greasy.greek@gmail.com', 5161111111);
