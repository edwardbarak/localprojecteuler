import numpy as np

with open('numbers.txt', 'r') as f:
    text = f.read()
    f.close()

nums = text.split('\n')
nums = [int(num) for num in nums]
nums = np.array(nums)
print(str(nums.sum())[:10])