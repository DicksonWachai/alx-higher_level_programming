#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0
    # Initialize the total score and total weight
    total_score = 0
    total_weight = 0
    # Iterate over the tuples in the list
    for score, weight in my_list:
        # Check if the score is an integer
        if isinstance(score, int):
            # Add the score multiplied by the weight to the total score
            total_score += score * weight
            # Add the weight to the total weight
            total_weight += weight
    # Calculate the weighted average
    average = total_score / total_weight
    # Return the weighted average
    return average
