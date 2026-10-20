# Write your MySQL query statement below
select user_id,name,mail from Users 
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$'
  AND BINARY mail LIKE '%@leetcode.com';

/*
REGEXP checks whether the email follows the required pattern and character rules.
It checks:
- ^[A-Za-z] — the email starts with a letter.
- [A-Za-z0-9_.-]* — the remaining name contains only allowed characters.
- @leetcode\\.com$ — the email ends with @leetcode.com.

BINARY makes the comparison case-sensitive, so uppercase letters won't match the required lowercase domain. */