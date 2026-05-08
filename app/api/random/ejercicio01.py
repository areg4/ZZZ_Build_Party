"""Description The input will be a list of integers, each separated by a newline character. 
The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow. 
Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100). 
For each test case, calculate the power of four of Yn, excluding when Yn is positive, and print the calculated sum in the output. 
Notes There should be no output until all the input has been received. 
Do not put blank lines between test cases solutions. 
Take input from standard input, and output to standard output. 
There will be no EOF. The final output is guaranteed to be within the int32 range. 
It is possible that X and the number of integers Yn may not be equal. 
If that is the case, print -1 as the output. Specific rules for Python solution Your source code must be a single file, including at least a main function. 
Do not use any for or while loop statements, or any list / set / dictionary comprehension syntax. 
Sample Input: 
2 
4 
3 -1 1 10 
5 
9 -5 -5 -10 10 
Sample output: 
1 
11250
"""


def main():
    N = int(input())
    results = []

    def process_cases(n):
        if n == 0:
            return
        
        X = int(input())
        Y = input().split()

        if len(Y) != X:
            results.append(-1)
        else:
            Y = map(lambda x: int(x), Y)
            negatives = filter(lambda x: x < 0, Y)
            powers = map(lambda x: pow(x, 4), negatives)
            results.append(sum(powers))

        process_cases(n - 1)

    process_cases(N)

    print("\n".join(map(str, results)))

main()