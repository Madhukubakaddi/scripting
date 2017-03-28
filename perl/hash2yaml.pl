#!/usr/local/bin/perl
# USAGE:hash2yaml.pl <file_name>
# OUTPUT: myyaml.yml
package <pkg_name>;
#Replace <pkg_name> with the name of the package. 
#This line needs to be present with the hash/perl file to be converted has this line
use YAML;

$file_1 = $ARGV[0];#file_1 represents the hash file which needs to be converted
my $filename = 'myyaml.yml';
open(my $fh, '>', $filename) or die "$!";

print "Start Extracting data from $file_1 ...\n";
# Add "1;" at the end of hash/perl file 
require $file_1;
print $fh Dump($f,$m,$r), "\n";# $f,$m,$r represent the main keys
close $fh;
