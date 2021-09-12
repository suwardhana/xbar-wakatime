#!/bin/bash

#
# Include BitBar metadata like this at the top of the file
# (commented out, of course ):
#
# <xbar.title>Cycle text and detail text</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Mat Ryer</xbar.author>
# <xbar.author.github>matryer</xbar.author.github>
# <xbar.desc>Example   of how to include items that cycle in the top, and items that only appear in the dropdown.</xbar.desc>
# <xbar.image>https://camo.githubusercontent.com/5cec3248a9fc4eede235ead682a65f977577f670/68747470733a2f2f7261772e6769746875622e636f6d2f6d6174727965722f6269746261722f6d61737465722f446f63732f4269744261722d4578616d706c652d4d656e752e706e67</xbar.image>
# <xbar.abouturl>https://github.com/matryer/bitbar-plugins/blob/master/Tutorial/cycle_text_and_detail.sh</xbar.abouturl>
#
# Text above --- will be cycled through in the menu bar,
# whereas text underneath will be visible only when you
# open the menu.
#
index=$[($RANDOM % 7 )]
text=("Bisa yuk bisa" "Istigfar" "Don't Slip" "Hidup ini singkat" "Selamat Produktif Dhan" "Ingat Waktu" "Malu jika malas")
echo ${text[$index]}
echo ---
echo These lines are only visible
echo when you open the menu.
