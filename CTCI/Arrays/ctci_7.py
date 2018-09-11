"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_string(matrix, N):
    for layer in range(N//2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i-1][layer]

            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            matrix[-layer-1][-i-1] = top
    return matrix

print(rotate_string([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4))

