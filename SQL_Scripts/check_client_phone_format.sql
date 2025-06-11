SELECT id, phone
FROM clients
WHERE phone NOT REGEXP '^\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}$';