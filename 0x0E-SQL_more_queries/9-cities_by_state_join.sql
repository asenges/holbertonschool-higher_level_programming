-- 0x0E. SQL - More queries
-- Alex Senges
SELECT 
cities.id, 
cities.name, 
states.name
FROM cities 
INNER JOIN states 
ON cities.state_id = states.id;

