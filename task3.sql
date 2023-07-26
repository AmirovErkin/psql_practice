-- Task 3.1  1 --
SELECT country , COUNT(country) FROM people GROUP BY country ;

-- Task 3.1  2 --
SELECT date_of_birth , COUNT(date_of_birth) FROM students GROUP BY date_of_birth ;

-- Task 3.1 3 --
SELECT universty , COUNT(universty) FROM students GROUP BY universty;

-- Task 3.1 4 --
SELECT country, count(is_married)  FROM people GROUP BY country HAVING count(is_married) > 0 AND bool_or(is_married);

-- Task 3.1 5 --
SELECT company , price , COUNT(*) FROM product GROUP BY company, price;

-- Task 3.1 6 --
SELECT type, COUNT(*) FROM product GROUP BY type;

-- Task 3.1 7 --
SELECT genre, COUNT(*) FROM films WHERE rate > 5 GROUP BY genre ;

-- Task 3.1 8 --

SELECT rate , country FROM films GROUP BY rate , country;