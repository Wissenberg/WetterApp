SET NAMES utf8;

DROP DATABASE IF EXISTS weather_db;
CREATE DATABASE weather_db
 	CHARACTER SET utf8mb4
	COLLATE utf8mb4_german2_ci
;

USE weather_db;

CREATE TABLE country(
	id INT AUTO_INCREMENT,#
	shorted CHAR(5),
	name_eng VARCHAR(60),
	name_de VARCHAR(60),
	PRIMARY KEY(id)
);

CREATE TABLE state_name(
	id INT AUTO_INCREMENT,
	name VARCHAR(60),
	country_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(country_id)
	 REFERENCES country(id)
);

CREATE TABLE city(
	id INT AUTO_INCREMENT,
	name VARCHAR(60),
	state_id INT,
	lat FLOAT,
	lon FLOAT,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id)
	 REFERENCES state_name(id)
);

CREATE TABLE weatherValues (
	id INT AUTO_INCREMENT,
	captured VARCHAR(30),
	forecastTime VARCHAR(30),
	temperature VARCHAR(10),
	wind VARCHAR(10),
	humidity VARCHAR(10),
	rain BOOLEAN,
	city_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(city_id)
	 REFERENCES city(id)
);

INSERT INTO country(shorted, name_eng, name_de) VALUES
('GER','Germany', 'Deutschland'),
('GB','Great Britain', 'Großbritannien')
;

INSERT INTO state_name(name, country_id) VALUES
('Nordrhein-Westfalen',1),
('Baden-Württemberg',1),
('Bayern',1),
('Berlin',1),
('Brandenburg',1),
('Bremen',1),
('Hamburg',1),
('Hessen',1),
('Mechlenburg-Vorpommern',1),
('Niedersachsen',1),
('Rheinland-Pfalz',1),
('Saarland',1),
('Sachsen',1),
('Sachsen-Anhalt',1),
('Schleswig-Holstein',1),
('Thüringen',1),
('England',2),
('Schottland',2),
('Wales',2),
('Nordirland',2)
;

INSERT INTO city(name, state_id, lat, lon) VALUES
('Essen',1,51.450832,7.013056),
('Gelsenkrichen',1,51.511530,7.093030),
('Berlin',4,52.520008,13.404954),
('München',3,48.135124,11.581981),
('London',17,51.507351,-0.127758)
;



