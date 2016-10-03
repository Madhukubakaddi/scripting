package chip_name;
use YAML;

#############################################################################

$regfile_1 = $ARGV[0];
my $filename = 'regsfile_to_yaml.yml';
open(my $fh, '>', $filename) or die "$!";

print "Start Extracting data from $regfile_1 ...\n";
require $regfile_1;
print $fh Dump( $formats), "\n";    
close $fh;
