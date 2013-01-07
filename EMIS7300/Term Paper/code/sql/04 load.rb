  # This will use DATA LOAD and call on each movie file
  #  - A LOT faster than doing inserts.

  require 'rubygems'

  require "dbi"

   begin
    # connect to the MySQL server
    dbh = DBI.connect("DBI:Mysql:netflix:127.0.0.1", "root", "Three&34Platypi")

    row = dbh.select_one("SELECT VERSION()")
    p "Running on version: " + row[0]
    movieCount = 0

    1.upto(17770) do |n|
        movie = Dir.getwd << "C://School//EMIS7300//term paper//nf_prize_dataset//dataload//ratings.#{n.to_s.rjust(7, '0')}.txt"
        result = dbh.do("LOAD DATA INFILE '#{movie}' INTO TABLE ratings FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
        p "#{movieCount} : #{result}" if movieCount % 100 == 0

        movieCount = movieCount + 1
    end

   rescue DBI::DatabaseError => e
       p "An error occurred"
       p "Error code: #{e.err}"
       p "Error message: #{e.errstr}"
   ensure
       p "Exiting on: #{movieCount}"
       dbh.disconnect if dbh
   end
