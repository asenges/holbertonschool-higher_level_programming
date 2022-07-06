-- 0x0E. SQL - More queries
-- Alex Senges
SELECT 
id, 
name 
FROM cities 
WHERE state_id = (
	SELECT id FROM states WHERE name =`California`
);

