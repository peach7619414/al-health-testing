SELECT user_id, COUNT(*) AS failed_attempts 
FROM login_attempts 
WHERE status = 'failed' 
GROUP BY user_id 
HAVING COUNT(*) > 3;