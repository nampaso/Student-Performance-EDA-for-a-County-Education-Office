# PLP Data Analytics Assignment 5: Student Performance EDA (`plp-da-a5-student-performance-eda`)

## Project Summary
This repository contains an Exploratory Data Analysis (EDA) report investigating student performance across 1,200 learners. Prepared for a County Director of Education, it identifies key factors driving academic performance and highlights at-risk groups to guide learner-support funding allocations.

## Key Insights
1. **Attendance Drive:** Attendance percentage is the primary driver of performance ($r \approx 0.62$).
2. **Study Hour Impact:** Each additional study hour adds ~1.18 points to a student's average score ($R^2 \approx 0.34$).
3. **Institutional Gap:** Public school learners underperform private school peers across all attendance and study quartiles.
4. **Geographic Disparity:** Specific counties demonstrate higher concentrations of 'At Risk' learners (<60 average score).
5. **Gender Balance:** Minimal performance difference exists between male and female students.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
