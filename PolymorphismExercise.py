class Square:
    side = 4
    def __init__(self,length):
        self.length = length

    def __pow__(side1, side2):
        return (side1.length ** side2.length)

squareO = Square(2)
squareT = Square(4)
print(squareO ** squareT)

# class Square:
#     sides = 4
#     def __init__(self, length):
#         self.length = length
#
#     def __pow__(squareOne, squareTwo):
#         return(squareOne.length ** squareTwo.length)
#
# squareOne = Square(2)
# squareTwo = Square(4)
# print(squareOne ** squareTwo)
