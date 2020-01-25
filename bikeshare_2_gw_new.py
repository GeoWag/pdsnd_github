import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = str(input('What city are you interested in?\n')).lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = str(input('I am afraid that did not work. Please enter Chicago, New York City or Washington.\n')).lower()

    input_filter = str(input('Would you like to filter the data by month, day of the week of not at all?\n')).lower()
    while input_filter not in ['month', 'day of the week', 'none']:
        input_filter = str(input('I don`t understand this. Please type month, day of the week or none.\n'))
    
    if input_filter == 'month':
    
    # get user input for month (all, january, february, ... , june)
        month = str(input('Which month would like like to explore? You can select any month from January to June, or all.\n')).lower()

        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            month = str(input('I am afraid that did not work. You can choose any month from January to June, or all.\n')).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input('Which day of the week would you like to learn more about?\n')).lower()

        while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            day = str(input('I am afraid that did not work. You can choose any day from Monday to Sunday, or all.\n')).lower()
    
    elif input_filter == 'day of the week':
        day = str(input('Which day of the week would you like to learn more about?\n')).lower()

        while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            day = str(input('I am afraid that did not work. You can choose any day from Monday to Sunday, or all.\n')).lower()
        
        month = str(input('Which month would like like to explore? You can select any month from January to June, or all.\n')).lower()

        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            month = str(input('I am afraid that did not work. You can choose any month from January to June, or all.\n')).lower()
    
    else:
         month = 'all'
         day = 'all'
         print('\nAll right, we will not do any filtering.')
        
    
    
    
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
    df = pd.read_csv(CITY_DATA[city])    

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common month: ', popular_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', popular_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour    
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start)
    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end
          )
    # display most frequent combination of start station and end station trip
    df['trip'] = [str(x) + ' to ' + str(y) for x,y in zip(df['Start Station'], df['End Station'])]     
    popular_trip = df['trip'].mode()[0]
    print('The most popular route among users is: ', popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum() // 3600 
    print('Total travel time in hours: ', total_time)

    # display mean travel time
    avg_time = df['Trip Duration'].mean() // 60
    print('Mean travel time in minutes: ', avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Here, we have to differentiate between NYC/Chicago and Washington, because some columns don't exist in washington.csv.
    # This is done using and if clause and the amount of columns

    if df.shape[1] > 12:
        
    # Display counts of user types
        user_type_count = df['User Type'].value_counts()    
        print('\nDifferent types of users: ', user_type_count)
    
    # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\nGender distribution: ', gender_count)
    
    # Display earliest, most recent, and most common year of birth
        min_birth_year = df['Birth Year'].min()
        popular_birth_year = df['Birth Year'].mode()[0]
        max_birth_year = df['Birth Year'].max()
        print('\nBirth year of oldest user: ', min_birth_year)
        print('\nBirth year of the youngest user: ', max_birth_year)
        print('\nMost common birth year: ', popular_birth_year)
    
    else:
        user_type_count = df['User Type'].value_counts()    
        print('\nDifferent types of users: ', user_type_count)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)

        while True:            
            if raw == 'no':
                break
            print(df[i:i+5])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
