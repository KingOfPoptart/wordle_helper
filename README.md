# Wordle Helper, because why not.

Given some input, spit out the possible words for a Wordle puzzle

## First time setup

```sh
curl https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt -o dictionary.txt -s
python preprocess.py
```

## Usage

```sh
Usage: wordle.py [OPTIONS]

  Wordle Helper.

Options:
  --contains TEXT    Letters that must be included. Example "olk"
  --indices TEXT     Comma separated list of letters and indices.  Example
                     "f0,o1,l2,k3,s4
  --impossible TEXT  Letters that must be excluded.  Example
                     "abcdeghijmnpqrtuvwxyz"
  --inputfile TEXT   Word list to use
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
