import pathlib
import random

from Bio import Phylo
import Bio.Phylo.Consensus
from  Bio.Phylo.Consensus import majority_consensus, strict_consensus, adam_consensus
import Bio
import matplotlib.pyplot as plt

from .tree_tools import phylo_formats

CONSENSUS_MODES = ['STRICT', 'MAJORITY', 'ADAM']

def load_consensus_trees_impl(files,mode,cutoff):
    trees = []
    for file in files:
        trees.append(Phylo.read(file, phylo_formats[pathlib.Path(file).suffix]))
    cons_tree = None
    if mode == 'STRICT':
        cons_tree = strict_consensus(trees)
    elif mode == 'MAJORITY':
        if cutoff != '':
            cons_tree = majority_consensus(trees, float(cutoff))
        else:
            cons_tree = majority_consensus(trees, 0.5)
    elif mode == 'ADAM':
        cons_tree = adam_consensus(trees)
    else:
        raise Exception("Unknown consensus mode")
    Phylo.draw(cons_tree, do_show=False)
    cons_name = "../../data/created/cons_tree" + str(random.randint(0,10000000)) + ".png"
    plt.savefig(cons_name)
    return cons_name
