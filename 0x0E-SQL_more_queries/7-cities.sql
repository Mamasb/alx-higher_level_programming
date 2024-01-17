-- Create db 'hbtn_0d_usa'
-- If db aready exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--create tables 'cities' in db 'hbtn_0d_usa'
-- id INT uniquem, auto-generated, not null, primary key
-- state_id INT not null, foreign key that refrences if=d of 'ststes' table
-- name VARCHAR(256) not null
--  If table already exists, script should not fail

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFRENCES hbtn_0d_usa.states(id|)
);
