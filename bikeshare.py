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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which City? (Chicago, New York City or Washington)").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Not an appropriate choice.")
        else:
            break
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? (any one of the first 6 months or enter All to select all 6)").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Not an appropriate choice.")
        else:
            break
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which Day of the week (or all)").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Not an appropriate choice.")
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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    #filter day of weekif applicable
    if day != 'all':
    #filter by day of week to create new dataframe
       df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
        # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day:', popular_day)
        # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time).round())
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_sstation)

    # TO DO: display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_estation)

    # TO DO: display most frequent combination of start station and end station trip
    popular_route = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most Popular Start and End Station:', popular_route)
    print("\nThis took %s seconds." % (time.time() - start_time).round())
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time: (seconds)', total_time.round())
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time: (seconds)', mean_time.round())
    print("\nThis took %s seconds." % (time.time() - start_time).round())
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if city == 'new york city' or city == 'chicago':
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print('Everyone in Washington is of an undefined or non-binary gender.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'new york city' or city == 'chicago':
        earliest_year = df['Birth Year'].min()
        print('Earliest Birth Year', int(earliest_year))
        recent_year = df['Birth Year'].max()
        print('Most Recent Birth Year', int(recent_year))
        common_year = df['Birth Year'].mode()
        print('Most Common Birth Year', int(common_year))
        print("\nThis took %s seconds." % (time.time() - start_time).round())
        print('-'*40)
    else:
        print('Everyone in Washington does not wish their birth year/age known.')
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() = 'no':
            break
        elif restart.lower() != 'yes':
            print('Please, try again. (Yes/No)')

    i=0
    five_rows = df.iloc[:i+5]
    print(five_rows)
    i+=5
    while True:
        display_more = input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
        if display_more == 'yes':
            five_rows = df.iloc[i:i+5]
            print(five_rows)
            i+= 5
        else:
           break

if __name__ == "__main__":
	main()
