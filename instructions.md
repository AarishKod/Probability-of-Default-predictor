# FICO Score Bucketing for Mortgage Default Prediction

**Author:** Aarish Kodnaney  
**Project:** Credit Risk Analysis - Probability of Default (PD) Prediction

## Project Overview

Build a machine learning model to predict mortgage default probability using FICO scores. Since the ML architecture requires categorical data, you'll need to bucket continuous FICO scores (300-850) into discrete categories.

## Background

- **FICO Score:** Standardized credit score (300-850) that quantifies borrower creditworthiness
- **Usage:** Used in 90% of US mortgage application decisions
- **Goal:** Map FICO scores to buckets and calculate PD (Probability of Default) for each bucket

---

## Step-by-Step Implementation Plan

### Phase 1: Data Loading and Exploration

#### Step 1: Load the dataset using pandas
- Read the CSV file into a DataFrame
- Print the first few rows to understand the structure

#### Step 2: Explore the data
- Check how many rows and columns you have
- Look at the column names - identify which column has FICO scores and which has default indicator
- Check for missing values in FICO score column
- Use `.describe()` to see min, max, mean, median of FICO scores

#### Step 3: Visualize FICO distribution
- Create a histogram of FICO scores
- Check the distribution of defaults (how many defaulted vs didn't default)
- Calculate overall default rate

---

### Phase 2: Creating FICO Buckets

#### Step 4: Research FICO bucket ranges
- Decide: Use standard industry buckets (Poor/Fair/Good/Very Good/Excellent) OR create custom data-driven buckets?
- Standard ranges are: 
  - Poor: 300-579
  - Fair: 580-669
  - Good: 670-739
  - Very Good: 740-799
  - Excellent: 800-850

#### Step 5: Implement bucketing
- Use `pd.cut()` for standard ranges OR `pd.qcut()` for equal-frequency buckets
- Create a new column in your DataFrame with the bucket labels
- Verify: Check that all FICO scores were successfully bucketed (no NaN values)

#### Step 6: Validate bucketing
- Count how many loans are in each bucket
- Make sure no bucket is too small (aim for at least 30+ observations per bucket)

---

### Phase 3: Analyze Default Rates by Bucket

#### Step 7: Calculate default statistics per bucket
- Group by FICO bucket
- For each bucket, calculate:
  - Total number of loans
  - Number of defaults
  - Default rate (defaults / total)

#### Step 8: Visualize results
- Create a bar chart showing default rate by FICO bucket
- Verify the pattern: Does default rate decrease as FICO improves?

#### Step 9: Create a summary table
- Format your results into a clean table showing PD (probability of default) for each bucket
- This is what Charlie needs for her ML model

---

### Phase 4: Prepare for ML Model (Optional but Recommended)

#### Step 10: One-hot encode categorical buckets
- Use `pd.get_dummies()` to convert bucket categories into binary columns
- This creates columns like: `fico_bucket_Poor`, `fico_bucket_Fair`, etc.

#### Step 11: Split data for modeling
- Separate features (X) from target variable (y = default)
- Split into training and testing sets (80/20 split)

#### Step 12: Test with a simple model
- Try a decision tree classifier (you've done this before!)
- Evaluate accuracy
- Compare: Does bucketed FICO predict defaults better than random guessing?

---

### Phase 5: Optimization and Comparison

#### Step 13: Experiment with different bucketing strategies
- Try different numbers of buckets (3, 5, 7, 10)
- Compare which gives the clearest separation in default rates

#### Step 14: Document your findings
- Which bucketing approach worked best?
- What's the default rate for each bucket?
- How confident is your model?

#### Step 15: Create a function to predict PD for new loans
- Given a FICO score, your function should return which bucket it falls into and the associated PD

---

## Key Pandas Functions You'll Need

- `pd.read_csv()` - Load data
- `.describe()`, `.head()`, `.info()` - Explore data
- `pd.cut()` or `pd.qcut()` - Create buckets
- `.groupby().agg()` - Calculate statistics by group
- `pd.get_dummies()` - One-hot encoding

---

## Key Questions to Answer

1. **What bucketing scheme gives Charlie the best predictive power while keeping the model interpretable?**
2. **Is 5 buckets optimal, or should you use more/fewer?**
3. **Does default rate monotonically decrease as FICO score improves?**

---

## Expected Deliverables

1. Python script with data loading and bucketing functions
2. Summary table showing PD for each FICO bucket
3. Visualizations (histogram of FICO distribution, bar chart of default rates)
4. ML model that predicts default using bucketed FICO scores
5. Analysis document explaining your bucketing choice and results

---

## Tips for Success

- Start with Steps 1-3 to understand your data before bucketing
- Validate that your buckets make intuitive sense (higher FICO = lower default rate)
- Compare multiple bucketing strategies before choosing one
- Document your reasoning for bucket choices

---

## Next Steps

Start with Phase 1 (Data Loading and Exploration). Once you understand your data's structure and distribution, move on to bucketing in Phase 2.

Good luck! 🚀