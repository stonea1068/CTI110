# Ashley Stone
# 07/05/2026
# P4HW1
# This program collects grades, removes the lowest grade,
# calculates the average, and displays the letter grade.

# Pseudocode:
# Ask user how many scores they want to enter
# Create an empty list for scores
# Use a loop to collect each score
# Check if score is between 0 and 100
# If invalid, ask user to enter score again
# Add valid scores to list
# Find the lowest score
# Remove lowest score from list
# Calculate average of remaining scores
# Determine letter grade
# Display results


# Create empty list
scores = []

# Ask user how many scores
num_scores = int(input("How many scores do you want to enter? "))

# Loop to collect scores
for count in range(1, num_scores + 1):

    score = float(input(f"Enter score #{count}: "))

    # Validate score
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input(f"Enter score #{count} again: "))

    scores.append(score)


# Find lowest score
lowest_score = min(scores)

# Create modified list
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

# Calculate average
average = sum(modified_scores) / len(modified_scores)


# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"


# Display results
print()
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")