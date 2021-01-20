import pathlib
import subprocess
import sys
from io import StringIO
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO

from .programs_names import path_to_programs

def example():
    muscle_cline = MuscleCommandline(path_to_programs+"muscle",input="../data/myfasta.fasta")
    stdout, stderr = muscle_cline()
    child = subprocess.Popen(str(muscle_cline), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=(sys.platform!="win32"))
    align = AlignIO.read(child.stdout, "fasta")
    print(align)

def muscle_calculate_alignment(file,args):
    muscle_cline = MuscleCommandline(path_to_programs + "muscle", input=file)
    child = subprocess.Popen(str(muscle_cline), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=(sys.platform!="win32"))
    align = AlignIO.read(child.stdout, "fasta")
    return align