-- -- SELECT id FROM people;
-- -- SELECT * FROM people;
-- SELECT name, id FROM people;
-- SELECT * FROM people;
-- DROP TABLE people;
-- CREATE TABLE t1(
--     id INT PRIMARY KEY,
--     name VARCHAR NOT NULL,
--     price INT DEFAULT 0
-- );
-- x`
-- SELECT * FROM t1;
-- -- Set c2 column as a FOREIGN KEY;

-- INSERT INTO people VALUES (1, 'ALEX ISRAEL')
SELECT * FROM people
ORDER BY id DESC;
-- ORDER BY first_name, last_name;
-- OR age < 3;
-- WHERE last_name = 'Doe'
-- INSERT INTO people (id, name) VALUES (4, 'EVERY ATZIRE');
SELECT name FROM people;
-- UPDATE people
-- SET job = 'Unknown'
-- WHERE last_name = 'Doe'
-- AND name = "John"

-- CREATE TABLE inventory (
-- id INT PRIMARY KEY,
-- name VARCHAR NOT NULL,
-- price INT DEFAULT 0
-- );
-- INSERT INTO inventory VALUES (1, 'ALEX ISRAEL', 250);
INSERT INTO inventory VALUES (3, 'ALEXA SHADDAI',399);
-- INSERT INTO inventory VALUES (2, 'EIZA PAULINA',195);
SELECT * FROM inventory;