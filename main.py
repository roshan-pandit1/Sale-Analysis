import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default ="plotly_white"

data =pd.read_csv("Sample - Superstore.csv",encoding ='latin-1')

'''print(data.head())
print(data.describe())
print(data.info)'''

data['Order Date']= pd.to_datetime(data['Order Date'])
#print(data.info)
data['Ship Date']= pd.to_datetime(data['Ship Date'])
#print(data.head())

data['Order Month'] =data['Order Date'].dt.month
data['Order year'] =data['Order Date'].dt.year
data['Order Day of Week'] =data['Order Date'].dt.dayofweek

#print(data.head())

#Monthly Sale Analysis

sales_by_month =data.groupby('Order Month')['Sales'].sum().reset_index()
fig =px.line(sales_by_month,
             x="Order Month",
             y='Sales',
             title='Monthly sales Analysis')

#fig.show()

#Sales by Category

sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()
#print(sales_by_category)

fig =px.pie(sales_by_category,
            values='Sales',
            names='Category',
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside',textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category',title_font=dict(size=24))

#fig.show()

sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
#print(sales_by_subcategory)

fig=px.bar(sales_by_subcategory,
           x='Sub-Category',
           y='Sales',
           title="Sales analysis by Sub-Category")

#fig.show()

#profit for the month

profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
#print(profit_by_month)

fig =px.line(profit_by_month,
             x='Order Month',
             y='Profit',
             title="Monthly Profit analysis")

#fig.show()

#Profit by Category

profit_by_category =data.groupby('Category')['Profit'].sum().reset_index()
#print(profit_by_category)

fig =px.pie(profit_by_category,
            values='Profit',
            names='Category',
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside',textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis by Category',title_font=dict(size=24))

#fig.show()

#Profit by Sub Category
profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
#print(profit_by_subcategory)

fig=px.bar(profit_by_subcategory,
           x='Sub-Category',
           y='Profit',
           title="Profit analysis by Sub-Category")

#fig.show()

#Sales and Profit -Customer Segment

sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()

color_palette =colors.qualitative.Pastel

fig=go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Sales'],
                     name='Sales',
                     marker_color=color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Profit'],
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment',
                  yaxis_title='Amount')

#fig.show()

#Sales to Profit ratio

sales_profit_by_segment =data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio']= sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])
