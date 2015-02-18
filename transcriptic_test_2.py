__author__ = "Joshua Hancock"

import sys


# Dictionary for converting an RNA codon into an Amino Acid. Stop codon represented by *.
aa_convert = {"AUU": "I", "AUC": "I", "AUA": "I", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "UUA": "L", "UUG": "L", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "UUU": "F",
              "UUC": "F", "AUG": "M", "UGU": "C", "UGC": "C", "GCU": "A", "GCC": "A", "GCA": "A",
              "GCG": "A", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", "CCU": "P", "CCC": "P",
              "CCA": "P", "CCG": "P", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "UCU": "S",
              "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S", "UAU": "Y", "UAC": "Y",
              "UGG": "W", "CAA": "Q", "CAG": "Q", "AAU": "N", "AAC": "N", "CAU": "H", "CAC": "H",
              "GAA": "E", "GAG": "E", "GAU": "D", "GAC": "D", "AAA": "K", "AAG": "K", "CGU": "R",
              "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R", "UAA": "*", "UGA": "*",
              "UAG": "*"
}


# Start and stop codons to be checked when the program iterates to find start and stop points
codons = ["UAA", "UGA", "UAG"]
start_codons = ["AUG"]
stop_codons = set(codons)


# Opens the DNA file to be read
def dna(file_name):
    with open(file_name, "r") as f:
        for line in f:
            return line


# Converts DNA file into RNA.
def dna_to_rna(file_name):
    with open(file_name, "r") as x:
        nucleotides = list(x)
        rna = [letter.replace('T', 'U') for letter in nucleotides]
    return rna


# Iterates through RNA strand to find start and stop codons. Places functional RNA into new list.
def rna_to_aa(file_name):
    rna = dna_to_rna(file_name)
    subset = []
    start = -1
    rna_string = ''.join(rna)
    for i in range(0, len(rna_string)):
        if ''.join(rna_string[i:i + 3]) in start_codons and start == -1:
            start = i
        elif ''.join(rna_string[i:i + 3]) in stop_codons:
            amino_acid = ''.join(rna_string[start:i + 3])
            if start != -1 and len(amino_acid) % 3 == 0:
                subset.append(amino_acid)
                start = -1
    return subset


# Converts functional RNA strands produced from previous function and converts into amino acid chain using dictionary.
def rna_to_chain(file_name):
    aa_chains = rna_to_aa(file_name)
    proteins = []
    for chain in aa_chains:
        aa_chain = ''

        for index in range(0, len(chain), 3):
            sequence = chain[index:index + 3]
            aa_chain += aa_convert[sequence]

        proteins.append(aa_chain)

    return proteins


# Allows for user to input flag for which data they wish to return.
if __name__ == '__main__':

    FLAG_1 = '--rna'
    FLAG_2 = '--genes'
    try:
        flag = sys.argv[1]
        file_name = sys.argv[2]

        if flag == FLAG_1:
            print "RNA: " + ''.join(dna_to_rna(file_name))

        elif flag == FLAG_2:
            print "%s valid protein(s) can be produced from this sequence" % (len(rna_to_chain(file_name)))
            print "DNA: " + dna(file_name)
            print "RNA: " + ''.join(dna_to_rna(file_name))
            print "Amino Acid Chain: " + str(rna_to_chain(file_name))

        else:
            print "INVALID FLAG SUPPLIED, USE '--rna' or '--genes'"
    except IndexError:
        print "Oops! There needs to be a flag (--rna or --genes) and file with DNA."
    except IOError:
        print "Not a valid text file."