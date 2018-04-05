import md5
import sys
import string
import random

HASH = 0
CONTENTS = 1
PAD = 2

def verify(blocks):
    i=0
    for i in range(1,len(blocks)):
        prev_hash = blocks[i-1][HASH]
        contents = blocks[i][CONTENTS]
        pad = blocks[i][PAD]
        block = (prev_hash+
                 "\n---\n"+
                 contents+
                 "\n---\n"+
                 pad)
        hash=md5.new(block).hexdigest().upper()
        sys.stdout.write(hash+": ")
        if(hash==blocks[i][HASH]  # hash is valid
           and hash[0:2]=='AA'):  # AND it meets the rule
            print("OK")
        else:
            print("ERROR")
            print("Block %d [%s] is invalid" % (i,contents))
            break

def mine(contents, prev_hash, verbose):
    pad = 0
    print("linking to: "+prev_hash)
    while(1):
        pad = ''.join([random.choice(string.ascii_letters +
                                     string.digits) for n in xrange(7)])
        block = (prev_hash+
                 "\n---\n"+
                 contents+
                 "\n---\n"+
                 pad)
        hash = md5.new(block).hexdigest().upper()
        if(verbose):
            sys.stdout.write("["+hash+"]\n")
            sys.stdout.flush()
        if(hash[0:3] == 'CCC'):
            break
    return (hash, pad)

