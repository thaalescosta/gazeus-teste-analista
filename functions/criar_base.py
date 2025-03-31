import os
import sqlite3
from IPython.display import display

def display_df(df):
    display(df.style.hide(axis="index"))

def criar_base():
    if os.path.exists('dbCompany'):
        os.remove('dbCompany')

    # Create connection to database
    conn = sqlite3.connect('dbCompany')
    cursor = conn.cursor()

    # Create users table
    cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        country TEXT NOT NULL
                    )
                    '''
    )

    # Create transactions table
    cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS transactions (
                        user_id INTEGER NOT NULL,
                        transaction_id INTEGER PRIMARY KEY,
                        transaction_date TEXT NOT NULL,
                        transaction_state TEXT NOT NULL,
                        transaction_amount REAL NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                    )
                    '''
                )

    conn.commit()
    conn.close()
