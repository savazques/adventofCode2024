
def main():
    leftColumn = []
    rightColumn = []
    with open('input.txt', 'r') as file: 
        for line in file:
            left, right = line.split("   ")
            leftColumn.append(left)
            rightColumn.append(right.strip())
        
    leftColumn.sort()
    rightColumn.sort()

    totalSum = 0

    for i in range(len(leftColumn)):
        difference = abs(int(leftColumn[i]) - int(rightColumn[i]))
        totalSum += difference
    
    print(totalSum)


if __name__ == "__main__": 
    main()