def findRepeatedDnaSequences(s):
    seen = set()  # To track substrings that we've seen
    result = set()  # To store repeated sequences
    for i in range(len(s) - 9):  # Iterate through the string with window size 10
        substring = s[i:i + 10]  # Extract a 10-character-long substring
        if substring in seen:
            result.add(substring)  # If seen before, add to result
        else:
            seen.add(substring)  # Otherwise, add to seen set
    
    return list(result)  # Convert result set to a list and return
