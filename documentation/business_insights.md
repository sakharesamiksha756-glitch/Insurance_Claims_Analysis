# Business Insights & Recommendations

## 1. Overall Fraud Overview

- Total claims analyzed: 15,420
- Fraudulent claims: 923
- Non-fraudulent claims: 14,497
- Overall fraud rate: 5.99%

## 2. Fraud Risk by Vehicle Category

- Utility vehicles had a fraud rate of 11.25%.
- Sedan vehicles had a fraud rate of 8.22%.
- Sport vehicles had a fraud rate of 1.57%.

### Insight
The analysis shows different fraud rates across vehicle categories. Utility and sedan claims had higher observed fraud rates than sport vehicle claims in this dataset.

## 3. Fraud Risk by Policy Type

- All Perils policies showed higher fraud rates within several vehicle categories compared with Liability policies.
- In the vehicle category and policy type analysis:
  - Sedan + All Perils: 10.06%
  - Utility + All Perils: 12.06%
  - Sedan + Collision: 6.88%
  - Sedan + Liability: 0.72%

### Insight
The observed fraud rate varied considerably across combinations of vehicle category and policy type. All Perils combinations showed higher observed fraud rates than Liability combinations in the analyzed data.

## 4. Fraud Risk by Accident Area

- Rural accident claims had a fraud rate of 8.32%.
- Urban accident claims had a fraud rate of 5.72%.

### Insight
The observed fraud rate was higher for rural accident claims than for urban accident claims in this dataset.

## 5. Fraud Risk by Fault

- Policy Holder fault claims had a fraud rate of 7.89%.
- Third Party fault claims had a fraud rate of 0.88%.

### Insight
Claims where the policy holder was recorded as being at fault had a substantially higher observed fraud rate than claims involving third-party fault in this dataset.

## 6. Fraud Risk by Driver Rating

- Driver Rating 1: 5.88% fraud rate
- Driver Rating 2: 5.63% fraud rate
- Driver Rating 3: 6.23% fraud rate
- Driver Rating 4: 6.20% fraud rate

### Insight
Fraud rates were relatively close across all four driver-rating groups, ranging from 5.63% to 6.23%. No large difference was observed based on driver rating alone in this dataset.

## 7. Fraud Risk by Police Report and Witness

- Claims without a police report had a fraud rate of 6.05%.
- Claims with a police report had a fraud rate of 3.74%.
- Claims without a witness had a fraud rate of 6.00%.
- Claims with a witness had a fraud rate of 3.45%.

### Insight
In this dataset, claims without a recorded police report or witness had higher observed fraud rates than claims with these records.

## 8. Fraud Risk by Previous Claims

- No previous claims: 7.79% fraud rate
- 1 previous claim: 6.21%
- 2 to 4 previous claims: 5.36%
- More than 4 previous claims: 3.38%

### Insight
The observed fraud rate decreased as the number of previous claims increased in this dataset. This is a descriptive finding and does not establish that having more previous claims reduces fraud risk.

## 9. Fraud Risk by Vehicle Price

- Less than 20,000: 9.40% fraud rate
- More than 69,000: 8.73%
- 40,000 to 59,000: 6.72%
- 20,000 to 29,000: 5.21%
- 30,000 to 39,000: 4.95%
- 60,000 to 69,000: 4.60%

### Insight
The observed fraud rate varied across vehicle-price categories. The highest observed rate was for vehicles priced below 20,000, followed by vehicles priced above 69,000.

## 10. Fraud Risk by Vehicle Age

- 4 years: 9.17% fraud rate
- New vehicles: 8.58%
- 3 years: 8.55%
- 5 years: 7.00%
- 6 years: 6.61%
- 7 years: 5.60%
- More than 7 years: 5.17%
- 2 years: 4.11%

### Insight
The observed fraud rate varied by vehicle age. The highest observed rate was among 4-year-old vehicles, while vehicles aged more than 7 years had a lower observed rate.

## 11. Fraud Risk by Policyholder Age

- 21 to 25: 14.81% fraud rate
- 18 to 20: 13.33%
- 16 to 17: 9.69%
- 31 to 35: 6.44%
- Over 65: 5.91%
- 36 to 40: 5.86%
- 26 to 30: 5.38%
- 41 to 50: 5.09%
- 51 to 65: 5.03%

### Insight
The observed fraud rate varied substantially across policyholder age groups. The 21–25 age group had the highest observed fraud rate among the groups in this dataset.

## 12. Fraud Risk by Number of Supplements

- No supplements: 6.70% fraud rate
- 1 to 2 supplements: 6.39%
- More than 5 supplements: 5.04%
- 3 to 5 supplements: 4.81%

### Insight
The observed fraud rate varied across supplement-count categories, with claims having no supplements showing the highest fraud rate in this dataset.

## 13. Fraud Risk by Address Change

- Under 6 months: 75.00% fraud rate
- 2 to 3 years: 17.53%
- 1 year: 6.47%
- No change: 5.76%
- 4 to 8 years: 5.23%

### Insight
Claims with a recent address change showed higher observed fraud rates in this dataset. However, the "under 6 months" category contains only 4 claims, so its 75% rate should be interpreted cautiously because of the very small sample size.

## 14. Overall Business Recommendations

Based on the observed patterns in the dataset:

1. Use vehicle category, policy type, accident area, and fault information as important dimensions for fraud-risk monitoring.
2. Give additional analytical attention to claim combinations that show higher observed fraud rates.
3. Use police-report and witness information as supporting claim-verification features.
4. Monitor unusual patterns in vehicle price, vehicle age, and policyholder age.
5. Treat very small categories cautiously and avoid making decisions based only on their percentage.
6. Use these findings as analytical indicators rather than proof of fraud, since the analysis describes patterns in historical claims data.