def fasta_reader(fasta_file):
    id_seq = None
    seq_fasta = []
    with open(fasta_file) as file:
        for line in file:
            line = line.strip()
            if line[0] == '>':
                if len(seq_fasta) == 0:
                    id_seq = line
                else:
                    yield id_seq, ''.join(seq_fasta)
                    id_seq = line
                    seq_fasta = []
            else:
                seq_fasta.append(line)
        yield id_seq, ''.join(seq_fasta)


reader = fasta_reader("seq.fasta")
print(type(reader))
for id_, seq in reader:
    print(id_, seq[:50])
