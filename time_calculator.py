DAYS = ['Monday', 'tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturDay', 'Sunday']   # list of days in week
import re

def add_time(start, duration, day=''):
    start_lst = re.split('[: ]', start)  #   list of start time
    dur_lst = duration.split(':')   #   list of start time
    # breakdown into components of time
    hours_start, minutes_start, half_of_day = int(start_lst[0]), int(start_lst[1]), start_lst[2]
    hours = hours_start + int(dur_lst[0])   # sum of result hours
    minutes = minutes_start + int(dur_lst[1])   # sum of result minutes

    if minutes//60 > 0:     # check hours in minutes
        hours += 1
        minutes -= 60

    days_later = ''
    num_of_halfs_days = hours//12

    # if num_of_halfs_days == 0 the answer is ready
    if num_of_halfs_days != 0:
        if num_of_halfs_days == 1:  # change half of day if num_of_halfs_days == 1
            if half_of_day == 'PM':
                half_of_day = 'AM'
                days_later = ' (next day)'
                hours -= 12 * num_of_halfs_days
            else:
                half_of_day = 'PM'
                hours -= 12 * num_of_halfs_days

        elif num_of_halfs_days == 2:     # change day if num_of_halfs_days == 2
            days_later = ' (next day)'
            hours -= 12*num_of_halfs_days

        elif num_of_halfs_days % 2 == 0:  # change day if num_of_halfs_days is even
            days_later = f' ({num_of_halfs_days//2} days later)'
            hours -= 12 * num_of_halfs_days
        else:                              # change day and half of day if num_of_halfs_days is not even
            if half_of_day == 'PM':
                half_of_day = 'AM'
                days_later = f' ({num_of_halfs_days//2+1} days later)'
                hours -= 12 * num_of_halfs_days
            else:
                half_of_day = 'PM'
                days_later = f' ({num_of_halfs_days // 2 } days later)'
                hours -= 12 * num_of_halfs_days

    if day:     # change day of week in
        num_day = DAYS.index(day)
        if start_lst[2] == 'PM' and num_of_halfs_days % 2 == 1:
            day = ', ' + DAYS[(num_day+num_of_halfs_days//2+1) % 7]
        else:
            day = ', ' + DAYS[(num_day + (num_of_halfs_days) // 2) % 7]

    if hours == 0:  # change 0:00 AM to 12:00 AM
        hours += 12
    new_time = str(hours)+':' + f'{minutes:0>2}' + ' ' + half_of_day + day + days_later

    return new_time
