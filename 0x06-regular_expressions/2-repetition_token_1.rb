#!/usr/bin/env ruby
# The regular expression that matches the given cases
puts ARGV[0].scan(/hb{0,1}tn/).join
