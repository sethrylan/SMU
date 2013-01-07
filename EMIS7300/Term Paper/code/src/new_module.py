

import MySQLdb

db = MySQLdb.connect("127.0.0.1","root","pass","netflix" )
movieCount, errorCount, cursor = 0, 0, db.cursor()

for n in range(1, 17771):
    try:
        result = cursor.execute("LOAD DATA INFILE '" + '/path/ratings.'\
                + str(n).zfill(7) +  "' INTO TABLE ratings FIELDS TERMINATED\
                BY ',' LINES TERMINATED BY '\n'")
        movieCount += 1
    except MySQLdb.IntegrityError:
        errorCount += 1
        print 'Error #' + str(errorCount)
db.commit()
db.close()



