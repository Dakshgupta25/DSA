SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
AND BINARY RIGHT(mail, 13) = '@leetcode.com'; 