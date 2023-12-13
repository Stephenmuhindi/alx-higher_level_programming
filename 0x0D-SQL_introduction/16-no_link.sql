-- we are listing all records kwa second table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
