SELECT user_id, COUNT(*) 
FROM appointments 
WHERE start_time BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 1 HOUR) 
GROUP BY user_id 
HAVING COUNT(*) > 1;