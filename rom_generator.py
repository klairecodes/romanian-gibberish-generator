import random
import time
import argparse

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
    parser = argparse.ArgumentParser(
                    prog='rom_generator',
                    description='Generates Romanian gibberish words.',
                    epilog='Written by Klaire Curde.')

    parser.add_argument('-n', type=int, dest='count', action='store', default=20, help='The number of words to generate.')
    parser.add_argument('-s', type=int, dest='num_syllables', action='store', default=3, help='The maximum number of syllables each word should contain.')
    parser.add_argument('-d', action='store_true', default=False, help='If set, adds a delay between each entry.')
    args = parser.parse_args()

    for _ in range(args.count):
        num_syllables = args.num_syllables
        print(generate_gibberish(num_syllables))
        if args.d:
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

