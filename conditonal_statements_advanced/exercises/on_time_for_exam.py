exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

time_of_exam = exam_hour * 60 + exam_minute
time_of_arrival = arrival_hour * 60 + arrival_minute

if time_of_exam < time_of_arrival:
    print("Late")
elif time_of_arrival >= time_of_exam - 30:
    print("On time")
elif time_of_arrival <= time_of_exam + 30:
    print("Early")

difference = abs(time_of_arrival - time_of_exam)

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{difference} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    hour = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hour}:0{minutes} hours before the start")
    else:
        print(f"{hour}:{minutes} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f"{difference} minutes after the start")
elif time_of_exam + 60 <= time_of_arrival:
    hour = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hour}:0{minutes} hours after the start")
    else:
        print(f"{hour}:{minutes} hours after the start")