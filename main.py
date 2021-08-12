# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from music21 import *
import operator

def main():
    s = corpus.parse('bach/bwv65.2.xml')
    pass

def get_highest_weight_note(measure):
    seen_notes = {}
    for note in measure.notes:
        # if the note has not been seen yet, put it into
        # the dictionary
        if note.pitch not in seen_notes:
            seen_notes[note.pitch] = note.duration.quarterLength
            continue

        seen_notes[note.pitch] += note.duration.quarterLength

    # get the highest weighted one
    print(max(seen_notes, key = seen_notes.get))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create an object of melodies that contains their paths
    # so only mxl files work
    melodies = {
        "sample": "tinynotation: 3/4 rest c4 d8 f g16 a g f c4 c8 e f g",
        "amazing_grace": ""
    }


    amazing_grace_score = converter.parse("sample_melodies/amazing_grace.mxl")

    # get each measure and for each measure, get eht higher weighed notes
    # each of the mxl files contain a textbox metadata and a part

    # there should be only one part (the piano part)
    for measure in amazing_grace_score.parts[0].getElementsByClass('Measure'):
        # if it is the first measure
        if measure.offset == 0.0:
            # get rid of useless info
            measure = measure[3:]

        get_highest_weight_note(measure)
