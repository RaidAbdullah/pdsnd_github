import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june'] """ Array for months"""
DAY = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday'] """ Array for days"""

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
     city = input("Please enter a city (Chicago, New York City, Washington): ").lower()
     if city in CITY_DATA:
        break
     else:
        print("Invalid input. Please enter a valid city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
     month = input("Please enter a month (all, january, february, ... , june): ").lower()
     if month in MONTHS:
        break
     else:
        print("Invalid input. Please enter a valid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
     day = input("Please enter a day (all, monday, tuesday, ... sunday): ").lower()
     if day in DAY:
        break
     else:
        print("Invalid input. Please enter a valid month.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour #to use it later

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is {}\n".format(common_month) )

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is {}\n".format(common_day) )

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0] #here we use it
    print("The most common start hour is {}\n".format(common_hour) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}\n".format(common_start_station) )
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}\n".format(common_end_station) )

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip"] = df["Start Station"] + ' to ' + df['End Station']
    frequent_combination = df["Trip"].mode()[0]
    print("The most frequent combination of start station and end station trip is {}\n".format(frequent_combination) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is {}\n".format(total_travel_time) )

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is {}\n".format(mean_travel_time) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("The counts of user types is {}\n".format(user_type_count) )
    # TO DO: Display counts of gender
    if 'Gender' in df: 
        gender_count = df["Gender"].value_counts()
        print("The counts of gender is {}\n".format(gender_count) )


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       earliest_birth = df["Birth Year"].min()
       most_recent = df["Birth Year"].max()
       most_common_year = df["Birth Year"].mode()[0]
       print('Earliest birth is: {}\n'.format(earliest_birth))
       print('Most recent birth is: {}\n'.format(most_recent))
       print('Most common birth is: {}\n'.format(most_common_year) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
         """Function to display data to the user in chunks of 5 rows"""
         view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
         start_loc = 0
         while view_data.lower() == 'yes':
           rows=df.head(5)
           print(rows)     
           print(df.iloc[start_loc:start_loc+5])
           start_loc += 5
           view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
