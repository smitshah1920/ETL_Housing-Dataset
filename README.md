# ETL_Housing-Dataset (Extract,Transform,Load - Data_Pipeline)

### In this project I have built ETL pipeline for the housing data containing 63,474 records.

### The source of the data was a Datacamp URL containing the CSV file.

## 1st stage : ### The first stage of the process is to create a python script to Extact data (Extract.py). I have first set source path and desitination path and then defined Object oriented function to download snapshot of the data into the destination folder.

### 2nd stage : The second stage of the process is to create a script that would Transform (Transform.py) raw data of the downloaded snapshot into the cleaned version by performing create,insert,detele,data type identification and querying data operations using SQLAlchemy.

### 3rd Stage : The third stage of the process is to load the cleaned data into the PostgreSQL database which I have automated by script (load.py).

### 4th Stage : To gain the insights from the loaded data, I have initiated a (create_insights.py) which will provide data grouped by county and provide insights on sales count, total sales, maximum/minimum and average sales proces for which houses had been sold. 

### 5th stage : the last stage of the cycle is to develop a script that would export monthly insights data (Exporting_Monthly_Insights.py) into the destination folder in the form of the MS Excel worksheet using library 'xlsxwriter'.

Note: The file names mentioned above can be explored individually in this repository.
