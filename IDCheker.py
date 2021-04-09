# Getting unknown digits
i = 0
x1 = [None] * 12
unknown_digits = input("Enter unknown digits: ")

# Getting 13rd digits
last_digit = input("Enter 13rd digit: ")
last_digit = int(last_digit)

# Getting Known digits
while i < 12:
    x1[i] = input("Enter digits: ")
    i += 1

# Getting Unknown positions
i = 0
unknown_list = []

while i < int(unknown_digits):
    unknown_list.append(input("Enter the unknown position: "))
    i += 1
# print("Unknown digits list :", unknown_list)                          # Debug



# Brute forcing
unknown_list = list(reversed(unknown_list))
# print("Reversed unknown digits list :", unknown_list)                 # Debug
limiter = pow(10, len(unknown_list))
# print(limiter)    # Debug
counter = 0
counter2 = 0
counter_list = []
while counter < limiter:
    # Start counting
    counter_list.clear()
    # print("This counter list must be empty : ", counter_list)           # Debug
    digits = [int(x) for x in str(counter)]
    counter_list.extend(digits)
    # print("Original counter list :", counter_list)                    # Debug
    rev_counter_list = counter_list[::-1]
    # print("Reversed counter list :", rev_counter_list)                # Debug
    # for l in rev_counter_list:
    for index, digit in enumerate(rev_counter_list):
        # print("Index : ", index,"Digit :", digit)                     # Debug
        x = unknown_list[index]
        # print("Unkonwn digit's index :", x)                           # Debug
        x1[int(x) - 1] = int(digit)
    # print("Prepared ID's list :", x1)                                # Debug

    ## Find the 13rd digit.
    ## Multipy all digits by sigma 13-i
    y = 13
    x2 = [None] * 12
    i = 0
    while i < 12:
        x2[i] = int(x1[i]) * y
        i += 1
        y -= 1

    # print(x2)                                                     # Debug

    ## Sum a list of numbers
    z = 0
    for l in x2:
        z += int(l)

    # print("Sum of x2 :", z)                                                      # Debug

    ## Mod The sum by 11
    c = z % 11
    # print("Moded by 11 :", c )
    ## Check for a condition and add to the list..
    d = 0
    if c <= 1:
        # print("c <=1", 1 - c)                                                  # Debug
        d = 1 - c
    if c > 1:
        # print("c > 1", 11 - c)                                              # Debug
        d = 11 - c
         x1.append(d)
    # print("13rd digit is :", d)                                   # Debug

    # print("".join(map(str, x1)))                                  # Debug
    ## print a final ID if a 13rd digit = 3.
    if int(x1[12]) == last_digit:
        counter2 += 1
        print("".join(map(str, x1)))
    # print(x1)                                                     # Debug
    ## Remove last digit from the list
    x1.pop()
    counter += 1
print("All occurrences :", counter2)
