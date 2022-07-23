#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month = ''
    day = ''
    months=["january", "february", "march", "april", "may", "june"]
    weekdays=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print('US bikeshare data!')
    #user input for city (chicago, new york city, washington).
    print("Would you like to see data for Chicago, New York City, or Washington?")
    # while loop to handle invalid inputs
    while(True):
        try:
            selected_option = input('Enter the city name: ').lower().strip()
        except:
            print("This is not correct city name. re-enter (chicago, new york city and washington)")
        if selected_option in CITY_DATA.keys():
            city = selected_option
            break
        else:
            print("This is not correct city name. re-enter (chicago, new york city and washington)")

    print("Would you like to filter the data by month, day, both or not at all? type 'none' for no time filter.")
    while(True):
        try:
            date_filter = input('Enter time filter: ').lower().strip()
        except:
            print("This is not a corrects filter type for the date (month, day, both or None)")
        #user input for months (all, january, february, ... , june)
        if date_filter == 'month':
            print("Which month? January, February, March, April, May, or June?")
            while(True):
                try:
                    month_filter = input('Enter a month: ').lower().strip()
                except:
                    print("This is not correct month please re-enter from (january, february, ... , june)")
                if month_filter in months:
                    month = month_filter
                    day = 'all'
                    break
                else:
                    print("This is not correct month please re-enter from (january, february, ... , june)")
            break
        # user input for days (all, monday, tuesday, ... sunday)
        elif date_filter == 'day':
            print("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            while(True):
                try:
                    day_filter = input('Enter a day: ').lower().strip()
                except:
                    print("This is not correct day please re-enter from ('sunday', 'monday', ... , saturday)")
                if day_filter in weekdays:
                    day = day_filter
                    month = 'all'
                    break
                else:
                    print("This is not a valid month please re-enter from ('sunday', 'monday', ... , saturday)")
            break
        elif date_filter == 'both':
            #user input for months (all, january, february, ... , june)
            print("Which month? January, February, March, April, May, or June?")
            while(True):
                try:
                    month_filter = input('Enter a month: ').lower().strip()
                except:
                    print("This is not corredt month please re-enter from (january, february, ... , june)")
                if month_filter in months:
                    month = month_filter
                    break
                else:
                    print("This is not correct month please re-enter from (january, february, ... , june)")
            # user input for days (all, monday, tuesday, ... sunday)
            print("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            while(True):
                try:
                    day_filter = input('Enter a day: ').lower().strip()
                except:
                    print("This is not correct day please re-enter from ('sunday', 'monday', ... , saturday)")
                if day_filter in weekdays:
                    day = day_filter
                    month = 'all'
                    break
                else:
                    print("This is not correct month. re-enter from ('sunday', 'monday', ... , saturday)")
            break
        elif date_filter == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            print("This is not correct filter. re-enter (month, day or both None)")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the city file and filters by month and day if applicable.
    Args:
        (str) city - name of the city 
        (str) month - name of the month 
        (str) day - name of the day 
    Returns:
        df - Pandas DataFrame containing city data 
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour: ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station : ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station : ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    Max = df.groupby(['Start Station', 'End Station']).count().max()[0]
    data = df.groupby(['Start Station', 'End Station']).count().reset_index()
    start_Station = data[data["User Type"] == Max]["Start Station"].values[0]
    end_Station = data[data["User Type"] == Max]["End Station"].values[0]
    print("The most most frequent combination of start station and end station trip : \nStart Station : ",start_Station, "\nEnd Station : ", end_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time : ", df["Trip Duration"].sum())
    # TO DO: display mean travel time
    print("The mean travel time : ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types :")
    userTypes = df['User Type'].value_counts()
    for userType in userTypes.index:
        print(userType, ":", userTypes[userType])

    # TO DO: Display counts of gender
    try:
        print("The counts of gender :")
        genderTypes = df['Gender'].value_counts()
        for genderType in genderTypes.index:
            print(genderType, ":", genderTypes[genderType])
    except:
        print("No Gender Data!!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth :",df["Birth Year"].min())
        print("The most recent year of birth :", df["Birth Year"].max())
        print("The most common year of birth :", df["Birth Year"].mode()[0])
    except:
        print("No Birth Year Data!!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_five_lines(df,start):
    """This Function Displays Five Lines of Raw Data of bikeshare users."""
    print('\nShowing Five Lines Of Users Data...\n')
    start_time = time.time()
    print(df.iloc[start:start+5])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print("Do you want to see the time stats of {}".format(city))
        time_stats(df)
        print("Do you want to see the station stats of {}".format(city))
        station_stats(df)
        print("Do you want to see the trip duration stats of {}".format(city))
        trip_duration_stats(df)
        print("Do you want to see the user stats of {}".format(city))
        user_stats(df)
        start = 0
        while True:
            if start == 0:
                choice = input("Do you want to see 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
                while choice not in ['yes', 'no']:
                    print("Enter a Valid Input!!!")
                    choice = input("Do you want to see 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
            else:
                choice = input("Do you want to see another 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
                while choice not in ['yes', 'no']:
                    print("Enter a Valid Input!!!")
                    choice = input("Do you want to see another 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
            if choice == 'yes':
                display_five_lines(df, start)
                start += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("You're Welcome!!".center(50,'-'))
            break


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




