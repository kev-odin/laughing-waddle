"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as 
the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of 
all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Image of Flood Fill Example #1
Examples:

Input: 
image = [[1,1,1],
        [1,1,0],
        [1,0,1]
        ],
        
        sr = 1, sc = 1, newColor = 2

Output: [[2,2,2],
         [2,2,0],
         [2,0,1]
        ]

Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the 
same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Input: image = [[0,0,0],
                [0,0,0]
                ], 
                sr = 0, sc = 0, newColor = 2

Output: [[2,2,2],
         [2,2,2]
        ]

U:
    bao:    Can we modify the input array or should we need to create another array?
            What about a different color? - Keep the same.
    far:    Are we limited to the 4 directions of traversal?
            What if a color is the same color as being landed on?
    jes: 
    kev: Driving.
    tin: What if there is an empty node? - > Is there an "X" to designate a hole in the 2D array?
    xin: What happens if the input is empty?
M:
    DFS
    Helper Function - If the position is valid? -> Run DFS
P:
    * Track the starting color that we land on
    * Loop thru each cell that is 4-D adjacent
    * Run DFS on each cell if it is not in the visited set
        * Compare to check if the color is the same as the starting color
            * If it is the same, then change > recursive call on neighbor cell
            * Else if the boundary is OOB, return
I:
R:
E:

"""


def solution(image, sr=1, sc=1, new_color=2):

    visited = set()

    rows = len(image)
    cols = len(image[0])

    def dfs(row, col):
        visited.add((row, col))
        starting_color = image[row][col]

        image[row][col] = new_color

        possible_dir = [(row, col + 1), (row + 1, col), (row - 1, col), (row, col - 1)]

        for next_row, next_col in possible_dir:
            if (
                next_row in range(rows)
                and next_col in range(cols)
                and (next_row, next_col) not in visited
            ):
                if image[next_row][next_col] != starting_color:
                    continue

                dfs(next_row, next_col)

    dfs(sr, sc)
    print(visited)
    return image


if __name__ == "__main__":
    # test1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    test1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(test1))
