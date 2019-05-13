from collections import Counter


numbers = [257]
with open("/nums.txt","r") as f:
    for everyline in f:
        num = line.strip()      # remove any extra spaces trailing or before
        if cleanedLine:                 # is not empty
            numbers.append(num)


b = Counter(numbers)

print( b.most_common(3))  # 3 most common numbers in array
