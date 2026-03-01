def calculate_scores(criteria_data, decision_data):
    scores = {}
    total_weight = 0
    # Compute total weight (ignore zero-weight automatically)
    for crit in criteria_data:
        total_weight += criteria_data[crit]["weight"]
    # Edge case: if total weight is 0
    if total_weight == 0:
        print("All criteria have zero weight. Cannot compute decision.")
        return None
    for option in decision_data:
        weighted_sum = 0

        for crit in criteria_data:
            weight = criteria_data[crit]["weight"]
            max_value = criteria_data[crit]["max_value"]
            rating = decision_data[option][crit]

            normalized = rating / max_value
            weighted_sum += weight * normalized

        final_score = (weighted_sum / total_weight) * 100
        scores[option] = round(final_score, 2)

    return scores

#explanation function to explain why the best option was selected
def explain_choice(best_option, scores, criteria_data, decision_data):
    print("\n=== Explanation ===")

    # Find highest score
    max_score = max(scores.values())

    # Check for tie
    winners = [opt for opt in scores if scores[opt] == max_score]

    if len(winners) > 1:
        print("Tie detected between:", ", ".join(winners))
        print("They achieved equal weighted scores.")
        return

    best_option = winners[0]

    print(f"{best_option} was selected with highest score of {scores[best_option]}%.")

    # Most important criterion
    most_important = max(criteria_data, key=lambda x: criteria_data[x]["weight"])
    weight_value = criteria_data[most_important]["weight"]

    print(f"Most important criterion: {most_important} (weight {weight_value})")

    rating = decision_data[best_option][most_important]
    max_value = criteria_data[most_important]["max_value"]

    performance = (rating / max_value) * 100

    print(f"{best_option} scored {round(performance,2)}% in this key criterion.")
    print("This strong performance in high-weight area increased its final score.")



print("DECISION COMPANION SYSTEM")

print("This system helps you make decisions by evaluating options based on criteria.")
print("You'll be asked to enter the options, criteria, and scores for each option on each criterion.")  
print("The system will then calculate a score for each option and show you the results.\n") 
print("Let's get started!\n")   


print("What is decision are you trying to make?")
decision=input()


print("Step1: What are the options you are considering?")
print("For example, if you are trying to decide which car to buy, your options might be 'Car A', 'Car B', and 'Car C'.")

#list for taking options as input from user
options = []
print("\nEnter options (type 'done' to finish):")
while True:
    option = input("Option: ")
    if option.lower() == "done":
        if len(options) == 0:
            print("You must enter at least one option!")
            continue
        else:
            break
    options.append(option)

print("\nStep2: What are the criteria you will use to evaluate the options?")
print("For example, if you are deciding which car to buy, your criteria might be 'price', 'fuel efficiency', and 'safety rating'.")

criteria_data = {}
print("\nEnter criteria (type 'done' to finish):")
while True:
    crit = input("Criterion name: ")
    if crit.lower() == "done":
        if len(criteria_data) == 0:
            print("You must enter at least one criterion!")
            continue
        else:
            break
    # Weight validation (0-10)
    while True:
        weight = float(input(f"Enter importance weight for {crit} (0-10): "))
        if 0 <= weight <= 10:
            break
        else:
            print("Weight must be between 0 and 10!")
    # Ask maximum possible value
    max_value = float(input(f"Enter maximum possible value for {crit}: "))
    criteria_data[crit] = {
        "weight": weight,
        "max_value": max_value
    }

print("\nStep3: Now enter the value for each option on each criterion.")

print("For example, if you are evaluating cars, you might enter the price for each car on a scale of 1-10.")

decision_data = {}

for option in options:
    print(f"\n Option: {option}")
    decision_data[option] = {}

    for crit in criteria_data:
        max_value = criteria_data[crit]["max_value"]

        # Rating validation (must not exceed max_value)
        while True:
            rating = float(input(f"Rate {crit} (0-{max_value}): "))
            if 0 <= rating <= max_value:
                break
            else:
                print("Invalid rating! Must be within allowed range.")

        decision_data[option][crit] = rating


#calling the function to calculate scores for each option
scores = calculate_scores(criteria_data, decision_data)

print("\n=== Final Results ===")
for option in scores:
    print(option, "-->", scores[option], "%")

best_option = max(scores, key=scores.get)

print("\nRecommended Option:", best_option)

#calling the function to explain why the best option was selected
explain_choice(best_option, scores, criteria_data, decision_data)