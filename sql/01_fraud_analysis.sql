-- ============================================================
-- INSURANCE CLAIMS ANALYSIS
-- SQL ANALYSIS
-- ============================================================

-- 1. TOTAL NUMBER OF CLAIMS

SELECT
    COUNT(*) AS total_claims
FROM fraud_claims;
-- 2. FRAUD VS NON-FRAUD CLAIMS

SELECT
    FraudFound_P AS fraud_flag,
    COUNT(*) AS claim_count
FROM fraud_claims
GROUP BY FraudFound_P
ORDER BY fraud_flag;

-- 3. FRAUD PERCENTAGE

SELECT
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_percentage
FROM fraud_claims;

-- 4. FRAUD RATE BY VEHICLE CATEGORY

SELECT
    VehicleCategory,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY VehicleCategory
ORDER BY fraud_rate DESC;

-- 5. FRAUD RATE BY POLICY TYPE

SELECT
    PolicyType,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY PolicyType
ORDER BY fraud_rate DESC;

-- 6. FRAUD RATE BY ACCIDENT AREA

SELECT
    AccidentArea,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY AccidentArea
ORDER BY fraud_rate DESC;

-- 7. FRAUD RATE BY FAULT

SELECT
    Fault,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY Fault
ORDER BY fraud_rate DESC;

-- 8. FRAUD RATE BY DRIVER RATING

SELECT
    DriverRating,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY DriverRating
ORDER BY DriverRating;

-- 9. FRAUD RATE BY POLICE REPORT

SELECT
    PoliceReportFiled,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY PoliceReportFiled
ORDER BY fraud_rate DESC;

-- 10. FRAUD RATE BY WITNESS PRESENT

SELECT
    WitnessPresent,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY WitnessPresent
ORDER BY fraud_rate DESC;

-- 11. FRAUD RATE BY PAST CLAIMS

SELECT
    PastNumberOfClaims,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY PastNumberOfClaims
ORDER BY fraud_rate DESC;

-- 12. FRAUD RATE BY VEHICLE PRICE

SELECT
    VehiclePrice,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY VehiclePrice
ORDER BY fraud_rate DESC;

-- 13. FRAUD RATE BY VEHICLE AGE

SELECT
    AgeOfVehicle,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY AgeOfVehicle
ORDER BY fraud_rate DESC;

-- 14. FRAUD RATE BY POLICY HOLDER AGE

SELECT
    AgeOfPolicyHolder,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY AgeOfPolicyHolder
ORDER BY fraud_rate DESC;

-- 15. FRAUD RATE BY NUMBER OF SUPPLEMENTS

SELECT
    NumberOfSuppliments,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY NumberOfSuppliments
ORDER BY fraud_rate DESC;

-- 16. FRAUD RATE BY ADDRESS CHANGE

SELECT
    AddressChange_Claim,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) AS fraud_claims,
    ROUND(
        100.0 * SUM(CASE WHEN FraudFound_P = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fraud_rate
FROM fraud_claims
GROUP BY AddressChange_Claim
ORDER BY fraud_rate DESC;