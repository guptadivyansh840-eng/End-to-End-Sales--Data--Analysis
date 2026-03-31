import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
file= r"c:\Users\LENOVO\Downloads\sales_data_10000.csv"
df= pd.read_csv(file)
print(df.head())
# City wise Sales in all Categories
df["Sales"]= df["Price"]*df["Quantity"]
piv = df.groupby("City",as_index= False)["Sales"].sum()
print(piv)
#city wise Sales for Tech Category Grouping
z= df[df["Category"]== "Tech"] 
gh = z.groupby("City",as_index= False)["Sales"].sum()


#Visualization
# City wise Sales in all Categories Graph plot
plt.subplot(1,2,1)
plt.bar(piv["City"],piv["Sales"])
plt.xticks(rotation=45)
plt.ticklabel_format(style= "plain", axis="y")
plt.title("Sales By City", size=10)
# City wise Sales in Tech Cateogry plotting
plt.subplot(1,2,2)
plt.title("Sales in Tech Category")
plt.pie(gh["Sales"], labels= gh["City"],autopct='%1.1f%%')
plt.tight_layout()# overlapping fixing
plt.show()


#####SQL dataset store
conn = sqlite3.connect("sales.db")
df.to_sql("sales_data", conn, if_exists="replace", index=False)
#Query1 City wise Sales Data
query1= "SELECT City, SUM(Price*Quantity) AS Total_Sales FROM sales_data GROUP BY City"
sql_city_sales= pd.read_sql(query1,conn)# this line only runs query1 in file stored in conn(sales.db) and store reult in SQL_CITY_Sales varialble
print(sql_city_sales)
#Query2 City wise sales for tech category
query2= "SELECT City, SUM(Price*Quantity) AS Total_Saless FROM sales_data WHERE Category= 'Tech' GROUP BY City"
sql_city_Tech_sales = pd.read_sql(query2, conn)
print(sql_city_Tech_sales)
conn.close() # close connection





