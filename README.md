# DATA70202 Applying Data Sciene: IBM 2024 Group Project

## Group Members
- Radoslaw Izak (radoslaw.izak@postgrad.manchester.ac.uk)
- Tomas Garcia (tomas.garcia@postgrad.manchester.ac.uk)
- Iqra Ali (iqra.ali@postgrad.manchester.ac.uk)
- Maria Teneva (maria.teneva@postgrad.manchester.ac.uk)
- Zhihui Wang (zhihui.wang@student.manchester.ac.uk)

Please be advised that these emails have been made valid for the academic year 2023-2024 at The University of Manchester and might be invalid at the time of cloning the repository. For further contact, please directly contact the collaborators.

## Short description of the Project
### Course Unit Leader
- **Name:** Dr. Nuno Pinto
- **Email:** [nuno.pinto@manchester.ac.uk](mailto:nuno.pinto@manchester.ac.uk)

### Industry Project Mentor
- **Name:** Jon McNamara
- **Email:** [j0nnymac@uk.ibm.com](mailto:j0nnymac@uk.ibm.com)

During the 2023-2024 academic year, as part of "Applying Data Science (ADS) 70202", group members enrolled at the University of Manchester, collaborated on a project with IBM (academic partner). Our focus was on IBM Skills Build and our project aimed to analyze data from the UK Govt Employment and Skills survey to evaluate and improve the relevance of IBM Skills Build platform content. 

We investigated current IBM Skills Build material; identified skill gaps using variety of data sources, and ultimately recommended content updates to address current and projected industry needs. More about the process and findings can be found in the `REPORT.pdf` and `PRESENTATION.pdf` files.

This collaboration was conducted within the framework of our university course and does not represent emplyoment under IBM. 

For more information, please refer to the `P13 IBM.docx` file.

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

## Local Skills Improvement Plans Analysis and Modelling (./LSIP/*)
Short description (TBD).

## Working Futures 2024 Analysis and Modelling (./WF2024/*)
This folder focuses on predicting UK labor market trends from 2025 to 2035. More data information is available [here](https://www.gov.uk/government/publications/uk-labour-market-projections-2014-to-2024).

The `wf-regions-ml-2.ipynb` notebook provides an end-to-end workflow for forecasting labor market trends. It covers data preprocessing, model selection, predictions, evaluations, and includes a graphical user interface for interactive forecasting.

## Indeed Scraping and Contemporary Skills Analysis (./INDEED/*)
### Scraping
The `scrap.ipynb` notebook is utilised data collection for UK job positions by scraping specific keywords. It targets roles like programmers, software developers, IT analysts, architects, and managers.

### Analysis
The `indeed_analysis.ipynb` notebook analyzes Indeed job postings, involving data preprocessing, skill extraction, median salary analysis, and skill frequency evaluation. It visualizes insights such as median salaries by measures such as location and skill demand by companies.

## File Structure
- `README.md`: Overview of the project, folders, and work achieved.
- `./LSIP/*`: Folder with all files relevant to Local Skills Improvement Plan modelling and analysis, more information found inside.
- `./INDEED/*`: Folder with all files relevant to Indeed scraping skills analysis, more information found inside.
- `./WF2024/*`: Folder with all files relevant to Working Futures 2024 modelling and analysis, more information found inside.
- `P13 IBM.docx`: Full description of the academic project, as given by the course leader and academic industry partner.
- `REPORT.pdf`: Detailed description of our work in form of a scientific report.
- `PRESENTATION.pdf`: Detailed description of our work in form of a presentation.

## Code Attribution
### LSIP
- Which core libraries, data, and so on were used (TBD).

### WF2024
- **Scikit-learn**: Used for implementing and training machine learning models such as Elastic Net orSupport Vector Regression.
- **Matplotlib**: Employed for creating visualizations to compare actual versus predicted labor workforce across various model predictions.
- **Pandas** and **NumPy**: Utilized for data manipulation and handling, especially for preparing and structuring data for model training and predictions.
- **XGBoost** and **LightGBM:**: Specifically used for training and prediction within the context of boosting methods in machine learning.

### INDEED
- **Pandas** and **NumPy**: Used for data manipulation and numerical computations.
- **Matplotlib**: Employed for creating various data visualizations like bar graphs and plots.
- **JSON**: Employed for loading and saving scraped data in JSON format.
- **Requests** and **urllib**: Utilized for making HTTP requests and encoding URL parameters to Indeed's website to scrape job data.
- **Re (Regular Expression)**: Used for pattern matching and data extraction from the raw HTML content. For more information, click [here](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags)

## References
- UK Government. "Local Skills Improvement Plans". UK Government Publications. Retrieved from https://www.gov.uk/government/publications/local-skills-improvement-plans

- UK Government. "UK Labour Market Projections: 2014 to 2024". UK Government Publications. Retrieved from https://www.gov.uk/government/publications/uk-labour-market-projections-2014-to-2024
