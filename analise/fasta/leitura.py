from Bio import SeqIO

proteinas = []

for protein in SeqIO.parse('sequence.fasta', 'fasta'):
    t = (str(protein.id), str(protein.seq))
    proteinas.append(t)

print(proteinas[0])