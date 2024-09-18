# Find the first nonrepeating character in a test string
teststring = 'little green apples grow on great big trees'
chars = list(teststring)
for i in range(len(chars)):
    if chars.count(chars[i]) == 1:
        print(f"First unique character in the test string is {chars[i]}")
        break
    elif i == len(chars) -1:
        print(f"There are no unique characters in the string")



