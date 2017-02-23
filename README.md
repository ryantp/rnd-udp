# rnd-udp

rnd-udp (Random User Defined Processes) -- a collection of simple scripts that enhance system commands (mostly going to be Win32 based).

=================================================
Repo Notes:

In my day job, I get to do a certain process
which puts me in the position to have access to
a computer and use (most) all the tools to do
said process.

Since I moonlight as a programmer, I tend to
take some inspiration from those tools (
including all their faults (good stuff to learn
from :P)), and implement my own (although
_my_ scripts are more along the lines of sys-
administation).

================================================

LIST:
- bcx.py -- inspired to write this because of my day job o.o; creates .PNG barcode images of given values [max_len=15]; NOTE: requires `pybarcode`
- better_win_taskkill.py -- interactive taskkill program (still being polished); call without params for interactive session, with params for single-call cli use
                              (NOTE: gets called from batch file called `tkill.bat` (on local machine).)
- checksum.py -- performs a rudamentary sha calculation of a file's contents
- fibn.py -- simple fibonocci program, because why not?
- grep.py -- a python implementation of grep
- makefile.py -- makes a file of .* type in the cwd; a Win32 version of unix's `touch` function
- open_file.py -- because I am tired of having to type in `notepad <filename>` all the time to add quick edits to files :/
- rpw.py -- prints string of random character of N length (if I'm not feeling too creative when it comes time to come up with a new password :P)
- textev.py -- from `http://usingpython.com/dl/evolutionText.py`; it's a cute little program, so why not?
