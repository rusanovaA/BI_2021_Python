#import Bio
from Bio.Seq import Seq
from Bio import SeqIO
import seaborn as sns


class DoctorWho:
    number_of_hearts = 2
    can_regenerate = True

    def __init__(self, number):
        self.number = number

    def save_the_world(self):
        print("I'm the Doctor. I'm a Timelord. I'm from the Planet Gallifrey \
              in the constellation of Kasterborous. I'm 903 years old, \
              and I'm the man who's gonna save your lives and all 6 billion \
              people on the planet below. You got a problem with that?")

    def run_fast(self):
        print("Run!!!")

    def be_kind(self):
        print("In 900 years of time and space, I’ve never met anyone who wasn’t important")


class DescribeRNA:
    def __init__(self, rna_seq):
        self.rna_seq = Seq(rna_seq)
        if rna_seq.find("T") != -1:
            print("Please, try again! The seq in not RNA")
        else:
            print("It is RNA. Continue")

    def translate_rna(self):
        print(Seq.translate(Seq(self.rna_seq)))

    def back_transcribe_rna(self):
        print(Seq.back_transcribe(Seq(self.rna_seq)))


class SetInherited(set):
    def __init__(self, *args):
        for i in args:
            if i > 0:
                self.add(i)
            else:
                continue

    def add(self, new_i):
        if new_i > 0:
            super().add(new_i)
        else:
            print("The number is negative. Try another one")


path = 'fasta_test_new.fasta'


class FastaStat:
    def __init__(self, fasta_path):
        self.fasta_path = fasta_path

    def seq_count(self):
        input_file = open(self.fasta_path)
        count_seq = []
        for line in input_file:
            if line.startswith('>'):
                count_seq.append(1)
            else:
                continue
        print(sum(count_seq))
        input_file.close()

    def length_dist(self):
        input_file = open(self.fasta_path)
        lengths = []
        fasta_parse = SeqIO.parse(input_file, "fasta")
        for seq in fasta_parse:
            lengths.append(len(seq.seq))
        dist_plot = sns.displot(lengths, color="lightblue")
        dist_plot.set(xlabel="Sequences length distribution")
        input_file.close()

    def gc_count(self):
        input_file = open(self.fasta_path)
        fasta_file = input_file.read()
        c = 0
        a = 0
        g = 0
        t = 0
        for seq in fasta_file:
            if "C" in seq:
                c += 1
            elif "G" in seq:
                g += 1
            elif "A" in seq:
                a += 1
            elif "T" in seq:
                t += 1
        gc_content = (g + c) * 100 / (a + t + g + c)
        print("The GC content is % f " % gc_content, "%")
        input_file.close()
