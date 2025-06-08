# Customer Sentiment Analysis on Banking Apps

This project is part of a larger analysis on customer satisfaction using financial app reviews from the Google Play Store. The focus is on scraping and preprocessing app reviews for three major Ethiopian banks.

## Interim GitHub Link Submission Requirements

For evaluating the interim GitHub link submission, the new rubrics would use these metrics:

### Application of Technical Skills and Libraries

- **High:** Effectively uses required libraries (e.g., google-play-scraper, Pandas, NLP libraries) and demonstrates their correct application in the code.
- **Moderate:** Basic use of required libraries with some optimizations possible.
- **Average:** Limited application with foundational library usage.
- **Non-existent:** Lacks proper use of key libraries.

### Code Functionality and Task Implementation

- **High:** Completes all elements of Task 1 and shows meaningful progress in Task 2, meeting interim requirements.
- **Moderate:** Task 1 works, but Task 2 implementation needs further development.
- **Average:** Partial functionality for Task 1 or minimal Task 2 attempt.
- **Non-existent:** No deliverables meeting challenge requirements.

### Project Code Organization and Structure

- **High:** Clearly organized repository with logical file/directory structure and modular code.
- **Moderate:** Organizes code adequately, though improvements in structure would help integration.
- **Average:** Code is present but lacks clear organization.
- **Non-existent:** Chaotic structure that doesn’t reflect challenge guidelines.

## Task-1: Web Scraping & Preprocessing

### Objective

Scrape and clean at least 400+ reviews per banking app, targeting:

- Review text
- Rating
- Date
- Bank name
- Source of data

### Tools & Libraries

- google-play-scraper – for scraping app reviews
- pandas – for data cleaning and manipulation
- datetime – for date normalization
- os – for directory handling

### Target Banking Apps

| Bank Name | Google Play Package Name         |
|-----------|---------------------------------|
| CBE       | com.combanketh.mobilebanking    |
| BOA       | com.boa.boaMobileBanking        |
| Dashen    | com.dashen.dashensuperapp       |

### Steps Performed

- Created project structure: `notebooks/`, `src/`, `data/raw/`, `.github/`, and `venv/`
- Created and activated virtual environment (`webscraper`)
- Installed dependencies and registered Jupyter kernel
- Scraped 400+ reviews per bank (total 1200+)
- Preprocessed the data:
  - Removed duplicate reviews
  - Handled missing values
  - Normalized review dates to YYYY-MM-DD format
  - Combined all reviews into one cleaned DataFrame

### Output

Cleaned review data is saved to: `data/cleaned_reviews.csv`

