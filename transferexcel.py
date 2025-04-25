import json
import pandas as pd

# Load the JSON file
with open('bankques.JSON', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract data for each tab
tab1_data = data.get("phần sức khỏe bệnh lý", [])
tab2_data = data.get("phần thông tin sản phẩm", [])

# Convert data to DataFrames
tab1_df = pd.DataFrame(tab1_data, columns=["number", "type", "question", "answer", "difficulty"])
tab2_df = pd.DataFrame(tab2_data, columns=["number", "type", "question", "answer", "difficulty"])

# Write to Excel with two tabs 
with pd.ExcelWriter('output4.xlsx', engine='xlsxwriter') as writer:
    tab1_df.to_excel(writer, sheet_name='Phần sức khỏe bệnh lý', index=False)
    tab2_df.to_excel(writer, sheet_name='Phần thông tin sản phẩm', index=False)

print("Excel file created successfully!")