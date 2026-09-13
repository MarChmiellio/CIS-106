# Problem 4: Job Payment
#This program asks for the total amount earned form a job.
# The money is split evenly between three people.

total_amount = float(input("Enter the total amount recieved for the job: $"))

amount_per_person = total_amount / 3

print(f"Each person will recieve: ${amount_per_person:.2f}")
