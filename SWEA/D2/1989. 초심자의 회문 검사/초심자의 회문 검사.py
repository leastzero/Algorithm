t = int(input())
for i in range(1, t+1):
    palindrome = str(input())
    r_palindrome = palindrome[::-1]
    answer = 0
    if palindrome == r_palindrome:
        answer = 1
    else:
        answer = 0
    print("#%d %d" % (i, answer))