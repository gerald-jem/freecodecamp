import pandas as pd

def demographic_data_analyzer():
    # Read data
    df = pd.read_csv("adult.data.csv", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", 
        "marital-status", "occupation", "relationship", "race", 
        "sex", "capital-gain", "capital-loss", "hours-per-week", 
        "native-country", "salary"
    ])
    
    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    percentage_advanced_education_rich = round((df[advanced_education & (df["salary"] == ">50K")].shape[0] /
                                                df[advanced_education].shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    non_advanced_education = ~advanced_education
    percentage_non_advanced_education_rich = round((df[non_advanced_education & (df["salary"] == ">50K")].shape[0] /
                                                    df[non_advanced_education].shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers[min_workers["salary"] == ">50K"].shape[0] /
                             min_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_earnings = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_counts = df["native-country"].value_counts()
    highest_earning_country = (country_earnings / country_counts).idxmax()
    highest_earning_country_percentage = round((country_earnings / country_counts).max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_occupation = (df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
                        ["occupation"].value_counts().idxmax())

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "percentage_advanced_education_rich": percentage_advanced_education_rich,
        "percentage_non_advanced_education_rich": percentage_non_advanced_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "india_occupation": india_occupation
    }
