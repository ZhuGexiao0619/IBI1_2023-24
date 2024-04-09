import re
seq="ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
seq1=re.compile(r"GTGTGT|GTCTGT")
total=0
match=None
while True:
    match=seq1.search(seq)
    if not match:
        break
    total+=1
    seq=seq[match.end():]
print(f"{total}")
