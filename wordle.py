import click, re

@click.command()
@click.option('--contains', default="", help='Letters that must be included. Example: "olk"')
@click.option('--indices', default="", help='Comma separated list of letters and indices.  Example: "f0,o1,l2,k3,s4"')
@click.option('--impossible', default="", help='Letters that must be excluded.  Example: "abcdeghijmnpqrtuvwxyz"')
@click.option('--inputfile', default="5letterwords.txt", help='Word list to use. Default: "5letterwords.txt"')
def solve(contains, indices, impossible, inputfile):
    """Wordle Helper."""
    
    with open(inputfile) as file:
        fiveletterwords = file.readlines()
    indices = indices.split(",")

    for word in fiveletterwords:
        word = word.strip()
        correct = True
        if len(indices) > 0:
            for letter in indices:
                if letter and word[int(letter[1])] != letter[0]:
                    correct = False
                    break
        if correct and len(contains) > 0:
            for letter in contains:
                if letter not in word:
                    correct = False
                    break
        if correct and len(impossible) > 0:
            for letter in impossible:
                if letter in word:
                    correct = False
                    break
        if correct:
            print(word)

if __name__ == '__main__':
    solve()
