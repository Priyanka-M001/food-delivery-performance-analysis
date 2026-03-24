import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Standardize column names
df.rename(columns={"Time_taken (min)": "Delivery_Time_Min"}, inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Convert time columns with defined format
df["Order_Time"] = pd.to_datetime(df["Time_Ordered"], format="%H:%M", errors="coerce")
df["Pickup_Time"] = pd.to_datetime(df["Time_Order_picked"], format="%H:%M", errors="coerce")

# Calculate preparation time (in minutes)
df["Prep_Time_Min"] = (df["Pickup_Time"] - df["Order_Time"]).dt.total_seconds() / 60
df.loc[df["Prep_Time_Min"] < 0, "Prep_Time_Min"] = None

# Convert numeric fields
df["Delivery_person_Ratings"] = pd.to_numeric(df["Delivery_person_Ratings"], errors="coerce")
df["multiple_deliveries"] = pd.to_numeric(df["multiple_deliveries"], errors="coerce")

# Clean and standardize categorical data
df["City"] = df["City"].replace("Metropolitian", "Metropolitan")
df["City"] = df["City"].fillna("Not Available")
df["Road_traffic_density"] = df["Road_traffic_density"].fillna("Not Available")

cat_cols = [
    "Weather_conditions",
    "Road_traffic_density",
    "Type_of_order",
    "Type_of_vehicle",
    "Festival",
    "City"
]

for col in cat_cols:
    df[col] = df[col].astype("string").str.strip().str.title()

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Create additional columns for analysis
df["Day_Of_Week"] = df["Order_Date"].dt.day_name()
df["Is_Weekend"] = df["Day_Of_Week"].isin(["Saturday", "Sunday"])
df["Order_Hour"] = df["Order_Time"].dt.hour

# Remove extreme delivery time values
df = df[df["Delivery_Time_Min"] < 120]

# Export cleaned dataset
df.to_csv("cleaned_data.csv", index=False)