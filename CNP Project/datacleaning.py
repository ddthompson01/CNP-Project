#imported pandas for data manipulation
import pandas as pd

file_path = '/Users/daniellethompson/Desktop/CNP Project/Data Set/School_Nutrition_Programs___Meal_Reimbursement_Information___Program_Year_2017-2018.csv'
data = pd.read_csv(file_path)

# Filtering data for only IDEA Public Schools
idea_data = data[data['CEName'].str.contains('IDEA', case=False, na=False)]

# Dropping columns 
columns_to_drop = [
    'CountyDistrictCode','CEName','CECounty','ReportType', 'CEID', 'TypeOfAgency', 'TypeOfSNPOrg',
    'MilkDays', 'Milktotal', 'MilkADP', 'MilkServedFree', 'MilkServedReduced',
    'MilkServedPaid', 'MilkReimbursement'
]
idea_data = idea_data.drop(columns=columns_to_drop)

# Removing duplicates if there are any
idea_data = idea_data.drop_duplicates()

# Exporting the filtered data to a CSV file
output_file_path = '/Users/daniellethompson/Desktop/CNP Project/IDEA_Public_Schools.csv'
idea_data.to_csv(output_file_path, index=False)

#Printing statement to ensure my code is saved
print(f"New filtered data is saved to CNP Project {output_file_path}")
