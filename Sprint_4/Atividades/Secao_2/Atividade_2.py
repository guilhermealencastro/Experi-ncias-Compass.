def conta_vogais(texto: str) -> int:

    is_vowel = lambda char: char.lower() in 'aeiou'
    count_vowels = len(list(filter(is_vowel, texto)))

    return count_vowels
