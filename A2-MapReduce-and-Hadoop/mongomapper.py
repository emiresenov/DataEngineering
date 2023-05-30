#!/usr/bin/env python
"""mapper.py"""

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:

    try:
        # Load line (tweet) as JSON
        tweet = json.loads(line)
        print('%s\t%s' % ("processed tweets", 1))
        text = tweet["text"] # Extract text field
        text = text.strip() # Clean whitespace
        words = text.split() # Split text into word array
        # Declare pronouns
        pronouns = ["han","hon","den","det","denna","denne","hen"]
        print('%s\t%s' % ("unique tweets", 1)) # output

        # increase counters
        for i in words:
            prn = pronouns # Alias the pronouns list
            word = i.lower() # Lower case the word
            if (word in prn):
                prn.remove(word) # Remove from aliased list
                print('%s\t%s' % (word, 1)) # output

    # For linebreak characters in txt file that cause json parse errors
    except:
        continue
