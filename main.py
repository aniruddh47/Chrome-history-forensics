import sqlite3
import pandas as pd
from datetime import datetime, timedelta

# -------- CONFIGURATION --------
# Chrome History file ka path (apne system ka path daal)
history_path = r"C:\DF project\History"

# -------- FUNCTION TO CONVERT CHROME TIMESTAMP --------
def convert_chrome_time(chrome_time):
    try:
        # Chrome time = microseconds since Jan 1, 1601
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)
    except:
        return None

# -------- READ DATA FROM DB --------
conn = sqlite3.connect(history_path)
cursor = conn.cursor()

# URLs table se data fetch karo
query = "SELECT url, title, visit_count, last_visit_time FROM urls"
df = pd.read_sql_query(query, conn)

# Chrome time ko normal datetime me convert karo
df['last_visit_time'] = df['last_visit_time'].apply(convert_chrome_time)

# 12-hour format me convert karo (string bana ke)
df['last_visit_time'] = df['last_visit_time'].apply(lambda x: x.strftime("%d-%m-%Y %I:%M:%S %p") if pd.notnull(x) else '')

# NaN URL ya title hatao
df = df[df['url'].notnull() & df['title'].notnull()]

# CSV export
output_path = "chrome_history_output.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ Chrome history exported successfully to: {output_path}")
