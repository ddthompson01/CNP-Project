-- Example queries for analyzing data from the IDEA Public Schools dataset
--Assume the dataset is stored in a table named idea_public_schools with appropriate data types

-- 1. Retrieve all records for IDEA Public Schools
SELECT * FROM idea_public_schools;

-- 2. Getting the total reimbursements for each school
        --Getting the reimbursments by school helps idenify the schools that recived the most funding
SELECT CEName, SUM(TotalReimbursement) AS Total_Reimbursement
FROM idea_public_schools
GROUP BY CEName;

-- 3. Finding the average daily participation in lunch for each school
        --This helps identify the schools with the highest lunch participation rates
SELECT CEName, AVG(LunchADP) AS Avg_Lunch_ADP
FROM idea_public_schools
GROUP BY CEName;

-- 4. Listing the schools with total meal reimbursements over 5000
SELECT CEName, TotalReimbursement
FROM idea_public_schools
WHERE TotalReimbursement > 5000;

-- 5. Counting the number of schools in each county
SELECT SiteCounty, COUNT(*) AS School_Count
FROM idea_public_schools
GROUP BY SiteCounty;

-- 6. Exploring the distribution of meal reimbursements

SELECT
    CEName,
    AVG(TotalReimbursement) AS avg_reimbursement,
    MIN(TotalReimbursement) AS min_reimbursement,
    MAX(TotalReimbursement) AS max_reimbursement,
    SUM(TotalReimbursement) AS total_reimbursement
FROM idea_public_schools
GROUP BY CEName;

--7. Idenifing outliers in the meal reinmbursents
    --important to identify errors
WITH stats AS (
    SELECT
        AVG(TotalReimbursement) AS avg_reimbursement,
        STDDEV(TotalReimbursement) AS stddev_reimbursement
    FROM idea_public_schools
)
SELECT *
FROM idea_public_schools, stats
WHERE TotalReimbursement > avg_reimbursement + 3 * stddev_reimbursement
   OR TotalReimbursement < avg_reimbursement - 3 * stddev_reimbursement;
