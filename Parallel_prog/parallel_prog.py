import sys
import argparse
from concurrent.futures import ProcessPoolExecutor

parser = argparse.ArgumentParser(description="Count all symbols in fasta file")
parser.add_argument("-f", "--fasta", default=sys.stdin,
                    help="Your data in fasta format")
parser.add_argument("-t", "--threads", default=1, help="Indicate the desired number of threads")
args = parser.parse_args()


def fasta_reader(fasta_file):
    id_seq = None
    seq_fasta = []
    with open(fasta_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if len(seq_fasta) == 0:
                    id_seq = line
                else:
                    yield id_seq, ''.join(seq_fasta)
                    id_seq = line
                    seq_fasta = []
            else:
                seq_fasta.append(line)
        yield id_seq, ''.join(seq_fasta)


reader = fasta_reader(args.fasta)


def i_counter(yeild_output):
    seq_id = yeild_output[0]
    seq = yeild_output[1]
    dir_sym = {}
    for i in seq:
        if i in dir_sym.keys():
            dir_sym[i] += 1
        else:
            dir_sym[i] = 0

    return f"Contig {seq_id}:" + str(", ".join(f'{key}={value}' for key, value in dir_sym.items())) + "\n"


if __name__ == '__main__':
    n_threads = int(args.threads)
    with ProcessPoolExecutor(n_threads) as pool:
        results = pool.map(i_counter, reader)
    sys.stdout.writelines(results)
