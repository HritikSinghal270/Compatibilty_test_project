def calculate_flames_percentage(name1, name2):
    """
    Calculate the FLAMES compatibility percentage between two names.

    Args:
        name1 (str): First name
        name2 (str): Second name

    Returns:
        str: Compatibility percentage and relationship type
    """

    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    # print('hello check 2')
    # Remove common letters
    unique_letters = list(name1) + list(name2)
    for char in name1:
        if char in name2:
            unique_letters.remove(char)
            # unique_letters.remove(char)

    # Count remaining unique letters
    remaining_count = len(unique_letters)

    # FLAMES relationship types
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    # Determine relationship type based on count
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:-1]

    # Calculate percentage based on remaining letters
    compatibility_score = (100 - remaining_count * 5) if remaining_count < 20 else 5
    compatibility_score = max(compatibility_score, 0)

    return f"{flames[0]} ({compatibility_score}%)"


# Compatibility logic
def calculate_compatibility(user1, user2):
    # Dummy compatibility logic
    if not isinstance(user1, dict) or not isinstance(user2, dict):
        return "Error: Both inputs must be dictionaries."
    
    # Collect all unique keys from both users
    all_keys = set(user1.keys()).union(set(user2.keys())) - {"name","id","is_admin"} 
    matching_attributes = 0
    print(user1)
    print(user2)
    print(all_keys)
    for key in all_keys:
        # Check if both users have the key and the values match
        if key in user1 and key in user2 and user1[key] == user2[key]:
            matching_attributes += 1
    print(matching_attributes)
    # Calculate percentage score
    score = (matching_attributes / len(all_keys)) * 100 if all_keys else 0
    return f"Compatibility Score: {score:.2f}%"
    # return f"Compatibility Score: {score}%"


# Example usage
# name1 = "aa"
# name2 = "aa"
# result = calculate_flames_percentage(name1, name2)
# print(f"Compatibility between {name1} and {name2}: {result}")
# print('hello')
