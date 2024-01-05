#!/usr/bin/env ruby
# Output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/).join(",")
