SELECT id, address
FROM clients
WHERE address IS NULL OR address = '' OR LENGTH(address) < 5;