import time

def get_time_remaining_in_day():
    # Get the current local time
    currentTime = time.localtime(time.time())

    # Calculate the seconds passed since midnight
    seconds_since_midnight = currentTime.tm_hour * 3600 + currentTime.tm_min * 60 + currentTime.tm_sec

    # Calculate the seconds in a day (24*60*60 = 86400)
    seconds_in_a_day = 24 * 60 * 60

    # Calculate the seconds remaining in the day
    seconds_remaining = seconds_in_a_day - seconds_since_midnight

    # Calculate the hours, minutes and seconds remaining
    hoursRemaining, remainder = divmod(seconds_remaining, 3600)
    minutesRemaining, secondsRemaining = divmod(remainder, 60)

    # Display the results
    print("Time remaining in the day:", hoursRemaining, "hours", minutesRemaining, "minutes", secondsRemaining, "seconds")

get_time_remaining_in_day()