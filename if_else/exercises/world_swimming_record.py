record_in_seconds = float(input())
distance_in_meters = float(input())
time_seconds_one_meter = float(input())

swimming = distance_in_meters * time_seconds_one_meter

distance_in_meters = (distance_in_meters // 15) * 12.5

total_time = swimming + distance_in_meters

if record_in_seconds < total_time:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} "
          f"seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record"
          f" is {swimming + distance_in_meters:.2f} seconds.")