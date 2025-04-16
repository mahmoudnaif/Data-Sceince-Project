# 🚖 Porto Taxi Trajectories - EDA & Trip Duration Insights

This repository contains an exploratory data analysis (EDA) notebook based on the **Porto Taxi Trajectories Dataset**, which includes a full year of GPS trajectory data from taxi trips in Porto, Portugal.

## 📂 Dataset Source

- 📎 **Kaggle Dataset**: [Taxi Trajectory Data](https://www.kaggle.com/datasets/crailtap/taxi-trajectory/data)
- 📅 **Time Period**: 01/07/2013 – 30/06/2014
- 🚕 **Taxis Covered**: 442 unique taxis
- 📍 **Data Points**: Trip metadata + GPS trajectories

## 📌 Objective

The main goal of this notebook is to **analyze and clean** the data in preparation for potential predictive modeling tasks such as:
- **Trip duration prediction**
- **Route clustering**
- **Anomaly detection**
- **Geo-spatial pattern analysis**

## 🧠 What’s Inside the Notebook?

- ✅ **Data Loading and Overview**
  - Load and inspect the structure of the CSV file.
  - Understand data types, nulls, and basic statistics.

- 🔍 **Detailed Dataset Description**
  - Explanation of each column in the dataset.
  - Contextual notes for geo-spatial and temporal features.

- 📈 **Initial Analysis**
  - Check for outliers and anomalies in the `TIMESTAMP`.
  - Detect and handle duplicated `TRIP_ID`s.
  - Examine missing GPS data using the `MISSING_DATA` field.

- 📊 **Feature Engineering Potential**
  - Discussion of how to compute trip duration from `POLYLINE`.
  - Note on parsing `POLYLINE` (list of GPS points) from string to usable format.

## 🛠 Key Columns Explained

| Column         | Description |
|----------------|-------------|
| `TRIP_ID`      | Unique ID for each trip |
| `CALL_TYPE`    | How the trip was requested (Central, Taxi Stand, Street) |
| `ORIGIN_CALL`  | Customer ID (if applicable) |
| `ORIGIN_STAND` | Taxi stand ID (if applicable) |
| `TAXI_ID`      | ID of the taxi driver |
| `TIMESTAMP`    | Start time of the trip (Unix timestamp) |
| `DAYTYPE`      | Type of day: normal, holiday, or pre-holiday |
| `MISSING_DATA` | Whether GPS points are missing |
| `POLYLINE`     | List of GPS coordinates, sampled every 15 seconds |

## 🧮 Trip Duration Formula

> **Trip Time (seconds)** = (`len(POLYLINE)` - 1) × 15

## 📌 Notes

- Duplicated `TRIP_ID`s were found and flagged for cleaning.
- `POLYLINE` is the most valuable feature for predicting travel time and understanding routes.

## 🚀 Future Work

- Parse and visualize GPS data
- Cluster routes using trajectory similarity
- Train ML models to predict trip duration or optimize routes

---

📬 Feel free to fork, contribute, or use this analysis as a baseline for further modeling work!
