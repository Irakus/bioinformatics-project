from Bio import AlignIO
import pathlib

read_converter_formats = {  # "fasta" is done via Bio.SeqIO
    ".aln": "clustal",
    ".emboss": "emboss",
    ".maf": "maf",
    ".mln": "mauve",
    ".msf": "msf",
    ".phy": "phylip",
    ".sth": "stockholm",
    ".fasta": "fasta",
    ".fa": "fasta",
    ".xml": "nexml",
    ".nex": "nexus",
}

write_converter_formats = {  # "fasta" is done via Bio.SeqIO
    ".aln": "clustal",
    ".emboss": "emboss",
    ".maf": "maf",
    ".mln": "mauve",
    ".phy": "phylip",
    ".sth": "stockholm",
    ".fasta": "fasta",
    ".fa": "fasta",
    ".xml": "nexml",
    ".nex": "nexus",
}

def load_sequences_file(file):
    out_string = ""
    try:
        alignments = AlignIO.read(file, format = read_converter_formats[pathlib.Path(file).suffix])
        for alignment in alignments:
            out_string += str(alignment) + "\n"
        return out_string
    except KeyError:
        return "Unsupported format"

def convert_file_impl(input,output):
    try:
        AlignIO.convert(in_file=input,
                        in_format = read_converter_formats[pathlib.Path(input).suffix],
                        out_file=output,
                        out_format = write_converter_formats[pathlib.Path(output).suffix])
        return open(output).readlines()
    except KeyError:
        return "Unsupported format"
