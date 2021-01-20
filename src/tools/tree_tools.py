from Bio import Phylo
import matplotlib.pyplot as plt
import pathlib
from matplotlib.pyplot import figure
import pathlib
import Bio.Phylo.Consensus as cons

phylo_formats = {  # "fasta" is done via Bio.SeqIO
    ".xml": "nexml",
    ".nw": "newick",
    ".dnd": "newick",
    ".nex": "nexus",
    ".msf": "msf",
    ".phy": "phylip",
    ".sth": "stockholm",
    ".fasta": "fasta",
    ".fa": "fasta",
}

figure(num=None, figsize=(5, 5), dpi=50, facecolor='w', edgecolor='k')

def load_tree_impl(file):
    try:
        tree = Phylo.read(file, phylo_formats[pathlib.Path(file).suffix])
    except ValueError:
        tree = next(Phylo.parse(file, phylo_formats[pathlib.Path(file).suffix]))
    Phylo.draw(tree, do_show=False)
    plt.savefig(pathlib.Path(file).with_suffix(".png"))
    tree = tree.as_phyloxml()
    return pathlib.Path(file).with_suffix(".png"), tree.count_terminals(), tree.total_branch_length()

def calculate_distance_impl(file,leaf1,leaf2):
    tree = Phylo.read(file, phylo_formats[pathlib.Path(file).suffix])
    tree = tree.as_phyloxml()
    elem1 = tree.find_any(lambda leaf : leaf.name == leaf1)
    if(leaf2 == ''):
        elem2 = None
    else:
        elem2 = tree.find_any(lambda leaf: leaf.name == leaf2)
    return tree.distance(elem1, elem2)

def common_ancestor_impl(file, children):
    tree = Phylo.read(file, phylo_formats[pathlib.Path(file).suffix])
    tree = tree.as_phyloxml()
    tree.root.color = (128, 128, 128)
    common_ancestor_arg = []
    for child in children:
        common_ancestor_arg.append({"name": child})
    mrca = tree.common_ancestor(common_ancestor_arg)
    mrca.color = "red"
    Phylo.draw(tree, do_show=False)
    plt.savefig(pathlib.Path(file).with_suffix(".png"))
    return pathlib.Path(file).with_suffix(".png")

def route_impl(file, node):
    tree = Phylo.read(file, phylo_formats[pathlib.Path(file).suffix])
    tree = tree.as_phyloxml()
    tree.root.color = (128, 128, 128)
    target_leaf = tree.find_any(lambda leaf: leaf.name == node)
    clades = tree.get_path(target_leaf)
    for clade in clades:
        clade.color = "red"
    Phylo.draw(tree, do_show=False)
    plt.savefig(pathlib.Path(file).with_suffix(".png"))
    return pathlib.Path(file).with_suffix(".png")

