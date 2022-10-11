- Add a new program which don't exist earlier
- It should be in .py extenstion
- Please run the program and check if there are no errors before making the PR
- Review other PR's as well
- No Spamming allowed, make sure to include all programs in one PR.


def sum(n):
 s=0
 for i in range (1,n+1):
    s=s+i
 return s
a=int(input("Enter the number till which sum of natural no. is to be counted :"))
print(sum(a))