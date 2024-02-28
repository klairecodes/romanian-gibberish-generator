[Româneşte](#generatorul-de-bolboroseală-românesc)

# Romanian Gibberish Generator
This is a silly script to generate Romanian words using the romanian alphabet and common digraphs and trigraphs. It can be easily modified for other languages.

## Example
```
> python rom_generator.py -n 5 -s 3
iașâșâ
ieșînâ
stituueirâ
kâdâțu
țățătă
```

## Usage
For usage information, run:
```
python3 rom_generator.py -h
```
Here is the current help text:
```
usage: rom_generator [-h] [-n COUNT] [-s NUM_SYLLABLES] [-d]

Generates Romanian gibberish words.

options:
  -h, --help        show this help message and exit
  -n COUNT          The number of words to generate.
  -s NUM_SYLLABLES  The maximum number of syllables each word should contain.
  -d                If set, adds a delay between each entry.

Written by Klaire Curde.
```
The default number of words generated is 20, and the default maximum syllables is 3.

___

# Generatorul de Bolboroseală Românesc
Acesta este un script amuzant pentru a genera cuvinte românești folosind alfabetul român și digrafele și trigrafele comune. Poate fi ușor modificat pentru alte limbi.

## Exemplu
```
> python rom_generator.py -n 5 -s 3
iașâșâ
ieșînâ
stituueirâ
kâdâțu
țățătă
```

## Utilizare
Pentru informații despre utilizare, rulați:
```
python3 rom_generator.py -h
```
Iată textul de ajutor curent:
```
usage: rom_generator [-h] [-n COUNT] [-s NUM_SYLLABLES] [-d]

Generates Romanian gibberish words.

options:
  -h, --help        show this help message and exit
  -n COUNT          The number of words to generate.
  -s NUM_SYLLABLES  The maximum number of syllables each word should contain.
  -d                If set, adds a delay between each entry.

Written by Klaire Curde.
```
Numărul implicit de cuvinte generate este 20, iar numărul implicit maxim de silabe este 3.
