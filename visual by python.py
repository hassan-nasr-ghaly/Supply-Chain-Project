import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r"F:\PROJECT\supply_chain_data.csv")

# Select columns
loc = df[['Product type','Defect rates']]

# Group by 'Product type' and calculate the mean defect rates
calc = loc.groupby('Product type')['Defect rates'].mean()

# Create a barh chart with control in name title and size 
plt.barh(calc.index,calc.values,color = '#091B39',height=0.6)
plt.title('Average Defect Rate by Product Type',fontsize=14, color = 'g',style = "italic")
plt.xlabel('Average Defect Rate (%)', fontsize=12, color='blue')

# Add text labels with defect rates formatted to 2 decimal places
for i , s in enumerate(calc):
    plt.text(s, i ,f'{s:.2f}' , ha ='left' , va= 'bottom')

# To remove right gradline in chart So that the number does not interfere with the line
plt.gca().spines['right'].set_visible(False)     

# Display the chart
plt.show()

