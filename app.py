
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('UTKFace_age_gender_dataset.csv')

st.title("Age & Gender Data Analysis – UTKFace")

st.markdown("""
This app allows you to explore the UTKFace dataset, containing age and gender information.
""")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Age Distribution
st.subheader("Age Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='age', bins=10, kde=True, color='skyblue', ax=ax1)
st.pyplot(fig1)

# Gender Countplot
st.subheader("Gender Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='gender', palette='pastel', ax=ax2)
ax2.set_xticklabels(['Male', 'Female'])
st.pyplot(fig2)

# Age by Gender Histogram
st.subheader("Age Distribution by Gender")
fig3, ax3 = plt.subplots()
sns.histplot(data=df, x='age', hue='gender', multiple='stack', kde=True, palette='pastel', ax=ax3)
ax3.legend(title='Gender', labels=['Male', 'Female'])
st.pyplot(fig3)

# Average Age by Gender
st.subheader("Average Age by Gender")
fig4, ax4 = plt.subplots()
sns.barplot(data=df, x='gender', y='age', estimator='mean', ci='sd', palette='muted', ax=ax4)
ax4.set_xticklabels(['Male', 'Female'])
st.pyplot(fig4)

# Age Trend Line
st.subheader("Age Trend Over Sample Index")
fig5, ax5 = plt.subplots()
sns.lineplot(data=df, x=df.index, y='age', hue='gender', palette='Set2', ax=ax5)
ax5.set_xlabel("Sample Index")
st.pyplot(fig5)

# Summary
st.markdown("### Key Insights")
st.markdown("""
- Age ranges from 22 to 60, mostly distributed evenly.
- Slight female majority (4 females vs 3 males).
- Average female age is higher than male.
- Age trends show more variation in male data.
""")

