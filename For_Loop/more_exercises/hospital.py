period_for_calculating = int(input())       # integer between [1...1000]
initial_doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_for_calculating + 1):
    daily_treated_patients = 0
    daily_untreated_patients = 0

    if day % 3 == 0 and untreated_patients > treated_patients:
        initial_doctors += 1

    number_of_patients = int(input())  # integer between [1...10 000]

    if initial_doctors >= number_of_patients:
        daily_treated_patients = number_of_patients
        daily_untreated_patients = 0
    if initial_doctors < number_of_patients:
        daily_untreated_patients = number_of_patients - initial_doctors
        daily_treated_patients = number_of_patients - daily_untreated_patients

    treated_patients += daily_treated_patients
    untreated_patients += daily_untreated_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")