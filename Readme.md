# 🏏 IPL Big Data Analytics Dashboard

Welcome to the **IPL Big Data Analytics Dashboard** repository! This project demonstrates an end-to-end Big Data pipeline, utilizing Apache Spark for processing large datasets and Streamlit for visualizing the results.

## 🚀 Project Overview

Developed for the **Big Data Analytics (BCS714D)** course, this mini-project aims to analyze historical cricket data to uncover trends, player performance, and team statistics. The raw data is processed in a cloud-based Big Data environment (Google Colab) using PySpark, ensuring efficient handling of large datasets.

-----

## 🎯 Key Features

* **🏆 Most Successful Teams:** Visualizing match wins across all seasons to identify the most dominant franchises.

* **🏏 Top Run Scorers:** Career analysis of the highest run-getters, highlighting batting consistency over the years.

* **🎯 Top Wicket Takers:** Identification of the most effective bowlers and their wicket-taking records.

* **🎖️ Player of the Match:** Analysis of players with the most match-winning performances to find the true game-changers.

* **📊 Season Trends:** Tracking the number of matches played per season to understand the league's evolution.

-----

## 📊 Data Pipeline Workflow

This project follows a structured Big Data processing pipeline:

  * **Ingestion**: Raw `matches.csv` and `deliveries.csv` files are uploaded to the Spark environment.
  * **Cleaning (ETL)**: Team names are standardized (e.g., "Delhi Daredevils" → "Delhi Capitals") using PySpark DataFrames.
  * **Analysis**: Spark SQL queries are executed to aggregate data (Counts, Sums, Group By).
  * **Export**: Final aggregated results are saved as lightweight CSV files.
  * **Visualization**: Streamlit loads the CSVs and renders interactive charts using Plotly.

-----

## 🛠 Technologies Used

  * **Google Colab**: Cloud-based notebook environment for running Spark.
  * **PySpark**: The Python API for Apache Spark, used for ETL and SQL analytics.
  * **Streamlit**: Python library for building the interactive web application.
  * **Plotly**: Library used for creating interactive and dynamic charts.

-----

## 📂 Project Structure

```text
ipl-big-data-dashboard/
├── app.py                  # The main Streamlit dashboard application
├── requirements.txt        # Python dependencies (streamlit, pandas, plotly)
├── README.md               # Project documentation
└── data/                   # Folder containing processed CSVs
    ├── top_winners.csv
    ├── top_scorers.csv
    ├── top_wickets.csv
    ├── top_pom.csv
    └── matches_per_season.csv
```

## ⚙️ How to Run Locally

To run the dashboard on your own machine, follow these steps:

1.  **Prerequisites**:
    Ensure you have Python (version 3.8 or higher) and a code editor (like VS Code) installed.

2.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/ipl-big-data-dashboard.git](https://github.com/your-username/ipl-big-data-dashboard.git)
    cd ipl-big-data-dashboard
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App**:
    ```bash
    streamlit run app.py
    ```
    The app will open in your default web browser at `http://localhost:8501`.

-----

## 📜 License

This project is open-source and available under the **[MIT License](LICENSE)**.

-----