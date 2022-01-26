# Wordle Helper, because why not.

What am I doing with my life?

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
  --contains TEXT    Comma separated list of letters of indices.  Indicates
                     that these letters must be included NOT at these indices.
                     Example: "o0,l1,k2"
  --indices TEXT     Comma separated list of letters and indices.  Indicates
                     that these letters MUST be included at these indices.
                     Example: "f0,o1,l2,k3,s4"
  --impossible TEXT  Letters that must be excluded.  Example:
                     "abcdeghijmnpqrtuvwxyz"
  --inputfile TEXT   Word list to use. Default: "5letterwords.txt"
  --help             Show this message and exit.
```

## Examples

```sh
; python wordle.py --contains l0,n4 --indices o2 --impossible wertyuiascb
flong
klong
knoll
plonk

; python wordle.py --contains l0,l2,n4 --indices k0,o2 --impossible wertyuiascb
klong
knoll
```
