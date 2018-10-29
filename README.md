# Project Euler Local

Clone this repository to do exercises from https://projecteuler.net/ offline.

## FAQ
### How do I check my answer?

use shell command: 	./exercises/checkAnswer.py [exercise #] [your solution]

**Example:**

user@pc:~/projectueler/exercises$ python checkAnswer.py 6 2441

False

### How do I contribute?
Use the current file schema, where each exercise is given its own folder in the *exercises* folder, accompanied with the answer inside a text file. To make it easier, ./exercises/exerciseTemplate.py takes arguments **[exercise #] [answer]** to generate the exercises' README.md & answer.txt. **This requires an internet connection** to pull the exercise from projecteuler.net.

**Example:**

user@pc:~/projecteuler/exercises$ python exerciseTemplate.py 6 25164150

result:

1. if directory **6** in the exercises folder does not exists, it will be created
- **README.md** will be generated from https://projecteuler.net/problem=6 containing the exercise
- **25164150** will be written to answer.txt inside of directory 6

When you are done, you can submit a pull request.
