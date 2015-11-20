import re


handler = open("sampleDataWk2.txt")
count = []
for line in handler:
    nums = re.findall('[0-9]+', line.strip())
    if len(nums) >= 1:
        for num in nums:
            count.append(int(num))
print sum(count)
