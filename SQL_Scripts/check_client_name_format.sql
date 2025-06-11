SELECT id, full_name
FROM clients
WHERE full_name IS NULL OR full_name = '' OR full_name NOT REGEXP '^[A-Za-z\s]{2,}$';