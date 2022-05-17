import time
import pandas as pd
import numpy as np
#avialble cities data 
city_data={'ch':'chicago.csv',
           'ny':'new_york_city.csv',
           'wa':'washington.csv'}
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

    #ask user for city needed and validate the answer
    while True:
        city= input ("pleas select one city you want to show data in \n ch for chicago \n ny for new york \n wa for washington\n : ").lower()
        if city in city_data.keys():  
            break
        else:
            print("oh sorry ! you have to select one of avialbe cities" )
        city = input ("pleas select one city you want to show data in \n ch for chicago \n ny for new york \n wa for washington\n : ").lower()
  
    # TO DO: get user input for month (all, january, february, ... , june)
    #ask user for the month and validat the answer
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month= input ("please select the month you want show data from'january', 'february', 'march', 'april', 'may', 'june','all' :").lower()
        if month in months:
            break
        else:
            print ("oh sorry !please select on from the list ")
            month= input ("please select the month you want show data from'january', 'february', 'march', 'april', 'may', 'june','all': \n:").lower()
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #ask user for the day in the week 
    week=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    while True:
        day=input("please insert the day of the week you need filter by it from this list \n 'saturday','sunday','monday','tuesday','wednesday','thursday','friday','all':")
                  
        if day in week :
            break
        else :
            print ( "oh sorry! you enterd wrong day...." )
            day=input("please insert the day of the week you need filter by it from this list \n'saturday','sunday','monday','tuesday','wednesday','thursday','friday':")
                  
            
    

    print('-'*40)
    return city,month,day

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
    df = pd.read_csv(city_data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # in case we need filter by index or numbers 
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month=months.index(month)+1
         # filter by month to create the new dataframe
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
        print(df.columns)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("Most common month is :",common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print ("Most common day is :",common_day)

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("Most common hour is:",common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station =df['Start Station'].mode()[0]
    print("Most common start station is:",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station =df['End Station'].mode()[0]
    print("Most common end station is:",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip_stations']=df['Start Station']+df['End Station']
    most_trip_station=df['trip_stations'].mode()[0]
    print("most frequent combination is :",most_trip_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    #dispaly time in minets
    print("Total travel time is :{} min".format(total_travel_time/60))

    # TO DO: display mean travel time
    avrage_travel_time=df['Trip Duration'].mean()
    #dispaly time in minets
    print("Avrage travel time is :{} min".format(avrage_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print("Cont of user types is : \n",user_type)
    
    # TO DO: Display counts of gender
    #display count of gender in NYC and chicago 
    if 'Gender' in df:
        count_of_gender=df['Gender'].value_counts()
        print('Count of gender is : \n',count_of_gender)
    else:
        print ('No avialabel data for users gender in this city  ')
    
    # TO DO: Display earliest, most recent, and most common year of birth
   #check if file contain the birth coulumn and get result as interger 
    if 'Birth Year' in df :
        earliest_birth=int(df['Birth Year'].min())
        most_recent_birth=int(df['Birth Year'].max())
        most_common_birth=int(df['Birth Year'].mode())
        print("Earlist birth year of users is:",earliest_birth)
        print("The most recent birth year of users is: ",most_recent_birth)
        print("The most common birth year of users is:",most_common_birth)
    else:
        print('No avialbel data for birth yaer in this file ')
        

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
