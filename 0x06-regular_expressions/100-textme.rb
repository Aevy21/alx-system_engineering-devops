#!/usr/bin/env ruby
# Output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?[0-9]:-?[0-9]:-?[0-9]:-?[0-9]:-?[0-9])\]/).join(',')
