#!/usr/bin/env python3

"""Word frequency graph generator.

This script prints out a graph of frequecy of word occurency in the provided file.
Need two arguments:

 - the issued word
 - the filename
"""

import sys
import operator
import argparse
# pylint: disable=import-error
import matplotlib.pyplot as plt


def word_freq(word, filename):
    doc = {}

    # populate doc with new word
    for line in open(filename):
        split = line.split(' ')
        for entry in split:
            if (doc.__contains__(entry)):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    # exit if word is not populated
    if (not word in doc):
        sys.stderr.write("Error: " + word + " does not appear in " + filename)
        sys.exit(1)

    # sorting out dictionary data from highest to least in occurrence for appropriately visualized on the graph
    sorted_doc = (sorted(doc.items(), key=operator.itemgetter(1)))[::-1]

    # populate data for graph
    just_the_occur = []
    just_the_rank = []
    word_rank = 0
    word_frequency = 0
    entry_num = 1

    for entry in sorted_doc:
        if (entry[0] == word):
            word_rank = entry_num
            word_frequency = entry[1]

        just_the_rank.append(entry_num)
        entry_num += 1
        just_the_occur.append(entry[1])

    # graph
    plt.title("Word Frequencies in " + filename)
    plt.ylabel("Total Number of Occurrences")
    plt.xlabel("Rank of word(\"" + word + "\" is rank " + str(word_rank) + ")")
    plt.loglog(just_the_rank, just_the_occur, basex=10)
    plt.scatter(
        [word_rank],
        [word_frequency],
        color="orange",
        marker="*",
        s=100,
        label=word
    )
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="the word to be searched for in the text file."
    )
    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through"
    )

    args = parser.parse_args()

    try:
        open(args.filename)  # check file existence
        word_freq(args.word, args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)


if __name__ == "__main__":
    main()
