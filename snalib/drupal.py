import _mysql
import time

def get_user_to_user(db):
    #db.query("""select comments.uid,node.uid,comments.timestamp from comments INNER JOIN node ON comments.nid=node.nid WHERE comments.nid=14;""")
    db.query("""select comments.uid,node.uid,comments.timestamp from comments INNER JOIN node ON comments.nid=node.nid""")
    results = db.store_result()
    f = open('comments_to_nodes.csv','w')
    f.write('out-degree,in-degree,timestamp\n')
    for i in range(results.num_rows()):
        single_row = results.fetch_row()[0]
        single_row = (single_row[0], single_row[1], time.ctime(int(single_row[2])))
        f.write('%s,%s,%s\n' % single_row)
    f.close()

def get_user_to_user(db):
    #db.query("""select comments.uid,node.uid,comments.timestamp from comments INNER JOIN node ON comments.nid=node.nid WHERE comments.nid=14;""")
    db.query("""select comments.uid,node.uid,comments.timestamp from comments INNER JOIN node ON comments.nid=node.nid""")
    results = db.store_result()
    f = open('comments_to_nodes.csv','w')
    f.write('out-degree,in-degree,timestamp\n')
    for i in range(results.num_rows()):
        single_row = results.fetch_row()[0]
        single_row = (single_row[0], single_row[1], time.ctime(int(single_row[2])))
        f.write('%s,%s,%s\n' % single_row)
    f.close()
