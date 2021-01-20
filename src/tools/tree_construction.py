import pathlib
import matplotlib.pyplot as plt
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor, ParsimonyScorer, NNITreeSearcher, \
    ParsimonyTreeConstructor
import random

from .file_converter import read_converter_formats


def load_MSA_for_tree(file):
    try:
        alignments = AlignIO.read(file, format = read_converter_formats[pathlib.Path(file).suffix])
        return  alignments
    except KeyError:
        return "Unsupported format"
def create_tree_distance_impl(msa, algorithm):
    calculator = DistanceCalculator('identity')
    constructor = DistanceTreeConstructor(distance_calculator=calculator,method=algorithm)
    tree = constructor.build_tree(msa)
    Phylo.write(tree, "../../data/created/tree" + str(random.randint(0,10000000)) + ".nex", "nexus")
    Phylo.draw(tree,do_show=False)
    plt.savefig("../../data/created/createdTree"+algorithm+".png")
    return "../../data/created/createdTree"+algorithm+".png"

def create_tree_parsimony_impl(msa):
    calculator = DistanceCalculator('identity')
    constructor = DistanceTreeConstructor(distance_calculator=calculator, method='nj')
    starting_tree = constructor.build_tree(msa)

    scorer = ParsimonyScorer()
    searcher = NNITreeSearcher(scorer)
    constructor = ParsimonyTreeConstructor(searcher=searcher,starting_tree=starting_tree)
    tree = constructor.build_tree(msa)
    Phylo.write(tree, "../../data/created/tree" + str(random.randint(0,10000000)) + ".nex", "nexus")
    Phylo.draw(tree,do_show=False)
    plt.savefig("../../data/created/createdTree_parsimony.png")
    return "../../data/created/createdTree_parsimony.png"