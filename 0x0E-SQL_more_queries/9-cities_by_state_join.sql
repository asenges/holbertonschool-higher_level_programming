-- 0x0E. SQL - More queries
-- Alex Senges
SELECT 
cities.id AS Id, 
cities.name AS City, 
states.name AS State
FROM cities 
INNER JOIN states 
ON cities.state_id = states.id;

