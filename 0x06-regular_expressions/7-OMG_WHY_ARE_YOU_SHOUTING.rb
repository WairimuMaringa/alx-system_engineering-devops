#!/usr/bin/env/ruby
# Regular expression that matches only capital letters
puts ARGV[0].scan(/[[:upper:]]/).join
