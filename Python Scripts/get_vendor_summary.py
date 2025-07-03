import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db
import os
import time

# Creating the logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# 1. Get the root logger that Jupyter has already pre-configured
logger = logging.getLogger()

# 2. Setting its level
logger.setLevel(logging.DEBUG) 

# 3. Creating our own handler to send logs to our desired file.
file_handler = logging.FileHandler("logs/get_vendor_summary.log", mode='a')

# 4. Creating a formatter to define the layout of our log messages
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# 5. Adding our handler to the logger
# To prevent adding it multiple times if you re-run the cell, we check first
if not any(isinstance(h, logging.FileHandler) and h.baseFilename == file_handler.baseFilename for h in logger.handlers):
    logger.addHandler(file_handler)

def create_vendor_summary(conn):
    """
    This function merges different tables to get the overall vendor summary
    and adds new columns to the resultant data.
    """
    
    # SQL query to build the vendor sales summary
    query = """
    WITH freight_summary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    
    purchase_summary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Volume,
            pp.Price AS ActualPrice,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM Purchases AS p
        JOIN purchase_prices AS pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.PurchasePrice, pp.Volume, pp.Price
    ),
    
    sales_summary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesPrice) as TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM Sales
        GROUP BY VendorNo, Brand
    )
    
    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.Volume,
        ps.ActualPrice,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM purchase_summary ps
    LEFT JOIN sales_summary ss
        ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
    LEFT JOIN freight_summary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC;
    """
    
    # Execute the query and load data into a DataFrame
    vendor_sales_summary = pd.read_sql_query(query, conn)
    
    return vendor_sales_summary


def clean_data(df):
    # This function will clean the data

    # Changing the datatype to float
    df['Volume'] = df['Volume'].astype('float')

    # Filling the missing values with 0
    df.fillna(0, inplace = True)

    # Removing spaces from the categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # Creating new columns for a better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']
    
    return df

if __name__ == '__main__':

    # --- START TIMING ---
    start_time = time.time()
    logging.info("Script execution started.")

    # Initialize conn to None
    conn = None

    try:
        # Creating database connection
        conn = sqlite3.connect('inventory.db')

        logging.info('Creating vendor summary table.....')
        summary_df = create_vendor_summary(conn)
        logging.info(f"Summary table created with {len(summary_df)} rows.")

        logging.info('Cleaning Data.....')
        clean_df = clean_data(summary_df)
        logging.info("Data cleaning complete.")

        # Creating CSV File
        clean_df.to_csv('vendor_summary_output.csv', index=False)

        logging.info('Ingesting data.....')
        ingest_db(clean_df, 'vendor_sales_summary', conn)
        logging.info('Ingestion complete.')

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

    finally:
        # --- CLOSE CONNECTION ---
        if conn:
            conn.close()
            logging.info("Database connection closed.")

        # --- END TIMING AND REPORT ---
        end_time = time.time()
        total_time = (end_time - start_time) / 60
        time_message = f"Script finished. Total execution time: {total_time:.2f} minutes."
        
        logging.info(time_message)
        print(time_message)