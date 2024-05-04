# DATA70202 Applying Data Sciene: Indeed Scraping

## Dependencies
Follow the process found in the main repo's `README.md`.

Core Dependencies Include:
- Python 3.6.9

Other libraries can be found in `requirements.txt` file.

## File Structure
- `README.md`: Overview of the folder and its contents.
- `requirements.txt`: Required Python dependencies.
- `indeed_analysis.ipynb`: Notebook for scraped data loading, processing, analysing and visualising.
- `scrap.ipynb`: Notebook for data scraping data based on specific keywords.
- `./scrap/*.json`: JSON files from 5 different scraping sessions.

## Notebooks Information and Usage

### `scrap.ipynb` Section:

#### 1. Introduction
This notebook is designed for scraping and processing data related to various IT and finance professional positions. It provides a basic script to fetch data from Indeed based on specific job titles.

#### 2. Notebook Structure
- **Themes/Positions to Scrap:** Outlines the types of professional roles targeted for data scraping.
- **Scraping Script:** Contains Python code to automate the extraction of job posting information using Indeed API calls.

#### 3. Setup Instructions
To run this notebook, ensure the following:
- Ensure Python 3.6.9 is installed along with the Jupyter notebook environment.
- Install required libraries mentioned in the `requirements.txt` file using pip or conda.

#### 4. Usage
- Modify the search parameters in the script as needed to target different positions, locations, or target postings number.
- Execute the notebook to start scraping data. Ensure to set the scraping limits accordingly, as the process might take several hours.

#### 5. Contributing
Feel free to contribute to enhancing the scraping capabilities or adding new features, as it is currently very basic and bare.


### `indeed_analysis.ipynb` Section:

#### 1. Introduction
This notebook provides workflow for analysis of job data from Indeed, focusing on loading job postings, extracting key information, and analyzing data like skills required and salary ranges.

#### 2. Notebook Structure
- **Data Loading:** Import and combine JSON data into a single DataFrame.
- **Data Cleaning and Processing:** Deduplication and structuring of job postings.
- **Skill Extraction:** Automated extraction of skills from job descriptions.
- **Data Analysis:** Calculation of several insights based on specified criteria.

#### 3. Setup Instructions
To run this notebook effectively:
- Ensure Python 3.6.9 is installed along with the Jupyter notebook environment.
- Install required libraries mentioned in the `requirements.txt` file using pip or conda.

#### 4. Usage
- Update the paths to your JSON data files before running, or use the current scraping data.
- Execute cells sequentially to maintain logical flow and dependencies.
- Modify or extend analyses to provide additional data or different insights. Check `.json` files to see the available keys.

#### 5. Contributing
Contributions to expand the analyses or improve data handling are welcome.

### Author: - Radoslaw Izak (radoslaw.izak@postgrad.manchester.ac.uk)
