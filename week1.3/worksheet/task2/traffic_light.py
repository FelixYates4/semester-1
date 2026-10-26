"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Felix Yates
"""

# Keep the original durations so we can reset them later
durations = { "red": 4, "red_amber": 3, "green": 5, "amber": 3 }
states = durations.copy()

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime < maxtime:
    systime += 1
    states[state] -= 1

    if states[state] == 0:
        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"
        
        # Reset the countdown for the new state back to its original duration
        states[state] = durations[state]

    print(f"Time {systime:03} State {state}")
# At the end of each step you should output the time and state using the statement on line 14