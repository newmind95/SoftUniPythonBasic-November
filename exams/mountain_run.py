from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

needed_climbing = distance_in_meters * time_in_seconds_for_one_meter

time = floor((distance_in_meters / 50)) * 30
total_time = needed_climbing + time

difference = abs(total_time - record_in_seconds)

if record_in_seconds <= total_time:
    print('No! He was %.2f seconds slower.' % (difference))
else:
    print('Yes! The new record is %.2f seconds.' % total_time)
