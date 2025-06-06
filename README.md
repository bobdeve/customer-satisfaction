# 📊 Customer Sentiment Analysis on Banking Apps

This project is part of a larger analysis on customer satisfaction using financial app reviews from the Google Play Store. The focus is on scraping and preprocessing app reviews for three major Ethiopian banks.

---

## ✅ Task-1: Web Scraping & Preprocessing

### 📌 Objective

Scrape and clean at least 400+ reviews per banking app, targeting:

- Review text
- Rating
- Date
- Bank name
- Source of data

---

### 🧰 Tools & Libraries

- `google-play-scraper` – for scraping app reviews
- `pandas` – for data cleaning and manipulation
- `datetime` – for date normalization
- `os` – for directory handling

---

### 🏦 Target Banking Apps

| Bank Name | Google Play Package Name                     |
|-----------|----------------------------------------------|
| CBE       | `com.combanketh.mobilebanking`               |
| BOA       | `com.boa.boaMobileBanking`                   |
| Dashen    | `com.dashen.dashensuperapp`                  |

---

### 🛠️ Steps Performed

1. **Created project structure**:
   - `notebooks/`, `src/`, `data/raw/`, `.github/`, and `venv/`
2. **Created and activated virtual environment (`webscraper`)**
3. **Installed dependencies and registered Jupyter kernel**
4. **Scraped 400+ reviews per bank (total 1200+)**
5. **Preprocessed the data**:
   - Removed duplicate reviews
   - Handled missing values
   - Normalized review dates to `YYYY-MM-DD` format
   - Combined all reviews into one cleaned DataFrame

---

### 📂 Output

Cleaned review data is saved to:
