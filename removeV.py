def removeVowels(s):
    vowels = "AEIOUaeiou"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result