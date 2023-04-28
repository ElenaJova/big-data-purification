# Big Data Purification with Flask application
This project aims to cleanse company names from a given dataset using a Flask application that interfaces with a SQLite database and a MongoDB instance. The goal is to standardize the names of the companies, removing unwanted characters and legal entities like "LTD." and "Limited" from the names.
## Prerequisites
To run this project, you will need the following software:

- Python 3.7 or later
- Flask
- pymongo
- sqlite3
### Get started
1.Clone this Git repository to your local machine. \
2.Install the required Python packages \
3.Start the Flask application \
4.The application provides two API functions: 
- 'GET /companies': returns a list of all company records from the SQLite database.
- 'POST /companies': writes a company record to the MongoDB instance. \
### Dataset
The dataset used in this project consists of the following fields: 
- 'id': a unique identifier for each record (primary key)
- 'name': the official name of the company
- 'country_iso': the ISO code for the country where the company is located
- 'city': the city where the company is located
- 'nace': the NACE code for the company's economic activity
- 'website': the company's website URL
### Processing company names
To cleanse the company names in the dataset, we used regular expressions (RegEx) in Python. The RegEx code was designed to remove unwanted characters and legal entities from the names, resulting in a standardized, normalized name. However, we recommend performing additional analysis of the data to ensure the names are accurately cleansed.
