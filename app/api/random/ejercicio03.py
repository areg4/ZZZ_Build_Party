from datetime import datetime
import math

def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)

def merge_the_tools(string, k):
    chunks = [string[i:i+k] for i in range(0, len(string), k)]
    
    for c in chunks:
        print("".join(list(dict.fromkeys(c))))

def time_delta(t1, t2):
    dt_t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt_t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
        
    return str(abs(int((dt_t1 - dt_t2).total_seconds())))

