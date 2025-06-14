A = input()

# Please write your code here.
def palindrome(string):
    s = list(string)
    if s == list(reversed(s)):
        return "Yes"
    else: return "No"


print(palindrome(A))

