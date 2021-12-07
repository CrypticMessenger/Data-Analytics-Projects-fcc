import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df1=df[df['sex']=='Male']
    average_age_men = round(df1['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    df1=df[df['education']=='Bachelors']
    percentage_bachelors = round((df1.shape[0]/df.shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df2=df[((df['education'] == 'Bachelors' )|( df['education'] == 'Masters' )|( df['education'] == 'Doctorate'))]
    higher_education =df2.shape[0]
    df2=df[~((df['education'] == 'Bachelors' )|( df['education'] == 'Masters' )|( df['education'] == 'Doctorate'))]
    lower_education = df2.shape[0]

    # percentage with salary >50K
    df2=df[((df['education'] == 'Bachelors' )|( df['education'] == 'Masters' )|( df['education'] == 'Doctorate'))]
    higher_education_rich = round((df2[df2['salary']=='>50K'].shape[0])*100/df2.shape[0],1)

    df2=df[~((df['education'] == 'Bachelors' )|( df['education'] == 'Masters' )|( df['education'] == 'Doctorate'))]

    lower_education_rich = round((df2[df2['salary']=='>50K'].shape[0])*100/df2.shape[0],1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df1=df[df['hours-per-week']==1]
    df2=df1[df1['salary']=='>50K']

    num_min_workers = df1.shape[0]

    rich_percentage = (df2.shape[0])*100/(df1.shape[0])

    # What country has the highest percentage of people that earn >50K?
    df1=df[df['salary']=='>50K']
    df3=df1['native-country'].value_counts()
    l=df3.index.tolist()
    df4=df['native-country'].value_counts()
    max=0
    countrymax=""
    for country in l:
      if((df3[country]/df4[country])>max):
        max=df3[country]/df4[country]
        countrymax=country
    highest_earning_country = countrymax
    highest_earning_country_percentage = round(max*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    df1=df[df['native-country']=='India']
    df1=df1[df1['salary']=='>50K']
    job=''
    max=0
    l=df1['occupation'].unique().tolist()
    for j in l:
      if(len(df1[df1['occupation']==j])>=max):
        job=j
        max=len(df1[df1['occupation']==j])

    top_IN_occupation = job

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
