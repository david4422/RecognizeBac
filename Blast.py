from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
import tkinter as tk
from tkinter import *
import threading
import os
import time

def details(data):
    print("starting details..")
    seq_record = Seq(data)
    print("finished seq")

    res = (NCBIWWW.qblast("blastn", "nt", seq_record))

    print("start writing")
    # save the res into file
    with open("blast_BE_isolate.xml" , "w+") as save_to:
        save_to.write(res.read())
        save_to.close()


    # res = open("blast_BE_isolate.xml" , 'r')

def parse_alignment(str, top):
    print(str)
    # bactria = Label(top, text=str)
    # bactria.grid(row=5, column=2)


def print_res(res , top):
    blast_record = NCBIXML.read(res)
    str = ""
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            str += alignment.title.split('| ')[1].split(',')[0] + "\n"
    parse_alignment(str,top)