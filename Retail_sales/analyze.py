
import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv("retail_sales_100.csv")
print(df.head())

#sales vs profit based on category
category_data = df.groupby("category")[["sales_amount", "profit"]].sum()
category_data.plot(kind = "bar")

plt.title("Total sales and profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("images/category_chart.png")
plt.show()


#sales vs profit based on region
region_data = df.groupby("region")[["sales_amount", "profit"]].sum()
region_data.plot(kind = "bar")

plt.title("Total sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("images/region_chart.png")
plt.show()


#monthly sales trend
month_order=["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)

monthly_sales = df.groupby("month")["sales_amount"].sum()
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("images/monthly_chart.png")
plt.show()

