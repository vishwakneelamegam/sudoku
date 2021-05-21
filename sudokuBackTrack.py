#example data set
dataSet = [[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0],[1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]

#check the number if it is suitable
def checkValue(givenData,num,i,j):
    if num in givenData[i]:
       return False
    for count in  range(9):
        if givenData[count][j] == num:
           return False
    rowSize = i - i % 3
    colSize = j - j % 3
    for x in range(3):
        for y in range(3):
            if(givenData[x + rowSize][y + colSize] == num):
               return False
    return True

#solves the given problem using recursive backtracking
def solve(givenData,row,col):
    try:
       dataSize = len(givenData)
       if row == dataSize - 1 and col == dataSize:
          return True
       if col == dataSize:
          row += 1
          col = 0
       if givenData[row][col] > 0:
          return solve(givenData,row,col + 1)
       for num in range(1,dataSize + 1):
          if checkValue(givenData,num,row,col):
             givenData[row][col] = num
             #recursion occurs here
             if solve(givenData,row,col):
                return True
          givenData[row][col] = 0
       return False
    except Exception as e:
       print(e)
       return False

#results
print(solve(dataSet,0,0))
print(dataSet)
