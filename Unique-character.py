def Uniqcharacter(s):
    character_count = {} 
    for character in s:
        character_count[character] = character_count.get(character, 0) + 1
    for i in range(len(s)):
        if character_count[s[i]] == 1:
            return i

    return -1
