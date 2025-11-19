# 🌍 Global Climate Data Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) ![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white)

A Data Science project developed to analyze global climate data, with a specific focus on filtering, processing, and visualizing weather stations in **Portugal**. This project demonstrates data cleaning, CSV manipulation, and geospatial visualization using Python.

---

## 📝 Project Overview

This repository contains a series of Python scripts (`ex1.py` to `ex8.py`) that perform progressive data analysis tasks on a global climate dataset.

**Key Features:**
* 📊 **Data Cleaning:** Handling missing values and optimizing data storage.
* 🇵🇹 **Filtering:** Extracting specific data for Portuguese weather stations.
* 🗺️ **Visualization:** Generating interactive HTML maps using **Folium** to plot station locations.

---

## 📂 File Structure & Script Guide

| Script | Description | Output |
| :--- | :--- | :--- |
| `ex1-1.py` | Analyzes dataset memory usage and space differences. | Console Output |
| `ex2-1.py` | Calculates percentage of null values in the dataset. | Console Output |
| `ex6.py` | Filters global data to extract Portuguese cities/stations. | `estacoesPT.csv` |
| `ex7.py` | Cleans data by replacing Station IDs with City Names. | `id_estacoesPT.csv` |
| `ex8.py` | Visualizes filtered stations on an interactive map. | `mapa.html` |
| `estacoes_portuguesas.html` | Generated map showing station locations. | HTML File |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed along with the necessary libraries:

```bash
pip install pandas folium notebook
```

### Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JeyCraftPT/Projeto_DataS_Two.git](https://github.com/JeyCraftPT/Projeto_DataS_Two.git)
    ```
Run the scripts: You can run individual scripts to process the data. For example, to generate the map:
```bash
python ex8.py
```

View the Map: Open the generated estacoes_portuguesas.html file in your web browser to explore the interactive map.
