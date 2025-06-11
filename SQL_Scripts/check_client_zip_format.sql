SELECT id, zip_code
FROM clients
WHERE zip_code NOT REGEXP '^[0-9]{5}(-[0-9]{4})?$';