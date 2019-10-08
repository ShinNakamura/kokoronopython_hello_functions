# -*- coding: utf-8 -*-
#

import sys
import csv

def main():
    _, csvf = sys.argv

    with open(csvf, "rt", encoding="utf-8", newline=None) as f:
        cin = csv.DictReader(f)
        for row in cin:
            pass

if __name__=='__main__':
    main()
