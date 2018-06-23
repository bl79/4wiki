#!/bin/sh
python3 ~/pwb/pwb.py add_text.py -pt:0 -file:"pages2delete.txt" -text:"{{d|}}" -up -except:"\{\{d[^|}]" -family:wikisource -always #  -simulate
