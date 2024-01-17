-- Listing all cities in the hbtn_0d_usa database.
-- sorting data in ascending ids.
SELECT c. `id`, c.`name`, s.`name`
  FROM `cities` as c
        INNER JOIN `states` AS s
	ON c.`states_id` = s.`id`
  ORDER BY c.`id`;
