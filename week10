# Import required libraries
import json
import csv

# Open the CSV file and reading the file
with open ("SalesJan2009.csv", "r") as f:
   reader = csv.reader(f)

   # Empty sales_data list
   sales_data = []

   # Iterate through each row
   for row in reader:
     # Appending the data to sales_data
     sales_data.append({"Transaction_data": row[0], "Product": row[1], "Price": row[2], "Payment_Type": row[3], "Name": row[4], "City": row[5], "State": row[6], "Country": row[7]})
     
# Open a json file called transaction_data.json
with open("transaction_data.json", "w") as f:
  #Write the list to the json file
  json.dump(sales_data, f, indent = 4)
