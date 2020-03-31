<?php
// inspired from https://github.com/wmde/wikidiff2-bench/

if(!extension_loaded("wikidiff2"))
{
    print("wikidiff2 extension not loaded\n");
    exit(1);
}

$result= wikidiff2_do_diff(file_get_contents($argv[1]), file_get_contents($argv[2]), 1000);

print $result;
?>
