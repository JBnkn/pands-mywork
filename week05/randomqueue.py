# randomqueue.py
# author: Joseph Benkanoun
# create a program that puts 10 random numbers into a queue(list)
# the program should then output all the values in the queue
# then take the numbers from the queue one at a time, print it and the current numbers still in the queue
# the command pop(0) takes the first element out of a list

import random

queue = []

while len(queue) != 10:
    number = random.randint(11,99)
    queue.append(number)

print(f"The numbers are {queue}")

while len(queue) != 0:
    if len(queue) != 1:
        print(f"Let's remove the number {queue.pop(0)}. The queue now consists of: {queue}")
    else:
        print(f"Let's remove the number {queue.pop(0)}. There are no numbers remaining in the queue.")
