SELECT DISTINCT card_type 
FROM payments 
WHERE LENGTH(card_number) = 16;