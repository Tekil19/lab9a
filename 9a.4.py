def checker(s):
    return s == s[::-1]

lst = ['madam', 'Python', 'malayalam', 12321]

palindromes = [str(x) for x in lst if checker(str(x))]

print("Palindromes:", palindromes)
