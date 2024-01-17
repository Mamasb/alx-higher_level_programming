-- List all cities of Cali that can be foundd in 'hbtn_0d_usa'
-- "states table contains only records where 'name = Califonia"
-- but 'id' cannot be different.
--Results must be stored in ascending order by 'city.id'
-- Not allowed to use JOIN Keyword

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'Califonia'
);
