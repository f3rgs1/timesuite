import time

def current_time():
    # Get the current local time
    currentTime = time.localtime(time.time())

    # Extract the hours, minutes, and seconds
    currentHour = currentTime.tm_hour
    currentMinute = currentTime.tm_min
    currentSecond = currentTime.tm_sec

    # Display the results
    print("Current time is", currentHour,":", currentMinute,":",currentSecond)

current_time()
