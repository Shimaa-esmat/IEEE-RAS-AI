import time
import pandas as pd
import numpy as np

# dictionary containing the data for the three cities to allow user to chose city by its name
access_city = {"chicago": "chicago.csv",
               "new york": "new_york_city.csv", "washington": "washington.csv"}


def access_data():
    """
    functon to access data by user
    access city ,month and day
    check the validity of user in
    Returns:
        str (city): name of the city
        str (month): name of the month and filtered it
        str (day): name of the day of week and filtered it
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # empty city to run the loop
    city = ''
    # make loop to ensure user access the correct input
    while city not in access_city.keys():
        city = input(
            "Please choose a city (Chicago, New York, Washington):\n")
        # convert any data to lower to fit data file
        city = city.lower()

        if city not in access_city.keys():
            city = input(
                "please enter city like (Chicago, New York, Washington):\n")

    # dictionary to store all the months including the 'all' option
    months = {'january': 1, 'february': 2, 'march': 3,
              'april': 4, 'may': 5, 'june': 6, 'all': 7}
    # empty input to run the loop
    month = ''

    # make loop to ensure user access the correct input
    while month not in months.keys():
        month = input("Which Month (all, january, ... june)?:\n").lower()

        if month not in months.keys():
            month = input(
                "please enter month like (all, january, ... june)?: \n ")

    # dictionary to store all the months including the 'all' option
    days = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    # empty input to run the loop
    day = ''
    # make loop to ensure user access the correct input
    while day not in days:
        day = input("Which day? (all, monday, tuesday, ... sunday):\n")
        day = day.lower()

        if day not in days:
            day = input(
                "please enter day like (all, monday, tuesday, ... sunday):\n ")
    # print all data access
    print(
        f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    # Returning the city, month and day selections
    return city, month, day

# Function to load data from .csv files


def load_data(city, month, day):
    """
     Loads data for city and filters by month and day
     arg:
        param city: name of the city
        param month: name of the month
        param day: name of the day
    return:
        df : pandas dataframre
    """
    # Load data for city
    df = pd.read_csv(access_city[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month, day  and hour of week from Start Time to create new columns
    # df['month'] = df['Start Time'].dt.month
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # Filter by month
    if month != 'all':
        # Use the index of the months list to get int
        # months1 = ['january', 'february', 'march', 'april', 'may', 'june']
        # month = months1.index(month) + 1
        # Filter by month to create the new dataframe
        df = df[df['month'] == month.title()]
    # Filter by day
    if day != 'all':

        df = df[df['day'] == day.title()]

    # Returns the selected file as a dataframe (df) with new columns
    return df

# Function to calculate all the time-related statistics


def popular_time(df):
    """
    apply statistics on the most frequent times of travel.

    Args:
        param1 (df): The data frame user input

    Returns:
        None.
    """

    start_time = time.time()

    print('\nCalculating The Most Popular Times of Travel...\n')

    # mode to find the most popular month
    print("Most Popular Month: ", df["month"].mode()[0])
    # mode to find the most popular day
    print("Most Day Of Week:", df["day"].mode()[0])
    # mode to find the most popular hour
    print("Most Common Start Hour:", df["hour"].mode()[0])

    # Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")

    print('-'*40)

# Function to calculate station statistics


def popular_station(df):
    """
    apply statistics on the most popular stations and trip.

        Args:
            param1 (df): The data frame user input

        Returns:
            None.
        """
    start_time = time.time()

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # mode to find the most common start station
    print("Most Start station", df["Start Station"].mode()[0])
    # mode to find the most common end station
    print("Most End station", df["End Station"].mode()[0])

    # str.cat to combine two columsn in the df
    # new colonm ['start to end']
    df['Start To End'] = df['Start Station'].str.cat(
        df['End Station'], sep=' to ')
    # mode on this new column to find out the most common combination of start and end stations
    freq = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {freq}.")

    # Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")

    print('-' * 40)

# Function for trip duration statistics


def TripDuration(df):
    """
    apply statistics on the total and average trip duration.

     Args:
         param1 (df): The data frame user input

     Returns:
         None.
     """
    start_time = time.time()

    # display total travel time
    df["Trip Duration"] = pd.to_numeric(df["Trip Duration"])
    # sum to calculate the total trip duration
    total_time = df["Trip Duration"].sum()
    print("\nTotal Travel Time (seconds):", total_time)
    # display mean travel time
    average_time = df["Trip Duration"].mean()
    print("\nAverage Travel Time (seconds):", average_time)

    # Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")

    print('-'*40)

# Function to calculate user statistics


def userInfo(df):
    """
    apply statistics on bikeshare users.

       Args:
           param1 (df): The data frame user input

       Returns:
           None.
       """
    start_time = time.time()

    # The total users are counted
    user_type_counts = df["User Type"].value_counts()
    print("Counts of each user type:")
    print(user_type_counts)
    # not all files have gender column
    try:
        # The total genders are counted
        gender_counts = df["Gender"].value_counts()
        print("Counts of each gender:")
        print(gender_counts)
    except:
        print("\nThere is no 'Gender' column in this file.")

    # not all files have birth year column
    try:
        df["Birth Year"] = pd.to_numeric(df["Birth Year"], errors="coerce")
        earliest_year_of_birth = df["Birth Year"].min()
        most_recent_year_of_birth = df["Birth Year"].max()
        most_common_year_of_birth = df["Birth Year"].mode()[0]
        print("Earliest year of birth: {}".format(int(earliest_year_of_birth)))
        print("Most recent year of birth: {}".format(
            int(most_recent_year_of_birth)))
        print("Most common year of birth: {}".format(
            int(most_common_year_of_birth)))
    except:
        print("\nThere is no 'Birthday' column in this file.")

    # Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")

    print('-' * 40)

# Main function to call all the previous functions


def main():
    while True:

        city, month, day = access_data()
        df = load_data(city, month, day)

        popular_time(df)
        popular_station(df)
        TripDuration(df)
        userInfo(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
