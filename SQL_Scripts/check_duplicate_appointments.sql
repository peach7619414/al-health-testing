SELECT user_id, date, COUNT(*) AS appointment_count
FROM appointments
GROUP BY user_id, date
HAVING COUNT(*) > 1;