import os
import pathlib

from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline

from .file_formats import file_extension
from .programs_names import path_to_programs


def example():

    file1 = "../data/myfasta.fasta";
    clustalw_cline = ClustalwCommandline(path_to_programs+"clustalw2.exe", infile=file1)

    clustalstdout, stderr = clustalw_cline()
    print(clustalstdout)
    file2 = "../data/myfasta.aln"
    align2 = AlignIO.read(file2, file_extension(file2))
    print(align2)

def clustal_calculate_alignment(file,args):
    clustalw_cline = ClustalwCommandline(path_to_programs + "clustalw2.exe", infile=file)
    clustalstdout, stderr = clustalw_cline()
    result = pathlib.Path(file).with_suffix(".aln")
    align2 = AlignIO.read(result, file_extension(result))
    return align2


