def canConstruct(self, ransomNote, magazine):
    magazine_count = {}

    for letter in magazine:
        magazine_count[letter] = magazine_count.get(letter, 0) + 1

    # Check if all letters in ransomNote can be formed from magazine
    for letter in ransomNote:
        if letter not in magazine_count or magazine_count[letter] == 0:
            return False
        magazine_count[letter] -= 1

    return True