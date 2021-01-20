from tkinter import filedialog
from tkinter import *
from Bio import SeqIO

from .tools import file_extension


def load_sequence_from_file(file):
    records = list(SeqIO.parse(file, file_extension(file)))
    output = ""
    for record in records:
        output = output + str(record.id) + "\n" + str(record.seq) + "\n"
    return output
