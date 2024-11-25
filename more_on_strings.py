import datetime
current_time = datetime.datetime.now()
print("it's now: {:%H:%M:%S}".format(current_time))
user_name = input("What is your name..? ")
user_age = input("How old are you? ")
seconds_lived = user_age*365*24*60*60
print(f"Hello {user_name}, how have you been? Based on your age input, you have lived for {seconds_lived} seconds... The clock is ticking")


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