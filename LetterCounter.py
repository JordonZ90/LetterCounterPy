user_msg = input("Please enter your message ").lower()
user_letter = input("Please enter your letter ").lower()

# Count occurrences
count = user_msg.count(user_letter)

# Calculate percentage
len_message = len(user_msg)
percentage = count/len_message * 100

# Print output to user
print(f"The letter '{user_letter}' occurs {user_msg.count(user_letter)}")
print(percentage)

