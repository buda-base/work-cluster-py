import csv

VALUETOLIST = {}

with open('alltitles-csv.csv',  newline='') as csvfile:
    srcreader = csv.reader(csvfile, delimiter=',')
    next(srcreader)
    for row in srcreader:
        value = row[2]
        if value not in VALUETOLIST:
            VALUETOLIST[value] = []
        VALUETOLIST[value].append(row[0])

def getbestcluster(l):
    lastid = None
    for id in sorted(l):
        if '_' not in id and 'WA0XL' not in id and 'NGMCP' not in id:
            return id
        lastid = id
    return lastid

IDTOCLUSTER = {}

#print(VALUETOLIST)

nbclustered = 0
for value, l in VALUETOLIST.items():
    if len(l) > 1:
        clusterval = getbestcluster(l)
        nbclustered += len(l) -1
        for id in l:
            if id != clusterval:
                IDTOCLUSTER[id] = clusterval
    if len(l) > 10:
        print(value)

with open('clusters.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    for id, cl in IDTOCLUSTER.items():
        writer.writerow([id, cl])

print("nb clustered: %d" % nbclustered)
