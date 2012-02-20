import time

def get_comments_to_nodes(db):
    db.query("""SELECT comments.uid,node.uid,comments.timestamp FROM comments JOIN node ON comments.nid=node.nid""")
    results = db.store_result()
    f = open('comments_to_nodes.csv','w')
    f.write('out-degree,in-degree,timestamp\n')
    for i in range(results.num_rows()):
        single_row = results.fetch_row()[0]
        single_row = (single_row[0], single_row[1], time.ctime(int(single_row[2])))
        f.write('%s,%s,%s\n' % single_row)
    f.close()

def get_comments_to_comments(db):
    db.query("""SELECT orig.uid,dest.uid,orig.timestamp FROM comments AS orig JOIN comments AS dest ON orig.pid=dest.cid WHERE orig.pid!=0""")
    results = db.store_result()
    f = open('comments_to_comments.csv','w')
    f.write('out-degree,in-degree,timestamp\n')
    for i in range(results.num_rows()):
        single_row = results.fetch_row()[0]
        single_row = (single_row[0], single_row[1], time.ctime(int(single_row[2])))
        f.write('%s,%s,%s\n' % single_row)
    f.close()
