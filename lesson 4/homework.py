food = ['food', 'sleep', 'coffee', 'candy', 'ipad']
print (food)
print (food[-2])
print (food[4])
food.append("pepper")
print (food)
food.insert (3,"cheese")
print (food)
food.remove ("coffee")
print (food)
print ("2D list")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("Number of rows :",len(matrix))
print("Number of columns :",len(matrix[0]))
for i in range(3):
  for j in range(3):
      print(matrix[i][j], end = " " ) 
  print (" \n ")
