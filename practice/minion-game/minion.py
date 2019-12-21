def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            #print(f"vowel = {s[i]} | len(s)-i = {len(s)} - {i} = {len(s) - i}")
            kevsc += (len(s)-i)
        else:
            #print(f"consonant = {s[i]} | len(s)-i = {len(s)} - {i} = {len(s) - i}")
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc) 
    elif kevsc < stusc:
        print("Stuart", stusc)

s = input()
minion_game(s)