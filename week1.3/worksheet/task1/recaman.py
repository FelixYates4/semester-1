# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

a = 0
k = 1
sequence = [0]
for i in range(L - 1):
    a1 = a - k
    a2 = a + k
    if a1 < 0 or a1 in sequence:
        sequence.append(a2)
        a = a2
    else:
        sequence.append(a1)
        a = a1
    k += 1

# You may wish to use further output for testing purposes while you develop your code
[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence