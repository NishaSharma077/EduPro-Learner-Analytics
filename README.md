# 📊 EduPro Learner Analytics Dashboard

## 📌 Project Overview

The **EduPro Learner Analytics Dashboard** is a data analysis and visualization project that explores learner demographics and course enrollment behavior on an online learning platform.

The project uses learner, course, and transaction data to identify patterns in learner participation, course preferences, and enrollment behavior. An interactive **Streamlit dashboard** was developed to present the analysis in an easy-to-understand and interactive format.

The project focuses on **descriptive learner intelligence** and aims to support data-driven decision-making for course planning, learner engagement, and inclusive educational strategies.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze learner demographics across different age groups.
- Understand gender participation on the platform.
- Identify the most popular course categories.
- Analyze course type and course level preferences.
- Examine enrollment patterns across different age groups.
- Identify relationships between learner demographics and course preferences.
- Compare gender and course-level enrollment patterns.
- Identify highly active learners based on enrollment activity.
- Build an interactive dashboard for exploring learner behavior.

---

## 📂 Dataset

The project uses three datasets:

### 1. Users Dataset

Contains learner demographic information:

- `UserID`
- `UserName`
- `Age`
- `Gender`

### 2. Courses Dataset

Contains information about available courses:

- `CourseID`
- `CourseName`
- `CourseCategory`
- `CourseType`
- `CourseLevel`

### 3. Transactions Dataset

Contains learner enrollment transactions:

- `TransactionID`
- `UserID`
- `CourseID`
- `TransactionDate`

The datasets are integrated using:

- `UserID` → Connects Users and Transactions
- `CourseID` → Connects Courses and Transactions

---

## 🔍 Key Analytical Questions

This project aims to answer the following questions:

1. What is the age distribution of learners on EduPro?
2. Which age groups have the highest enrollment activity?
3. How is learner participation distributed by gender?
4. Which course categories attract the highest enrollments?
5. Which course types are most popular?
6. Which course levels are preferred by learners?
7. Do different age groups prefer different course categories?
8. Are there gender-based differences in course-level preferences?
9. How many courses does the average learner enroll in?
10. Which learners have the highest enrollment activity?

---

## 🛠️ Technologies Used

The project was developed using:

- **Python**
- **Pandas** – Data cleaning and analysis
- **NumPy** – Data processing
- **Matplotlib** – Data visualization
- **Seaborn** – Heatmaps and statistical visualization
- **Streamlit** – Interactive web dashboard
- **GitHub** – Project version control and hosting
- **Google Colab / Jupyter Notebook** – Data analysis and exploration

---

## 📊 Key Performance Indicators (KPIs)

The dashboard provides the following KPIs:

- **Total Learners**
- **Total Enrollments**
- **Average Courses per Learner**
- **Most Popular Course Category**
- **Most Popular Course Level**
- **Gender Participation Ratio**

These KPIs provide a quick overview of learner engagement and course demand.

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

### 👥 Learner Demographics
- Learner distribution by age group
- Gender participation analysis

### 📚 Enrollment Analysis
- Enrollment by age group
- Course category popularity
- Course type popularity
- Course level preference

### 🔥 Demographic Course Preferences
- Age Group × Course Category heatmap
- Gender × Course Level analysis

### 🏆 Learner Engagement
- Top 10 active learners
- Average courses per learner
- Enrollment concentration analysis

### 🔎 Interactive Filters

Users can filter dashboard results by:

- Age Group
- Gender
- Course Category
- Course Level

---

## 📊 Age Group Segmentation

Learners are grouped into the following age bands:

| Age Group |
|-----------|
| 0–18 |
| 19–25 |
| 26–35 |
| 36–45 |
| 46+ |

This segmentation helps compare enrollment behavior across different learner demographics.

---

## 🔄 Data Analysis Workflow

```text
Raw Datasets
     │
     ▼
Data Cleaning
     │
     ▼
Users + Transactions + Courses
     │
     ▼
Data Integration
     │
     ▼
Age Group Segmentation
     │
     ▼
Exploratory Data Analysis
     │
     ├── Demographic Analysis
     ├── Enrollment Analysis
     ├── Course Preference Analysis
     └── Behavioral Analysis
     │
     ▼
Data Visualization
     │
     ▼
Interactive Streamlit Dashboard
