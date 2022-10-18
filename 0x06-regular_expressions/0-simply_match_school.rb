#!/usr/bin/env ruby
# The regular expression must match school
puts ARGV[0].scan(/School/).join
