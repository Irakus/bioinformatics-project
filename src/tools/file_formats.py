import os;
import pathlib;
ext_to_type = {
    ".fasta": "fasta",
    ".fa": "fasta",
    ".aln": "clustal",
    ".dnd": "newick",
    ".gb": "genbank",
    ".gbk": "genbank",
    ".sth": "stockholm",
    ".phy": "phylip",
    ".nex": "nexus",
}

def file_extension(file):
    return ext_to_type[pathlib.Path(file).suffix]

def supports(file):
    return ext_to_type.keys().__contains__(pathlib.Path(file).suffix)

def get_in_aln(file):
    return pathlib.Path(file).with_suffix(".aln")