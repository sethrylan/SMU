# Transforms movie_id.txt into a 'DATA LOAD'able format for MySQL
#  - Assuming table is: [movie_id, user_id, rating, date]
#  - Not the most efficient solution - for people on unix/linux, you can apparently pipe the data into DATA LOAD directly (google is your friend)

begin
    1.upto(17770) do |n|
      out = File.open("C:/School/EMIS7300/term paper/nf_prize_dataset/dataload/ratings.#{n.to_s.rjust(7, '0')}.txt", "w")

      File.open("C:/School/EMIS7300/term paper/nf_prize_dataset/training_set/mv_#{n.to_s.rjust(7, '0')}.txt", "r") do |ratings|
        ratings.each_line { |rating|
          if rating =~ /(\d+),(\d+),(.*)/
            userid, rating, date = rating.scan(/(\d+),(\d+),(.*)/).flatten
            out.write("#{n},#{userid},#{rating},#{date}\n")
          end
        }
      end
     end

     out.close
rescue => err
      puts "Exception: #{err}"
end
