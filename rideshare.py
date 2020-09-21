import time
import pandas as pd
import numpy as np

### Author of this code was EDUARDO COCCARO from SATX

### Code was made on ATOM and under the guidance of Udacity 

CITY_DATA = { 'chi': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'was': 'washington.csv' }
cities = ['nyc', 'chi', 'was']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['monday','tuesday','wednesday','thursday','friday',
        'saturday','sunday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_u = input('Select nyc, chi or was:\n').lower()
    while city_u not in cities:
        city_u = input('Try Again using one of the 3 options: nyc, chi or was:\n').lower()
    print('Thanks for selecting:',city_u)
    # TO DO: get user input for month (all, january, february, ... , june)
    month_u = input('Select a month:\n').lower()
    while month_u not in months:
        month_u = input('Try Again, select a month between Jan and Oct:\n').lower()
    print('Thanks for selecting:',month_u)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_u = input('Select a day:\n').lower()
    while day_u not in days:
        day_u = input('Try Again, select a days:\n').lower()
    print('Thanks for selecting:',day_u)
    print('Your search will be based on the data from {} for the month of {} in {} days'.format(city_u, month_u, day_u))
    print('-'*40)
    return city_u, month_u, day_u

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
    df = pd.read_csv(CITY_DATA[city])
    ################################################################
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['Combined'] = df['Start Station'] + ' to ' + df['End Station']
    #print(df['day_of_week'].describe())
    #print(months.index(month)+1)
    if month != 'all':
        df = df[df['month'] == months.index(month)+1]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    #################################################################
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # # convert the Start Time column to datetime
    # df['Start Time'] = pd.to_datetime(df['Start Time'])
    #
    # # extract month and day of week from Start Time to create new columns
    # df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = df['Start Time'].dt.day_name()
    # df['hour'] = df['Start Time'].dt.hour
    #print('Columnas disponibles son: ',df.columns)
    #print(df['day_of_week'].value_counts())
    # # TO DO: display the most common month
    print('the most common month was: {}\n'.format(months[df['month'].value_counts().idxmax()-1]))
    #
    # # TO DO: display the most common day of week
    print('the most common month was: {}\n'.format(df['day_of_week'].value_counts().idxmax()))
    #
    # # TO DO: display the most common start hour
    print('the most common hour to start a ride was: {}\n'.format(df['hour'].value_counts().idxmax()))
    #
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common used start station was: {}\n'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('the most common used end station was: {}\n'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print('the most common used combination was: {}\n'.format(df['Combined'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time was: {}\n'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time was: {}\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:\n{}\n'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if city != 'was':
        print('counts of Gender:\n{}\n'.format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'was':
        print('Earliest year of birth: {}\n'.format(df['Birth Year'].max()))
        print('most recent year of birth: {}\n'.format(df['Birth Year'].min()))
        print('most common year of birth: {}\n'.format(df['Birth Year'].value_counts().idxmax()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#programa de verdad
# filters = []
# #filters = get_filters()
# #raw_data = load_data(filters[0],filters[1],filters[2])
##
# raw_data = load_data('was','all','all')
# df = raw_data
# df['Start Time'] = pd.to_datetime(df['Start Time'])
# # extract month and day of week from Start Time to create new columns
# df['month'] = df['Start Time'].dt.month
# df['day_of_week'] = df['Start Time'].dt.day_name()
# df['hour'] = df['Start Time'].dt.hour
# print(df['month'].value_counts())
# print(df['day_of_week'].value_counts())
# print(df['hour'].value_counts())
# time_stats(raw_data)
##
# station_stats(raw_data)
# print('total travel time was: {}\n'.format(df['Trip Duration'].sum()))
# print('total travel time was: {}\n'.format(df['Trip Duration'].mean()))
# print('counts of user types:\n{}\n'.format(df['User Type'].value_counts()))
# print('Earliest year of birth: {}\n'.format(df['Birth Year'].max()))
# print('most recent year of birth: {}\n'.format(df['Birth Year'].min()))
# print('most common year of birth: {}\n'.format(df['Birth Year'].value_counts().idxmax()))
