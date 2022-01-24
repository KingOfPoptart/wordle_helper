# Wordle Helper, because why not.

Given some input, spit out the possible words for a Wordle puzzle

## First time setup

```sh
# Download the dictionary to a file called 'dictionary.txt'
curl https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt -o dictionary.txt -s

# Do some preprocessing and spit out '5letterwords.txt'
python preprocess.py
```

## Usage

```sh
Usage: wordle.py [OPTIONS]

  Wordle Helper.

Options:
  --contains TEXT    Letters that must be included. Example "olk"
  --indices TEXT     Comma separated list of letters and indices.  Example:
                     "f0,o1,l2,k3,s4"
  --impossible TEXT  Letters that must be excluded.  Example:
                     "abcdeghijmnpqrtuvwxyz"
  --inputfile TEXT   Word list to use  (Default: "5letterwords.txt")
  --help             Show this message and exit.
```

## Examples

```sh
; python wordle.py --contains ln --indices o2 --impossible wertyuiascb 
flong
klong
knoll
plonk

; python wordle.py --contains ln --indices k0,o2 --impossible wertyuiascb                        
klong
knoll

```
