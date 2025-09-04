"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output: list[list[str]] = []
        row: list[str] = []

        form_diagonal = False
        diagonal_position = numRows - 2

        for l in s:

            if not form_diagonal or diagonal_position < 1 or numRows <= 2:
                print(f"appending {l}")
                row.append(l)

                if len(row) == numRows:
                    output.append(row)
                    row = []
                    form_diagonal = True
            else:
                for i in range(0, numRows):
                    if i == diagonal_position:
                        row.append(l)
                    else:
                        row.append(" ")

                output.append(row)
                row = []
                diagonal_position -= 1

                if diagonal_position == 0:
                    form_diagonal = False
                    diagonal_position = numRows - 2

        if row:
            while len(row) < numRows:
                row.append(" ")
            output.append(row)

        output = list(map(list, zip(*output)))

        output_string = ""
        for row in output:
            for l in row:
                if l == " ":
                    continue
                else:
                    output_string += l

        return output_string


mySolution = Solution()
s = "A"
numRows = 1

print(mySolution.convert(s, 1))
