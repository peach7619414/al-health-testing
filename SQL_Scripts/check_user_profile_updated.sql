SELECT * FROM user_profiles 
WHERE last_updated >= NOW() - INTERVAL 1 DAY;