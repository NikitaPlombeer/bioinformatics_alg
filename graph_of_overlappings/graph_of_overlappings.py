file = open("input.txt")
kmers = file.readlines()

for idx, value in enumerate(kmers):
    kmers[idx] = value.strip()

for kmer in kmers:
    res = kmer + " -> "
    has = False
    for subkmer in kmers:
        if kmer != subkmer and kmer[1:] == subkmer[:-1]:
            has = True
            res = res + subkmer + ","
    if has:
        print(res[:-1])
