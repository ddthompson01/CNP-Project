--Cleaning Data in SQL

--1. This query identifies duplicate records in the dataset. 
SELECT SiteID, ClaimDate, COUNT(*)
FROM idea_public_schools
GROUP BY SiteID, ClaimDate
HAVING COUNT(*) > 1;


--2. This query ensures that the total number of students enrolled does not exceed total enrollemnt 
SELECT *
FROM idea_public_schools
WHERE (FreeEligibleQty + ReducedEligibleQty + PaidEligibleQty) > EnrollmentQty;

--3. This query checks that the ClaimDate follows the correct format (YYYY-MM-DD).
SELECT *
FROM idea_public_schools
WHERE ClaimDate NOT LIKE '____-__-__'
   OR LENGTH(ClaimDate) != 10;