#!/usr/bin/python3
# File: funk-tionary-ex.py

def funk():
    counts = dict()
    funkgreats = ['rickjames', 'pfunk', 'bootsy','jamesbrown', 'pfunk', 'rogertroutman', 'bootsy', 'bar-kays', 'ohio-players']
    for name in funkgreats :
     if name not in counts:
         counts[name] = 1
     else :
         counts[name] += 1
    print(counts)
def main():
    funk()
if __name__ == "__main__":
    main()
