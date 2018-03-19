#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
#
# Read a word from stdin, print the corresponding line (word + pronounce) to stdout
# Italian only
#
# Usage:
# cat 7346.vocab | ./guess_pronounce.py > 7346.it.dic
#
# FIXME gestione degli accenti: troppo complicata
# accetto tutte le varianti possibili


FONEMI = [     #order is worth, this is not a dict
    # gn    
    ( 'gn' , [['JJ','JJ']]),
    # gl    
    ( 'glia' , [['LL','LL','a']]),
    ( 'glie' , [['LL','LL','e']]),
    ( 'glio' , [['LL','LL','o']]),
    ( 'gliu' , [['LL','LL','u']]),
    ( 'gli' , [['LL','LL','i']]),
    ( 'gl' , [['g','l']]),
    # sc
    ( 'scia' , [['SS','SS', 'a']]),
    ( 'scio' , [['SS','SS', 'o']]),
    ( 'sciu' , [['SS','SS', 'u']]),
    ( 'sce' , [['SS','SS', 'e']]),
    ( 'sci' , [['SS','SS', 'i']]),
    ( 'sc' , [['s','k']]),
    # c,g    
    ( 'cia' , [['tSS','a']]),
    ( 'cio' , [['tSS','o']]),
    ( 'ciu' , [['tSS','u']]),
    ( 'ce' , [['tSS','e']]),
    ( 'ci' , [['tSS','i']]),
    ( 'ccia' , [['tSS','tSS','a']]),
    ( 'ccio' , [['tSS','tSS','o']]),
    ( 'cciu' , [['tSS','tSS','u']]),
    ( 'cce' , [['tSS','tSS','e']]),
    ( 'cci' , [['tSS','tSS','i']]),
    ( 'gia' , [['dZZ','a']]),
    ( 'gio' , [['dZZ','o']]),
    ( 'giu' , [['dZZ','u']]),
    ( 'ge' , [['dZZ','e']]),
    ( 'gi' , [['dZZ','i']]),
    ( 'ggia' , [['dZZ','dZZ','a']]),
    ( 'gge' , [['dZZ','dZZ','e']]),
    ( 'ggi' , [['dZZ','dZZ','i']]),
    ( 'ggio' , [['dZZ','dZZ','o']]),
    ( 'ggiu' , [['dZZ','dZZ','u']]),
    ( 'c' , [['k']]),
    ( 'g' , [['g']]),
    ( 'h' , [[]]),
    #q
    ( 'q' , [['k']]),
    # s,z -> accettiamo 2 pronunce diverse
    ( 'ss' , [['s','s']]),
    ( 'zz' , [['ts','ts']]),
    ( 's' , [['s'],['z']]),
    ( 'z' , [['ts'],['dz']]),
    # dittonghi
    ( 'ie' , [['j','e']]),
    ( 'ia' , [['j','a']]),
    ( 'io' , [['j','o']]),
    ( 'iu' , [['j','u']]),
    ( 'ui' , [['w','i']]),
    ( 'ua' , [['w','a']]),
    ( 'uo' , [['w','o']]),
    #apostrofo
    ( '\'' , [[]]),
    #vowels
    ( 'à' , [['a']]),
    ( 'á' , [['a']]),
    ( 'e' , [['e']]),
    ( 'è' , [['e']]),
    ( 'é' , [['e']]),
    ( 'i' , [['i']]),
    ( 'ì' , [['i']]),
    ( 'í' , [['i']]),
    ( 'ó' , [['o']]),
    ( 'ò' , [['o']]),
    ( 'ù' , [['u']]),
    ( 'ú' , [['u']]),
    #for all other 1-byte letters, we assume ( 'x', [['x']])
    #this is not true for non-ASCII (2-bytes long) characters
    ]

VOWELS = [ 'a', 'e', 'i', 'o', 'u' ]

VOWELS_MAP_ACC = {
    'a' : ['a1'],
    'e' : ['e1','EE'],
    'i' : ['i1'],
    'o' : ['o1','OO'],
    'u' : ['u1'],
    }

#    ( 'a' , [['a'],['a1']]),
#    ( 'à' , [['a'],['a1']]),
#    ( 'á' , [['a'],['a1']]),
#    ( 'e' , [['e'],['e1'],['EE']]),
#    ( 'è' , [['e'],['e1'],['EE']]),
#    ( 'é' , [['e'],['e1'],['EE']]),
#    ( 'i' , [['i'],['i1']]),
#    ( 'ì' , [['i'],['i1']]),
#    ( 'í' , [['i'],['i1']]),
#    ( 'o' , [['o'],['o1']]),
#    ( 'ó' , [['o'],['o1']]),
#    ( 'u' , [['u'],['u1']]),
#    ( 'ù' , [['u'],['u1']]),
#    ( 'ú' , [['u'],['u1']]),

def product(*args):
    """
    each arg is a a list of lists
    @return a list of lists
    """
    if not args:
        return [[]]
    return [items + [item] for items in product(*args[:-1]) for item in args[-1]]

if __name__ == "__main__":
    
    import sys

    for line in sys.stdin:
        line = line.lower().replace('\r','').replace('\n','')
        orig_word = line
        output = []
        
        # sostituzione fonemi
        while len(line) > 0:
            found = False
            for (x,y) in FONEMI:
                if line.startswith(x):
                    output.append(y)
                    line = line[len(x):]
                    found = True
                    break
            if not found:
                output.append([[line[0]]]) 
                line = line[1:]
        
        #debug
        #print output

        #here, output = [[[a]],[[s],[z]],[[j,a]]]
        output = product(*output)
        #now, output = [[a],[s],[j,a]],[[a],[z],[j,a]]]

        #merge
        for i in range(len(output)):
            word = output[i] 
            word = [ph for x in word for ph in x]
            output[i] = word
        #now, output = [[a,s,j,a],[a,z,j,a]]
        
        #1 and only 1 accented vowel
        newoutput = []
        for word in output:
            has_one_vowel = False
            i = 0
            for ph in word:
                if ph in VOWELS:
                    has_one_vowel = True
                    for ph2 in VOWELS_MAP_ACC[ph]:
                        word2 = list(word)
                        word2[i] = ph2
                        newoutput.append(word2)
                i += 1
            if not has_one_vowel: # ?!?
                newoutput.append(word)
        output = newoutput
        #now, output = [[a1,s,j,a],[a,s,j,a1],[a1,z,j,a],[a,z,j,a1]]

        #print
        i = 1
        for word in output:
            variant = "" 
            if i > 1:
                variant = "(" + str(i) + ")"
            print orig_word + variant + " " + " ".join(word)
            i += 1


