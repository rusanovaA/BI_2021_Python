def transcribe(sequence):
    nucl_transcribe = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 'u', 't': 'a', 'g': 'c', 'c': 'g'}
    seq_transcribe = []
    seq_transcribe_join = []
    for nucl in sequence:
        seq_transcribe.append(nucl_transcribe[nucl])
        seq_transcribe_join = ''.join(seq_transcribe)
    print(seq_transcribe_join)
####
def reverse(sequence):
    reverse_seq = sequence[::-1]
    reverse_seq = ''.join(reverse_seq)
    print(reverse_seq)
####
def complement(sequence):
    nucl_complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g', 'U': 'A', 'u': 'a'}
    seq_complement = []
    seq_complement_join = []
    for nucl in sequence:
        seq_complement.append(nucl_complement[nucl])
        seq_complement_join = ''.join(seq_complement)
    print(seq_complement_join)
####
def reverse_complement(sequence):
    nucl_complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g', 'U': 'A', 'u': 'a'}
    seq_complement = []
    seq_rev_complement = []
    seq_rev_complement_join = []
    for nucl in sequence:
        seq_complement.append(nucl_complement[nucl])
        seq_rev_complement = seq_complement[::-1]
        seq_rev_complement_join = ''.join(seq_rev_complement)        
    print(seq_rev_complement_join)
####
true_DNA_nucl = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']
true_RNA_nucl = ['A', 'a', 'U', 'u', 'G', 'C', 'g', 'c']
true_command = ['transcribe', 'reverse', 'complement', 'reverse complement']
###
while True:
    command_name = input("Enter command: ")    
    if command_name not in true_command:
        print("Try again")
        continue    
    if command_name == 'exit':
        print("Good luck")
        break
    sequence = input("Enter sequence: ")
    sequence = list(sequence)
    correct_alphabet_DNA = set(sequence).issubset(true_DNA_nucl)
    correct_alphabet_RNA = set(sequence).issubset(true_RNA_nucl)
    if correct_alphabet_DNA is False and correct_alphabet_RNA is False:
        print("Try again")
        continue    
    if command_name == 'transcribe' and correct_alphabet_RNA == True:
        print("Try again")
    elif command_name == 'transcribe':
        transcribe(sequence)
    elif command_name == 'reverse':
        reverse(sequence)
    elif command_name == 'complement':
        complement(sequence)
    elif command_name == 'reverse complement':
        reverse_complement(sequence)
