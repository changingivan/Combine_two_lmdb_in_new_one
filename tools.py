import lmdb

in_db=lmdb.open('newdatabase',map_size=int(1e12))
in_txn = in_db.begin(write=True)

env1 = lmdb.open("previous_lmdb1")
env2 = lmdb.open("previous_lmdb2")

txn1 = env1.begin()
txn2 = env2.begin()

database1 = txn1.cursor()
database2 = txn2.cursor()

idx = 1
for (key, value) in database1:
    print "file 1:" + str(idx)
    idx += 1
    in_txn.put(key, value)
idx =1
for (key, value) in database2:
    print "file 2:"+ str(idx)
    idx += 1
    in_txn.put(key, value)
