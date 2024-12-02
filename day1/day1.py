from collections import Counter
def main():
    leftColumn = []
    rightColumn = []
    with open('input.txt', 'r') as file: 
        for line in file:
            left, right = line.split("   ")
            leftColumn.append(left)
            rightColumn.append(right.strip())
        
    """
    Part 1
    leftColumn.sort()
    rightColumn.sort()

    totalSum = 0

    for i in range(len(leftColumn)):
        difference = abs(int(leftColumn[i]) - int(rightColumn[i]))
        totalSum += difference
    
    print(totalSum)"""

    rightFrequencyCount = Counter(rightColumn)

    similarityScore = 0

    for num in leftColumn:
        if num in rightFrequencyCount:
            similarityScore += int(num) * (rightFrequencyCount[num])

    print(similarityScore)

if __name__ == "__main__": 
    main()