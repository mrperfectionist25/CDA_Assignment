import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv(r"C:\Users\HP 450 G2\Desktop\athlete_events.csv.csv")

## Using Interpolate method() for filling the null values

data['Age'].value_counts()

data['Age'] = data['Age'].interpolate()

data['Age'].isnull().sum()

## Using median() middle value for the null values.

data['Weight'].median()

data['Weight'] = data['Weight'].fillna(data['Weight'].median())  # Std .deviation is low from the mean so that data is more reliable for wieght col for null values filling withy mean and median which is almost sameis almost same

data['Weight'].isnull().sum()

data['Height'].mean()

data['Height'] = data['Height'].fillna(data['Height'].median())

data['Medal'] = data['Medal'].fillna("No_Medal")

st.set_page_config(layout='wide')
st.title("Dataset of Olympic  data ")
st.subheader("Muhammad Ali Khan ")

col1, col2, col3, col4 = st.columns(4)

# total Particpants
participants = data['Name'].nunique()
col1.metric("Total Participants", participants)

# total Gold
Gold_Medal = data[data['Medal'] == 'Gold']
gm = Gold_Medal["Medal"].count()
col2.metric("Total Gold Medal", gm)

# total Silver
Silver_Medal = data[data['Medal'] == 'Silver']
sm = Silver_Medal["Medal"].count()
col3.metric("Total Silver Medal", sm)

# total Bronxe
Bronze_Medal = data[data['Medal'] == 'Bronze']
bm = Bronze_Medal["Medal"].count()
col4.metric("Total Bronze Medal", bm)

all_city = sorted(data['City'].unique())
col1, col2 = st.columns(2)
selected_city = col1.selectbox("Select your City", all_city)
Subset_city = data[data['City'] == selected_city]
st.dataframe(Subset_city)

# Subset Gold
subset_gold = Gold_Medal[Gold_Medal['City'] == selected_city]
gold = subset_gold['Medal'].count()

# subset Silver
subset_silver = Silver_Medal[Silver_Medal['City'] == selected_city]
silver = subset_silver['Medal'].count()

# subset Bronze
subset_bronze = Bronze_Medal[Bronze_Medal['City'] == selected_city]
bronze = subset_bronze['Medal'].count()

# medal won
without_no_medal = data[data['Medal'] != 'No_Medal']
medal_name = without_no_medal[without_no_medal['City'] == selected_city]
medal_won = medal_name.groupby("Name")['Name'].count().sort_values(ascending=False).head(5)
Table = medal_name.groupby("Name")['Medal'].count().sort_values(ascending=False).head(7)

# season_medal
season_medal = medal_name[medal_name['City'] == selected_city]
season = season_medal.groupby('Season')['Medal'].count().head(5)
# Hist=medal_won['Age'].value_counts()

col5, col6, col7, col8 = st.columns(4)
Total_participants = data[data['City'] == selected_city]['Name'].count()
col5.metric("Total_partipants", Total_participants)

Total_Gold = Gold_Medal[Gold_Medal['City'] == selected_city]['Medal'].count()
col6.metric("Total_Gold", Total_Gold)

Total_Silver = Silver_Medal[Silver_Medal['City'] == selected_city]['Medal'].count()
col7.metric("Total_Silver", Total_Silver)

Total_Bronze = Bronze_Medal[Bronze_Medal['City'] == selected_city]['Medal'].count()
col8.metric('Total_Bronze', Total_Bronze)

with st.container():
    col9, col10, col11 = st.columns(3)

# Line chart
# without_no_medal=data[data['Medal']!='No_Medal']
g = subset_gold.groupby("Year").agg(Gold=('Medal', 'count'))
s = subset_silver.groupby("Year").agg(Silver=('Medal', 'count'))
b = subset_bronze.groupby("Year").agg(Bronze=('Medal', 'count'))
line = pd.concat([g, s, b], 1)
col9.header("Winner Of Medal")
col9.line_chart(line)

# barchart
# without No Medal
fig, ax = plt.subplots(figsize=(20, 15))
ax = plt.barh(medal_won.index, medal_won.values, color='grey')
plt.xlabel("Number of Medal")
col10.header("Medal Winners Top 5")
col10.pyplot(fig)
col11.header("Table of Winners")
col11.table(Table)

# without_no_medal=data[data['Medal']!='No_Medal']
with st.container():
    col12, col13, col14 = st.columns(3)

# Piecahrt
Gender_medal = medal_name[medal_name['City'] == selected_city]
gender = Gender_medal.groupby(['Sex', 'Medal'])['Sex'].count()
fig1, ax1 = plt.subplots()
ax1.pie(gender, labels=gender.index, autopct='%.0f%%', shadow=True, startangle=90)
ax1.axis = ('Equal')
st.set_option('deprecation.showPyplotGlobalUse', False)  # colors = 'colors'
col12.header("Piechart of each Gender")
col12.pyplot()

# Histogram
# fig=plt.figure(figsize=(20,15))
# sns.histplot(data=medal_won,x=medal_won['Age'],bins=10)
# col13.header('Medal with Ages')
# col13.pyplot(fig)


fig = sns.histplot(data=without_no_medal, x="Year", bins=10)
st.set_option('deprecation.showPyplotGlobalUse', False)
col13.header('Medal with Ages')
col13.pyplot()

# season_plot
fig1 = plt.figure(figsize=(15, 20))
sns.barplot(x=season.index, y=season.values, alpha=0.8)
col14.header(' According to Season')
col14.pyplot(fig1)
# season_medal=without_no_medal.groupby('Season')['Medal'].count()
# plt.bar(season_medal.index,season_medal.values,color=['green'])
# plt.ylabel("No of Medal")
# col14.pyplot()

# st.selectbox()
# option = st.selectbox(
#   'How would you like to be contacted?',
#  ('Email', 'Home phone', 'Mobile phone'))
# st.write('You selected:', option)