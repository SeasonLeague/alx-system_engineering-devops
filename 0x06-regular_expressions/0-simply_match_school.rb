#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method. Regexp must match `School`.
puts ARGV[0].scan(/School/).join
