# Food Delivery Performance Analysis

## What this project is about

I wanted to understand what actually drives delivery delays — not just report averages, but find the specific conditions that slow things down. This project takes raw food delivery data, cleans it properly, engineers useful time-based features, and builds a dashboard that answers real operational questions.

---

## Dashboard Preview

![Dashboard](dashboard.png)

---

## What I found

- Traffic jams increase average delivery time by **45%** — from 21.3 min (low traffic) to 31.2 min (jam)
- The **7–9 PM window** is the highest-delay period across all cities, consistently
- Drivers handling **3 simultaneous orders** average 47.4 min vs 22.8 min for single orders — a 2x gap
- Urban areas average 23.0 min with a 4.7 rating; Semi-Urban areas average 49.7 min with a lower 4.5 rating
- Overall average delivery time across all records: **26.4 minutes**, customer rating: **4.6 / 5**
---

## What I actually did

**Data cleaning (Python / Pandas)**
- Removed duplicate records
- Standardised the column name `Time_taken (min)` → `Delivery_Time_Min`
- Fixed a recurring city name typo: `Metropolitian` → `Metropolitan`
- Parsed `Order_Time` and `Pickup_Time` from string → datetime (handling format errors with `coerce`)
- Calculated `Prep_Time_Min` from the difference, set negative values to null
- Filtered out extreme outliers: delivery times ≥ 120 min removed

**Feature engineering**
- `Day_Of_Week` — enables weekly trend analysis
- `Is_Weekend` — boolean flag for comparing weekend vs weekday performance
- `Order_Hour` — extracted from order time for hourly breakdown

**Dashboard (Power BI)**
- KPI cards: Average Delivery Time, Customer Rating
- Bar chart: Average delivery time by traffic condition
- Bar chart: Average delivery time by number of simultaneous orders
- Line chart: Average delivery time by hour of day
- Table: City-level breakdown of delivery time and rating
  
---

## Tech stack

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning and feature engineering |
| Power BI | Dashboard and visualisation |
| CSV | Raw and cleaned data format |


---

## Files

```
├── raw_data.csv              # Original dataset
├── cleaned_data.csv          # Cleaned and enriched dataset
├── data_cleaning.py          # Full cleaning script
└── Dashboard.png             # Power BI dashboard screenshot
```
---

## Note

Missing city values were labeled as "Not Available" during data cleaning and excluded in dashboard-level analysis for consistency.
