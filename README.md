# 🎮 Video Game Sales Analytics - Power BI Dashboard

## 📌 Project Overview
This project presents an interactive **Power BI Dashboard** that visualizes and analyzes global video game sales data. The dashboard provides insights into:
- **Top-selling video game genres**
- **Global sales distribution across regions**
- **Best-selling publishers**
- **Popular gaming platforms**
- **Sales trends over the years**

The dataset consists of **16,598** records, covering sales data from different **gaming consoles, publishers, and genres** worldwide.

---

## 📊 Key Visualizations & Insights

### 🔹 1. Global Sales by Genre
- The **Action** genre dominates with **19.63%** of total sales.
- Other top-selling genres include **Sports, Shooter, and Role-Playing.**

### 🔹 2. Popular Gaming Platforms
- The **PlayStation (PS)** series and **Nintendo DS** are among the most popular platforms.
- Other notable platforms include **PS2, Wii, Xbox 360, and PS3.**

### 🔹 3. Global Sales by Publisher
- **Nintendo leads the market**, followed by **Electronic Arts (EA) and Activision** in terms of global sales.
- Other major publishers include **Sony Computer Entertainment, Ubisoft, and THQ.**

### 🔹 4. Sales Over the Years
- A steady **rise in video game sales from 1980 to the early 2000s**, with peak sales around **2007-2009.**
- North America and Europe contribute the most to global sales.

---

## 📂 Files Included
| File Name | Description |
|-----------|------------|
| `VG_Sales.pbix` | Power BI dashboard file |
| `VGSales_ss.png` | Screenshot of the dashboard |
| `readme.md` | This documentation file |

---

## 📁 Folder Structure
```
VG_Sales_Analytics/
│-- data/
│   ├── VG_Sales.csv                 # Raw dataset
│   ├── cleaned_VG_Sales.csv          # Processed dataset
│-- scripts/
│   ├── data_cleaning.py              # Cleans and preprocesses the dataset
│   ├── exploratory_analysis.py        # Exploratory Data Analysis (EDA)
│   ├── sales_trends.py                # NEW: Sales trends analysis
│   ├── platform_analysis.py           # NEW: Platform-wise sales comparison
│   ├── forecasting.py                 # Improved: ML-based forecasting
│-- reports/
│   ├── insights_report.md            # Summary of insights & findings
│-- visualizations/
│   ├── VG_Sales.pbix                 # Power BI report
│   ├── VGSales_ss.png                 # Power BI dashboard screenshot
│-- .gitattributes                     # Ensures GitHub detects Python & CSV files
│-- README.md                          # Documentation

---

## 🚀 How to Use
1. **Open Power BI**: Ensure you have **Power BI Desktop** installed.
2. **Load `VG_Sales.pbix`**: Open the `.pbix` file in Power BI.
3. **Explore the Dashboard**:
   - Use **filters** and **slicers** to customize views.
   - Hover over charts for more detailed insights.
4. **Analyze Trends**: Identify **best-selling platforms, publishers, and genres**.

---

## 📈 Business Use Cases
This dashboard is useful for:
- **Game developers & publishers** to understand sales trends and market demand.
- **Investors & analysts** tracking gaming industry growth.
- **Retailers & marketers** planning sales and advertising strategies.

---

## 🔧 Future Improvements
✅ Add **forecasting models** for future sales predictions.
✅ Include **individual game analysis** for top-selling titles.
✅ Enhance **regional breakdowns** for more granular insights.

---

## 🏆 Credits & Acknowledgments
- **Dataset Source**: Video game sales dataset
- **Visualization Tool**: Microsoft Power BI

If you found this project useful, feel free to ⭐ the repository! 🚀🎮
