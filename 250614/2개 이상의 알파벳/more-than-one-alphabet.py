A = input()

# Please write your code here.
def morethantwo(word):
    finding_lst = list(set(word))
    return "Yes" if len(finding_lst) > 1 else "No"

print(morethantwo(A))