import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().strip()
A, C, G, T = map(int, input().split())

current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(P):
    current[DNA[i]] += 1

cnt = 0
if current['A'] >= A and current['C'] >= C and current['G'] >= G and current['T'] >= T:
    cnt += 1

for i in range(P, S):
    current[DNA[i - P]] -= 1  
    current[DNA[i]] += 1      
    if current['A'] >= A and current['C'] >= C and current['G'] >= G and current['T'] >= T:
        cnt += 1
        
print(cnt)
        
