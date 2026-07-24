
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="EduPro Learner Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    course = pd.read_csv(
        "EduPro Online Platform.xlsx - Courses.csv"
    )

    user = pd.read_csv(
        "EduPro Online Platform.xlsx - Users.csv"
    )

    transaction = pd.read_csv(
        "EduPro Online Platform.xlsx - Transactions.csv"
    )

    # Remove accidental spaces
    course.columns = course.columns.str.strip()
    user.columns = user.columns.str.strip()
    transaction.columns = transaction.columns.str.strip()

    # Merge Transactions + Users
    df = transaction.merge(
        user,
        on="UserID",
        how="left"
    )

    # Merge with Courses
    df = df.merge(
        course,
        on="CourseID",
        how="left"
    )

    return df


df = load_data()


# =========================================================
# CREATE AGE GROUP
# =========================================================

bins = [0, 18, 26, 36, 46, float("inf")]

labels = [
    "0-18",
    "19-25",
    "26-35",
    "36-45",
    "46+"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels,
    right=False
)


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.title("🔎 Dashboard Filters")

# Age Group Filter
age_options = sorted(
    df["AgeGroup"].dropna().unique().tolist()
)

selected_age = st.sidebar.multiselect(
    "Select Age Group",
    options=age_options,
    default=age_options
)


# Gender Filter
gender_options = sorted(
    df["Gender"].dropna().unique().tolist()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=gender_options,
    default=gender_options
)


# Course Category Filter
category_options = sorted(
    df["CourseCategory"].dropna().unique().tolist()
)

selected_category = st.sidebar.multiselect(
    "Select Course Category",
    options=category_options,
    default=category_options
)


# Course Level Filter
level_options = sorted(
    df["CourseLevel"].dropna().unique().tolist()
)

selected_level = st.sidebar.multiselect(
    "Select Course Level",
    options=level_options,
    default=level_options
)


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df[
    (df["AgeGroup"].isin(selected_age)) &
    (df["Gender"].isin(selected_gender)) &
    (df["CourseCategory"].isin(selected_category)) &
    (df["CourseLevel"].isin(selected_level))
]


# =========================================================
# TITLE
# =========================================================

st.title("📊 EduPro Learner Analytics Dashboard")

st.write(
    "Explore learner demographics, enrollment behavior, "
    "course preferences, and learner segments."
)


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_users = filtered_df["UserID"].nunique()

total_enrollments = len(filtered_df)

average_courses = (
    total_enrollments / total_users
    if total_users > 0
    else 0
)

# Most popular category
if len(filtered_df) > 0:
    most_popular_category = (
        filtered_df["CourseCategory"]
        .value_counts()
        .idxmax()
    )
else:
    most_popular_category = "N/A"


# Most popular level
if len(filtered_df) > 0:
    most_popular_level = (
        filtered_df["CourseLevel"]
        .value_counts()
        .idxmax()
    )
else:
    most_popular_level = "N/A"


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Learners",
        total_users
    )

with col2:
    st.metric(
        "Total Enrollments",
        total_enrollments
    )

with col3:
    st.metric(
        "Average Courses / Learner",
        round(average_courses, 2)
    )

with col4:
    st.metric(
        "Most Popular Category",
        most_popular_category
    )

with col5:
    st.metric(
        "Most Popular Level",
        most_popular_level
    )


# =========================================================
# SECTION 1: LEARNER DEMOGRAPHICS
# =========================================================

st.header("👥 Learner Demographics")


col1, col2 = st.columns(2)


# Age Group Distribution
with col1:

    st.subheader("Learners by Age Group")

    age_group_counts = (
        filtered_df["AgeGroup"]
        .value_counts()
        .reindex(labels, fill_value=0)
    )

    st.bar_chart(age_group_counts)


# Gender Distribution
with col2:

    st.subheader("Gender Participation")

    gender_counts = (
        filtered_df["Gender"]
        .value_counts()
    )

    st.bar_chart(gender_counts)


# =========================================================
# SECTION 2: ENROLLMENT ANALYSIS
# =========================================================

st.header("📚 Enrollment Analysis")


col1, col2 = st.columns(2)


# Age-wise Enrollment
with col1:

    st.subheader("Enrollments by Age Group")

    age_enrollment = (
        filtered_df["AgeGroup"]
        .value_counts()
        .reindex(labels, fill_value=0)
    )

    st.bar_chart(age_enrollment)


# Course Category
with col2:

    st.subheader("Course Category Popularity")

    category_counts = (
        filtered_df["CourseCategory"]
        .value_counts()
    )

    st.bar_chart(category_counts)


# =========================================================
# SECTION 3: COURSE TYPE AND LEVEL
# =========================================================

st.header("🎓 Course Preference Analysis")


col1, col2 = st.columns(2)


# Course Type
with col1:

    st.subheader("Course Type Popularity")

    course_type_counts = (
        filtered_df["CourseType"]
        .value_counts()
    )

    st.bar_chart(course_type_counts)


# Course Level
with col2:

    st.subheader("Course Level Preference")

    level_counts = (
        filtered_df["CourseLevel"]
        .value_counts()
    )

    st.bar_chart(level_counts)


# =========================================================
# SECTION 4: AGE GROUP VS COURSE CATEGORY
# =========================================================

st.header("🔥 Demographics × Course Preference")

st.subheader(
    "Age Group vs Course Category Enrollment"
)

pivot_age_category = pd.crosstab(
    filtered_df["AgeGroup"],
    filtered_df["CourseCategory"]
)

pivot_age_category = pivot_age_category.reindex(
    labels,
    fill_value=0
)


# Heatmap
fig, ax = plt.subplots(
    figsize=(12, 5)
)

sns.heatmap(
    pivot_age_category,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=ax
)

ax.set_xlabel("Course Category")
ax.set_ylabel("Age Group")

st.pyplot(
    fig,
    use_container_width=True
)


# =========================================================
# SECTION 5: GENDER VS COURSE LEVEL
# =========================================================

st.subheader(
    "Gender vs Course Level Enrollment"
)

pivot_gender_level = pd.crosstab(
    filtered_df["Gender"],
    filtered_df["CourseLevel"]
)

st.dataframe(
    pivot_gender_level,
    use_container_width=True
)

st.bar_chart(
    pivot_gender_level
)


# =========================================================
# SECTION 6: GENDER PARTICIPATION RATIO
# =========================================================

st.header("⚖️ Gender Participation Ratio")

gender_ratio = (
    filtered_df["Gender"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

st.dataframe(
    gender_ratio.rename("Percentage (%)"),
    use_container_width=True
)


# =========================================================
# SECTION 7: TOP 10 ACTIVE USERS
# =========================================================

st.header("🏆 Enrollment Concentration Among Active Users")

top_users = (
    filtered_df["UserID"]
    .value_counts()
    .head(10)
)

st.subheader(
    "Top 10 Users by Number of Enrollments"
)

st.bar_chart(top_users)


# =========================================================
# SECTION 8: BEGINNER VS ADVANCED
# =========================================================

st.header("📈 Beginner vs Advanced Learner Behavior")


level_behavior = (
    filtered_df["CourseLevel"]
    .value_counts()
)

st.bar_chart(
    level_behavior
)


# =========================================================
# SECTION 9: DATA SUMMARY
# =========================================================

st.header("📋 Filtered Data Summary")

st.write(
    f"Showing **{len(filtered_df):,} enrollments** "
    f"from **{filtered_df['UserID'].nunique():,} learners**."
)

st.dataframe(
    filtered_df,
    use_container_width=True
)
