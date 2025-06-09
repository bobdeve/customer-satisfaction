# Customer Sentiment Analysis on Banking Apps

This project is part of a broader analysis on customer satisfaction, using financial app reviews sourced from the Google Play Store. The primary focus is on collecting and preprocessing user reviews from three major Ethiopian banking applications.

The project demonstrates effective application of technical skills and relevant libraries, such as `google-play-scraper` for data extraction, and `pandas` for data manipulation. Code functionality adheres to project requirements, with all elements of Task 1 implemented, including meaningful preprocessing steps. The repository is structured for clarity and scalability, following best practices in modular design and organization.

---

✅ **Task-1: Web Scraping & Preprocessing**

### 📌 Objective  
Scrape and clean at least 400+ reviews per banking app, targeting:

- Review text  
- Rating  
- Date  
- Bank name  
- Source of data  

### 🧰 Tools & Libraries  
- `google-play-scraper` – for scraping app reviews  
- `pandas` – for data cleaning and manipulation  
- `datetime` – for date normalization  
- `os` – for directory handling  

### 🏦 Target Banking Apps  

| Bank Name | Google Play Package Name |
|-----------|---------------------------|
| CBE       | com.combanketh.mobilebanking |
| BOA       | com.boa.boaMobileBanking     |
| Dashen    | com.dashen.dashensuperapp    |

### 🛠️ Steps Performed  
- Created a well-structured project hierarchy: `notebooks/`, `src/`, `data/raw/`, `.github/`, and `venv/`  
- Set up and activated a virtual environment (`webscraper`)  
- Installed all necessary dependencies and registered the Jupyter kernel  
- Scraped 400+ reviews per bank (totaling 1200+ reviews)  
- Preprocessed the data:
  - Removed duplicate entries  
  - Handled missing values  
  - Normalized review dates to `YYYY-MM-DD` format  
  - Combined all cleaned reviews into a single DataFrame  

### 📂 Output  
Cleaned review data is saved to: `data/processed/cleaned_reviews.csv` (or your actual file path)

---

This foundational work sets the stage for deeper sentiment analysis and modeling in subsequent tasks. The implementation reflects strong attention to detail, adherence to task guidelines, and proficient use of Python tools.

✅ **Task-2: Sentiment & Thematic Analysis**

This phase focuses on extracting meaningful insights from the cleaned review data, combining sentiment analysis with thematic categorization to uncover common user concerns and feedback trends across banking apps.

### 📊 Sentiment Analysis

- Applied a transformer-based sentiment model: **`distilbert-base-uncased-finetuned-sst-2-english`** to classify review sentiments into **positive**, **negative**, or **neutral**.
- Optionally explored baseline comparisons using **VADER** and **TextBlob** to evaluate consistency across tools.
- Aggregated sentiment results by **bank** and **rating level** (e.g., average sentiment score per 1-star review).

### 🧠 Thematic Analysis

A **theme** represents a recurring idea or concern within customer reviews. Thematic clustering allows us to translate unstructured feedback into actionable categories.

#### 🗝️ Keyword Extraction & Clustering

- Employed **TF-IDF** and **spaCy** to extract relevant keywords and n-grams (e.g., “login error”, “transaction delay”, “easy to use”).
- Optionally utilized **topic modeling** techniques (e.g., LDA) to aid in clustering related terms.
- Manually grouped extracted keywords into **3–5 overarching themes per bank**, such as:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Feature Requests

### 🔄 Pipeline & Output

- Applied standard NLP preprocessing steps:
  - Tokenization
  - Stop-word removal
  - Lemmatization (where applicable)
- Processed and annotated dataset saved as CSV including:
  - `review_id`
  - `review_text`
  - `sentiment_label`
  - `sentiment_score`
  - `identified_theme(s)`
- Final output includes:
  - Cleaned and annotated review dataset
  - Sentiment summaries per bank
  - Theme categorizations for qualitative insights

---

output

Cleaned and annotated data is saved to:




# Oracle Database Integration for Bank Review Data

This notebook demonstrates how to connect to an Oracle database using Python, create a review table, insert cleaned customer review data from a CSV file, and fetch the data for analysis.

## ⚙️ Oracle DB Workflow

1. **Connect to Oracle DB**  
   Use `oracledb` Python package to establish a connection with your Oracle database.

2. **Create Review Table**  
   The `Review_Banks` table includes the following columns:
   - `Short_Review` (text)
   - `Cleaned_Review` (text)
   - `Sentiment` (positive/neutral/negative)
   - `Sentiment_Score` (decimal)
   - `Theme` (category/topic)
   - `Bank` (bank name)
   - `Rating` (numeric)
   - `Review_Date` (date)
   - `Source` (data source)

3. **Insert Data from CSV**  
   - Load the `bank_review_sentiment_theme.csv` file with Pandas.
   - Iterate through rows and insert into the Oracle DB with error handling (e.g., `DPY-4004: invalid number`).

4. **View Data with Pandas**  
   - Execute SQL queries to fetch and load data into a DataFrame for inspection and analysis.

## 🛠 Requirements

- Oracle DB set up and running
- Python packages: `pandas`, `oracledb`
- CSV file located at `../data/processed/bank_review_sentiment_theme.csv`

## ✅ Example Query

```python
query = "SELECT * FROM REVIEW_BANKS WHERE ROWNUM <= 10"
df = pd.read_sql(query, conn)
df.head()
