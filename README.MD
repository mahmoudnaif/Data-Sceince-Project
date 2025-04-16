# 🚖 Porto Taxi Trajectory Data Cleaning & Analysis Project

This project focuses on data cleaning, preprocessing, and basic exploratory analysis of the **Porto Taxi Trajectory dataset**, which includes over **1.5 million taxi trips** recorded between **July 2013 and June 2014**.

---

## 📦 Dataset Overview

- **Source:** [Kaggle – Porto Taxi Trajectory Dataset](https://www.kaggle.com/datasets/crailtap/taxi-trajectory)
- **City:** Porto, Portugal 🇵🇹
- **Period:** 01/07/2013 to 30/06/2014
- **Taxis Covered:** 442
- **Trips:** 1,710,671
- **Data Points:** Includes origin, timestamp, GPS trajectory, and more

Each row in the dataset represents one **completed taxi trip**, with GPS data points recorded every **15 seconds**.

---

## 🧠 Goals of the Project

- 📌 Understand and document the structure of the dataset
- 🧹 Clean and preprocess the data
- 📉 Analyze trip durations, speeds, and missing values
- 🧭 Handle GPS trajectory data (polyline)
- 📈 Prepare the data for further modeling and analysis

---

## 📋 Dataset Features

| Column Name     | Description |
|-----------------|-------------|
| `TRIP_ID`       | Unique ID for each trip |
| `CALL_TYPE`     | How the trip was requested (`A` = central, `B` = taxi stand, `C` = random street) |
| `ORIGIN_CALL`   | Customer ID if `CALL_TYPE` = `A` |
| `ORIGIN_STAND`  | Stand ID if `CALL_TYPE` = `B` |
| `TAXI_ID`       | Unique ID of the taxi driver |
| `TIMESTAMP`     | UNIX timestamp of the trip start |
| `DAY_TYPE`      | Type of day: `A` = normal, `B` = holiday, `C` = day before holiday |
| `MISSING_DATA`  | Whether the GPS data is incomplete |
| `POLYLINE`      | GPS trajectory of the trip in `[lon, lat]` format every 15 seconds |

---

## 🧹 Data Cleaning & Preprocessing Steps

### ✅ General Cleaning

- Mapped categorical values for better readability:
  - `CALL_TYPE`: A → `Central`, B → `Stand`, C → `Street`
  - `DAY_TYPE`: A → `Normal`, B → `Holiday`, C → `Day Before Holiday`
- Checked for `NULL` values and ensured `ORIGIN_CALL` and `ORIGIN_STAND` are null where appropriate
- Converted `TIMESTAMP` to human-readable datetime format
- Parsed the `POLYLINE` column into actual lists of GPS coordinates
### 📏 Feature Engineering
- ✅ **Holidays were not specified**  
  Used a library called holidays to mark the holidays in `Porto - Portugal`

- ✅ **Distance Calculation**  
  Calculated total distance traveled using the Haversine formula

- ✅ **Trip Duration Calculation**  
  Calculated trip duration in seconds and minutes from `POLYLINE`:
  \[
  \text{Trip Time (seconds)} = (\text{Number of GPS Points} - 1) \times 15
  \]

- ✅ **Speed Estimation**  
    Derived average speed per trip:  
    \[
    \text{Speed} = \frac{\text{Distance (km)}}{\text{Time (hours)}}
    \]

- ✅ **Outlier Detection**  
  Identified outliers in trip durations and Distance using the IQR method for efficiency.

### 📉 Missing Data

- ✅ Used the `MISSING_DATA` flag to identify trips with incomplete GPS logs
- ✅ Interpolated missing GPS points for partial trajectories using linear interpolation (within a threshold of ~0.3 km per 15 seconds)
- Considered realistic max distance a car could travel in 15 seconds (~0.3 km = 72 km/h upper bound)
  
  **Note**: The threshold of 0.3 km was choosen based on the average speed of the complete trips which was Calculated.
---

## 📊 Summary Stats

| Metric               | Value |
|----------------------|-------|
| Total Trips Analyzed | ~1.55M |
| Avg. Duration        | ~10.9 minutes |
| Max Duration         | ~498 minutes |
| Trips with Missing GPS | Present, interpolated in valid cases |

---

## 📌 Future Work Ideas

- 🚀 Predict trip duration using ML models
- 🗺️ Visualize trips on interactive maps
- 📈 Cluster routes or passenger behaviors
- 🧠 Analyze taxi demand vs. time of day/week

---

## 📁 Files in this Project

- `README.md`: Project overview and documentation
- `notebook.ipynb`: Main Jupyter Notebook containing all steps
- `porto-taxi.csv`: The original dataset (not included here, download from Kaggle)
- `cleaned_data.csv`: Output after cleaning and feature engineering (optional)

---

## 📚 References

- 📊 [Kaggle Dataset: Porto Taxi Trajectory](https://www.kaggle.com/datasets/crailtap/taxi-trajectory)
- 📖 ECML/PKDD 15: Taxi Trip Time Prediction (II) Competition

---

## 🙌 Acknowledgments

Thanks to the original dataset authors and the ECML/PKDD 2015 challenge organizers.

---

