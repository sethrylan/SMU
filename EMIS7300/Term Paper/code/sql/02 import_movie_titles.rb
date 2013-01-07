begin
      sql= <<-'EOS' # drop & create table
        USE `netflix`;
        DROP TABLE IF EXISTS `movies`;
        CREATE TABLE `movies` (
          `id` int(5) NOT NULL default '0',
          `year` int(4) default '0',
          `title` varchar(255) NOT NULL default '',
          PRIMARY KEY  (`id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
      EOS

      out = File.open("C:/School/EMIS7300/term paper/EMIS7300_code/sql/movies-import.sql", "w")
      out.write(sql)

      File.open("C:/School/EMIS7300/term paper/nf_prize_dataset/movie_titles.txt", "r") do |movies|
        movies.each_line { |movie|
            id, year, title = movie.chomp.scan(/(\d+),(\d+|NULL),(.*)/).flatten

            # escape ' and \ characters
            title = title.gsub(/\\/, '\&\&').gsub(/'/, "''")
            out.write("\nINSERT INTO `movies` (`id`,`year`,`title`) VALUES (#{id},#{year},'#{title}');")
        }
      end

      out.close
rescue => err
      puts "Exception: #{err}"
end
