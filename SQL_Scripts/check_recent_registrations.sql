SELECT * FROM users 
WHERE registration_date >= CURDATE() - INTERVAL 7 DAY;