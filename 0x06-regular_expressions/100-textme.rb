#!/usr/bin/env ruby
# Output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from: (?<sender>.*?)\] \[to: (?<receiver>.*?)\] \[flags: (?<flags>.*?)\]/).join(',')
