# DATA70202 Applying Data Sciene: IBM 2024 Group Project

## Group Members
- Radoslaw Izak (radoslaw.izak@postgrad.manchester.ac.uk)
- Tomas Garcia (tomas.garcia@postgrad.manchester.ac.uk)
- Iqra Ali (iqra.ali@postgrad.manchester.ac.uk)
- Maria Teneva (maria.teneva@postgrad.manchester.ac.uk)
- Zhihui Wang (zhihui.wang@student.manchester.ac.uk)

**Note:** These email addresses are valid for the academic year 2023-2024 at The University of Manchester and may be invalid thereafter. Please contact the collaborators directly through GitHub for further communication.

## Short description of the Project
### Course Unit Leader
- **Name:** Dr. Nuno Pinto
- **Email:** [nuno.pinto@manchester.ac.uk](mailto:nuno.pinto@manchester.ac.uk)

### Industry Project Mentor
- **Name:** Jon McNamara
- **Email:** [j0nnymac@uk.ibm.com](mailto:j0nnymac@uk.ibm.com)

During the 2023-2024 academic year, as part of the "Applying Data Science (ADS) 70202" course, we collaborated with our Industry Partner at IBM to focus on the IBM Skills Build platform. Our project aimed to analyze data from the UK Government's Employment and Skills survey to enhance the relevance of the IBM Skills Build platform content.

Key activities included analyzing current IBM Skills Build material, identifying skill gaps using various data sources, and recommending content updates based on current and projected industry needs. Find more details in `REPORT.pdf` and `PRESENTATION.pdf`.

This collaboration was conducted under the academic framework of our university course and does not represent employment under IBM.

For more project specifics, refer to `P13 IBM.docx`.

## Dependencies

To install the required dependencies, create a `venv` and activate it via:
```
python3 -m venv venv
source venv/bin/activate
```

and run:

```
pip3 install -r requirements.txt
```

Be advised that different `venv` instances and `Python3.XX` versions should be used for different Jupyter notebooks found within this repository in relevant folders. For more information visit [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) and `README` in each folder.

## Project Directories Info

### Local Skills Improvement Plans Analysis and Modelling `(./LSIP/*)`
This folder contains EDA and preprocessing tasks on web advert data from the ONS available [here](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/labourdemandvolumesbystandardoccupationclassificationsoc2020uk) which provides information about job postings by various socio-demographic characteristics, including Local Skills Improvement Plan (LSIP) areas. The files cover time series forecasting models and their evaluation, as sell as visualisations of regional skills gap indices by 2025.

### Working Futures 2024 Analysis and Modelling `(./WF2024/*)`
This folder focuses on predicting UK labor market trends from 2025 to 2035. More data information is available [here](https://www.gov.uk/government/publications/uk-labour-market-projections-2014-to-2024).

The `wf-regions-ml-2.ipynb` notebook provides an end-to-end workflow for forecasting labor market trends. It covers data preprocessing, model selection, predictions, evaluations, and includes a graphical user interface for interactive forecasting.

### Indeed Scraping and Contemporary Skills Analysis `(./INDEED/*)`
#### Indeed Scraping
The `scrap.ipynb` notebook is utilised data collection for UK job positions by scraping specific keywords. It targets roles like programmers, software developers, IT analysts, architects, and managers.

#### Data Analysis
The `indeed_analysis.ipynb` notebook analyzes Indeed job postings, involving data preprocessing, skill extraction, median salary analysis, and skill frequency evaluation. It visualizes insights such as median salaries by measures such as location and skill demand by companies.

## File Structure
* `README.md` - Overview of the project and its directories.
* `./LSIP/*` - Local Skills Improvement Plan modelling and analysis files.
* `./INDEED/*` - Files related to Indeed job scraping and skills analysis.
* `./WF2024/*` - Working Futures 2024 modelling and analysis files.
* `P13 IBM.docx` - Full academic project description.
* `REPORT.pdf` - Detailed scientific report of our work.
* `PRESENTATION.pdf` - Presentation outlining our project findings.

## Code Attribution
### `LSIP`
-  **Pandas** and **NumPy**: Utilized for data manipulation and handling.
-  **PlotlyExpress**: Employed module for visually appealing graphs of results
-  **Seaborn** and **Matpolotlib**: Used for data visualisation

### `WF2024`
- **Scikit-learn**: Used for implementing and training machine learning models such as Elastic Net or Support Vector Regression.
- **Matplotlib**: Employed for creating visualizations to compare actual versus predicted labor workforce across various model predictions.
- **Pandas** and **NumPy**: Utilized for data manipulation and handling, especially for preparing and structuring data for model training and predictions.
- **XGBoost** and **LightGBM:**: Specifically used for training and prediction within the context of boosting methods in machine learning.

### `INDEED`
- **Pandas** and **NumPy**: Used for data manipulation and numerical computations.
- **Matplotlib**: Employed for creating various data visualizations like bar graphs and plots.
- **JSON**: Employed for loading and saving scraped data in JSON format.
- **Requests** and **urllib**: Utilized for making HTTP requests and encoding URL parameters to Indeed's website to scrape job data.
- **Re (Regular Expression)**: Used for pattern matching and data extraction from the raw HTML content. For more information, click [here](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags)

## References
- UK Government. "Local Skills Improvement Plans". UK Government Publications. Retrieved from https://www.gov.uk/government/publications/local-skills-improvement-plans

- UK Government. "UK Labour Market Projections: 2014 to 2024". UK Government Publications. Retrieved from https://www.gov.uk/government/publications/uk-labour-market-projections-2014-to-2024
