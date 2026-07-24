
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="EduPro Learner Analytics",
    page_icon="📊",
    layout="wide"
)

# Load data
course = pd.read_csv("EduPro Online Platform.xlsx - Courses.csv")
user = pd.read_csv("EduPro Online Platform.xlsx - Users.csv")
transaction = pd.read_csv("EduPro Online Platform.xlsx - Transactions.csv")

# Remove accidental spaces from column names
course.columns = course.columns.str.strip()
user.columns = user.columns.str.strip()
transaction.columns = transaction.columns.str.strip()

# Merge data
df = transaction.merge(user, on="UserID", how="left")
df = df.merge(course, on="CourseID", how="left")
st.write("ALL COLUMNS:", df.columns.tolist())

# Debug: show columns
st.write("Columns in merged dataframe:")
st.write(df.columns.tolist())

# Title
st.title("EduPro Learner Analytics Dashboard")

# Calculate metrics
total_user = df["UserID"].nunique()
total_enrollment = len(df)

avg = (
    total_enrollment / total_user
    if total_user > 0
    else 0
)

# Age distribution
age_counts = df["Age"].value_counts().sort_index()

# Category distribution
category_counts = df["CourseCategory"].value_counts()

# Metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Learners", total_user)

with col2:
    st.metric("Total Enrollments", total_enrollment)

with col3:
    st.metric(
        "Average Courses/User",
        round(avg, 2)
    )
with col4:
    st.metric(
        "Most Popular Category",
        category_counts.idxmax()
    )
with col5:
    st.metric(
        "Most Popular Level",
        df["CourseLevel"].value_counts().idxmax()
    )

# Charts
st.subheader("Learners by Age")
st.bar_chart(age_counts)

st.subheader("Courses by Category")
st.bar_chart(category_counts)

st.subheader("Courses by Course Level")
st.bar_chart(
    df["CourseLevel"].value_counts()
)
!streamlit run app.py --server.address 0.0.0.0 --server.port 8501 > streamlit.log 2>&1 &
