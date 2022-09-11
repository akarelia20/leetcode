def rotate(matrix):
    l,r = 0, len(matrix) -1
    top,bottom = l, r 

    while r > l:
        for i in range(r-l):

            #save top left
            top_left= matrix[top][l +i]

            # move bottom left to top left
            matrix [top][l+i] = matrix [bottom-i][l]

            #move bottom right to bottom left
            matrix [bottom-i][l] = matrix[bottom][r-i]

            # move top right to bottom right
            matrix[bottom][r-i]= matrix[top+i][r]

            # move top left to top right
            matrix[top+i][r] = top_left

        r -= 1
        l += 1
    print(matrix)


print(rotate([[1,2,3], [4,5,6], [7,8,9]]))