food = ['pasta', 'pizza', 'burger', 'fries', 'sushi']
print (food)
print (food[1])
print (food[4])
print (food[-1])
food.append("ice cream")
print (food)
food.insert(2,"watermelon")
print (food)
food.remove ("burger")
print (food)
food.pop (4)
print (food)
print ("2D list")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("Number of rows :",len(matrix))
print("Number of columns :",len(matrix[0]))
for i in range(3):
  for j in range(3):
      print(matrix[i][j], end = " " ) 
  print (" \n ")