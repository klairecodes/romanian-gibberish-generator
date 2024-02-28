import random
import time

vowels = 'aeiou'
accented_vowels = 'ăâî'
consonants = 'bcdfghjklmnpqrstvwxyz'
accented_consonants = 'șț'
digraphs = ['ch', 'gh', 'oa', 'oe', 'ua', 'ue', 'ea', 'ei', 'ia', 'ie', 'io', 'iu', 'ui']
trigraphs = ['che', 'ghi', 'oai', 'oei', 'uai', 'uei', 'sti', 'str', 'ndr', 'ndi', 'mpl', 'nță']


def generate_initial_syllable():
    if random.random() > 0.5:  # Choose digraph or trigraph with equal probability
        initial_syllable = random.choice(digraphs + trigraphs)
    else:
        if random.random() > 0.2:  # Choose accented or non-accented vowel with higher probability
            vowel = random.choice(accented_vowels)
        else:
            vowel = random.choice(vowels)
        
        if random.random() > 0.5:  # Choose accented or non-accented consonant with equal probability
            consonant = random.choice(accented_consonants)
        else:
            consonant = random.choice(consonants)
        
        initial_syllable = consonant + vowel
    
    return initial_syllable


def generate_syllable():
    if random.random() > 0.2:  # Choose accented or non-accented vowel with higher probability
        vowel = random.choice(accented_vowels)
    else:
        vowel = random.choice(vowels)
    
    if random.random() > 0.5:  # Choose accented or non-accented consonant with equal probability
        consonant = random.choice(accented_consonants)
    else:
        consonant = random.choice(consonants)
    
    syllable = consonant + vowel
    
    # Add digraph or trigraph with lower probability
    if random.random() > 0.8:
        if len(syllable) < 3:  # Check syllable length before adding trigraph
            syllable += random.choice(trigraphs)
        elif len(syllable) < 2:  # Check syllable length before adding digraph
            syllable += random.choice(digraphs)

    return syllable


def generate_gibberish(num_syllables):
    # Specifically add the possibility of words that are only 2 trigraphs
    if num_syllables == 2 and random.random() > 0.8:
        return random.choice(trigraphs) + random.choice(trigraphs)

    gibberish = generate_initial_syllable()
    for _ in range(num_syllables - 1):
        gibberish += generate_syllable()

    return gibberish


def main():
    # for _ in range(20):
        # num_syllables = random.randint(1,4)
        # print(generate_gibberish(num_syllables))
    for _ in range(1000):
        # num_syllables = random.randint(1,3)
        num_syllables = 2
        print(generate_gibberish(num_syllables))
        # time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

