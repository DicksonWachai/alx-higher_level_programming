-- get all cities in db
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states
ON state_id=states.id;
