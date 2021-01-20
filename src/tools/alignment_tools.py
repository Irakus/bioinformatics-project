from Bio.Align import AlignInfo

def fetch_additional_data(MSA):
    summary_align = AlignInfo.SummaryInfo(MSA)
    consensus = summary_align.dumb_consensus()
    print(consensus)
    PSSM = summary_align.pos_specific_score_matrix()
    print(PSSM)
    return consensus, PSSM