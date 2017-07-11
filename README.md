# dirtreemod-sysadmin

Recursively list files in order of modification time.

# Purpose

When it's time to reboot a server, I like to see what files have been changed
in the /etc directory in an effort to understand what might stop a system
from rebooting properly.

The ls command is great for listing files in order of modification (ls -lrt)
however when the -R (recursive) option is used, i.e. ls -lrtR the output is
broken up into directories obscuring the results.

# Bash equivalent.

```bash
#!/bin/bash


find /etc -type f | while read file
do
	echo $file $(perl -le 'print((stat("'"$file"'"))[9])')
done | sort -n -k 2 | while read file moddate
do
	ls -ld "$file"
done
```

# Comments

The bash version runs ls for every file because xargs doesn't guarentee the
order of arguments to the command it runs, defeating the purpose of the
script.

Bash version uses Perl to stat the file because not all UNIX variants have a
stat command.
