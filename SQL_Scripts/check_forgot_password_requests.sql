SELECT * FROM password_resets 
WHERE requested_at >= CURDATE() - INTERVAL 1 DAY;