import datetime
current_time = datetime.datetime.now() #Tracking the current time
print("it's now: {:%H:%M:%S}".format(current_time)) #%H to display hours, %M to display mins, %S to display seconds
def get_user_name():
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        try:
            # Requesting the user's name
            user_input = input("What is your name..? \n").strip()  # Remove leading/trailing whitespace
            if user_input.isalpha():  # Ensure the name contains only letters
                return user_input
            else:
                print("C'mon man, enter your name properly, do I have to beg?")
                attempts += 1  # Increment attempts if the input is not valid
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            return None
    
    # If max attempts are reached
    print("This ain't working, I'm leaving.")
    return None

# Calling the function for the username
user_name = get_user_name()
if user_name is not None:
    print(f"Welcome, {user_name}!")
else:
    print("No valid name was provided.")

   
         
         
user_age = int(input("How old are you? \n"))
seconds_lived = user_age*365*24*60*60 
print(f"Hello {user_name}, how have you been? Based on your age, you have lived for {seconds_lived} seconds... \nThe clock is ticking")
print("Oh snap")
print("{:^11}".format("radius = 10") + " \n area = 3.14 * radius ** 2 \n the area of a circ...")
print("\n Lately it has been a blast remmembering python. \n Hasn't it?\n")

# 8 spaces reserved, 3 spaces after decimal
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:010.3f}".format(12.4565))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

# string padding with center alignment
# and '*' padding character
# added example
print("{:*^5}".format("mouse"))
print("{:*^7}".format("mouse"))