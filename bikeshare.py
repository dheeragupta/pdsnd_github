import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all'}
daysoftheweek = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'}

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
    while True:
      city = str(input("\nSelect city: New York City, Chicago or Washington? - ")).lower()
      if city not in CITY_DATA:
        print("City not found. Try again.")
        continue
      else:
        break

    # get user input for month (all, january, february, ... , june)
    while True:
      month = str(input("\nSelect month: January, February, March, April, June or type 'all' to select all months - ")).lower()
      if month not in months:
        print("Invalid month input. Try again.")
        continue
      else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = str(input("\nSelect day of week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all' to select all days of the week - ")).lower()
      if day in daysoftheweek:
          print("Invalid daysoftheweek input. Try again.")
          continue
      else:
          break

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

    #read file
    df = pd.read_csv(CITY_DATA[city])

    #convert data type for 'start time' column to datetime and extract month and day of the week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    #apply filter on month
    if month == 'all':
        pass
    else:
        month_num = months.index(month)
        df = df[df['Month'] = month_num]

    #apply day of the week filter
    if day == 'all':
        pass
    else:
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most common Month: ', most_common_month)

    # display the most common day of week
    most_common_dayofweek = df['Day of Week'].mode()[0]
    print('Most common day of week: ', most_common_dayofweek)

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print('Most common hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', most_common_start_station')

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost Common end station: ', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start-End-Combo'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_start_end_combo = df['Start-End-Combo'].mode().[0]
    print('Most frequent start and end station combination: ', most_common_start_end_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print ('Total travel time:',
            str(int(total_travel_time//86400)) + ' days ' +
            str(int((total_travel_time%86400//3600)) + ' hrs' +
            str(int(((total_travel_time%86400)%3600)//60)) + 'min')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:' str(int(mean_travel_time//60)) + ' min ' + str(int(mean_travel_time%60)) + ' sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print ('Gender:\n', gender)

    except:
        print ('Gender value not available')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_yr_of_birth = str(int(df['Birth Year']).min())
        print('Earliest year of birth: ', earliest_yr_of_birth)

        most_recent_yr_of_birth = str(int(df['Borth Year']).max())
        print('Most recent year of birth: ', most_recent_yr_of_birth)

        most_common_yr_of_birth = str(int(df['Birth Year'].mode()[0]))
        print('Most common year of birth: ', most_recent_yr_of_birth)

    except:
        print('Birth year value not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df, head = 0, tail = 5):
    """Displays 5 lines of raw data at a time upon request from user. Continue displaying until user asks to stop.
    Args:
        data frame
        start index
        end index
    Returns:
        none
    """

    while True:
        print("\n")
        print(df.iloc[head:tail].to_string())
        print("\n")

        display_trips = str(input("\nType 'yes' to continue viewing individual trip data. Press any other key to proceed to statistics: ")).lower()
        if display_trips == 'yes':
            head = tail + 1
            tail = tail + 5
            display_data(df, head, tail)
        else:
            break
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_rawdata = str(input("\nWould you like to view individual trip data? Type 'yes' to view trip data. Press any other key to proceed to statistics: ")).lower()
        if display_rawdata == 'yes':
            display_data(df)
        else:
            pass

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
