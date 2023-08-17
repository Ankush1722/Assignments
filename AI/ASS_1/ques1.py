def get_test_scores(subject):
    """prompts the user to enter test scores for each student in a specific subject.
       Validates the input to ensure the score is between © and 100. Returns a List
       of scores."""
    scores = []
    for i in range(1, 11):
        while True:
            try:
                score = int(input(f"Enter {subject} score for student {i}: "))
                if 0 <= score <= 100:
                    scores. append(score)
                    break
                else:
                    print("Invalid scorel Score should be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid score.")
    return scores

def get_statistics (scores):
    """Calculates the highest, lowest, and average marks from a list of scores.
    Returns the highest, lowest, and average marks as a tuple."""
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average

def display_statistics(subject, highest, lowest, average):
    """Displays the statistics (highest, lowest, and average marks) for a specific subject."""
    print(f"\n{subject} Test:")
    print (f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
    print(f"Average Mark: {average}")

def main():
    """Entry point of the program. Generates test results for multiple subjects and displays
    and statistics."""
    subjects = ["Maths", "Science", "English", "IT"]
    test_scores = {}
    for subject in subjects:
        test_scores[subject] = get_test_scores (subject)
    print("\nTest Results:")
    for subject, scores in test_scores.items():
        highest, lowest, average = get_statistics(scores)
        display_statistics(subject, highest, lowest, average)
    # Overall Results
    overall_scores = [score for subject_scores in test_scores.values() for score in subject_scores]
    overall_highest, overall_lowest, overall_average = get_statistics(overall_scores)

    print("\nOverall Results:")

    print(f"Highest Mark: {overall_highest}")
    print(f"Lowest Mark: {overall_lowest}")
    print(F"Average Mark: {overall_average}")
          
if __name__ == "__main__":
    main()




