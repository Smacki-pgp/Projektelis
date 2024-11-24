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