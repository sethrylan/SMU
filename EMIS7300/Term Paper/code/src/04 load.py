__author__="gaineys"
__date__ ="$Nov 12, 2012 8:20:22 PM$"

import MySQLdb

# This will use DATA LOAD and call on each movie file
#  - A LOT faster than doing inserts.

# connect to the MySQL server
db = MySQLdb.connect("127.0.0.1","root","Three&34Platypi","netflix" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

movieCount = 0
errorCount = 0

for n in range(1, 17771):
#    movie = open('C:/School/EMIS7300/term paper/nf_prize_dataset/dataload/ratings.' + str(n).zfill(7) + '.txt').read()
#        movie = Dir.getwd << "C:\\School\\EMIS7300\\term paper\\nf_prize_dataset//data-load//ratings.#{n.to_s.rjust(7, '0')}.txt"
#    sql = 'LOAD DATA INFILE \'%s\' INTO TABLE ratings FIELDS TERMINATED BY \',\' LINES TERMINATED BY \'\n\';'
#    cursor.execute(sql, movie)
    result = "no result yet!"
    try:
        result = cursor.execute("LOAD DATA INFILE '" + 'C:/School/EMIS7300/term paper/nf_prize_dataset/dataload/ratings.' + str(n).zfill(7) + '.txt' +  "' INTO TABLE ratings FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
        movieCount = movieCount + 1
    except MySQLdb.IntegrityError:
        errorCount += 1
        print 'Error #' + str(errorCount)

    if movieCount % 100 == 0:
        print str(movieCount) + " : " + str(result)

#        p "#{movieCount} : #{result}" if movieCount % 100 == 0


db.commit()
db.close()


if __name__ == "__main__":
    print "Hello World";
