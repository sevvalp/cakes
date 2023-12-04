import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Load your dataset
df = pd.read_csv('/app/cake_list.csv')

# Fetching values from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Define a function to standardize units and convert diameter to mm


def standardize_units(row):
    unit = str(row['unit']).lower()

    if unit in ['mm', 'milimeter', 'milimetre']:
        return row['diameter']
    elif unit in ['inch', 'in', 'inches']:
        # Convert inches to millimeters (1 inch = 25.4 mm)
        return row['diameter'] * 25.4
    else:
        # Handle other units or unknown units as needed
        return None


# Apply the function to create a new 'diameter_mm' column
df['diameter_mm'] = df.apply(standardize_units, axis=1)

# Drop the original 'diameter' and 'unit' columns if needed
df = df.drop(['diameter', 'unit'], axis=1)

print(df)

engine = create_engine(
    connection_string)

# Write the DataFrame to the database table named 'cake'
df.to_sql('cake', con=engine, index=False, if_exists='replace')
