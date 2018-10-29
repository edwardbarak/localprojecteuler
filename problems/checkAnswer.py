from sys import argv
import os

# Usage:    python checkAnswer.py [problem #] [your answer]

# Example:  python checkAnswer.py 6 2441
#           False

path = '%s/%s' % (os.getcwd(), str(argv[1]))
with open(path + '/' + str(argv[1]) + '/answer.txt', 'r') as f:
    ans = f.read()

print(argv[2] == ans)
