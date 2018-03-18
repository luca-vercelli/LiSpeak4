#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
#
# Read a word from stdin, print the corresponding line (word + pronounce) to stdout
# Italian only
#
# Usage:
# cat 7346.vocab | ./guess_pronounce.py > 7346.it.dic


FONEMI = [     #order is worth, this is not a dict
    # gn    
    ( 'gn' , [['JJ','JJ']]),
    # gl    
    ( 'glia' , [['LL','LL','a']]),
    ( 'glie' , [['LL','LL','e']]),
    ( 'gli' , [['LL','LL','i']]),
    ( 'glio' , [['LL','LL','o']]),
    ( 'gliu' , [['LL','LL','u']]),
    ( 'gl' , [['g','l']]),
    # sc
    ( 'scia' , [['SS','SS', 'a']]),
    ( 'sce' , [['SS','SS', 'e']]),
    ( 'sci' , [['SS','SS', 'i']]),
    ( 'scio' , [['SS','SS', 'o']]),
    ( 'sciu' , [['SS','SS', 'u']]),
    ( 'sc' , [['s','k']]),
    # c,g    
    ( 'cia' , [['tSS','a']]),
    ( 'ce' , [['tSS','e']]),
    ( 'ci' , [['tSS','i']]),
    ( 'cio' , [['tSS','o']]),
    ( 'ciu' , [['tSS','u']]),
    ( 'ccia' , [['tSS','tSS','a']]),
    ( 'cce' , [['tSS','tSS','e']]),
    ( 'cci' , [['tSS','tSS','i']]),
    ( 'ccio' , [['tSS','tSS','o']]),
    ( 'cciu' , [['tSS','tSS','u']]),
    ( 'gia' , [['dZZ','a']]),
    ( 'ge' , [['dZZ','e']]),
    ( 'gi' , [['dZZ','i']]),
    ( 'gio' , [['dZZ','o']]),
    ( 'giu' , [['dZZ','u']]),
    ( 'ggia' , [['dZZ','dZZ','a']]),
    ( 'gge' , [['dZZ','dZZ','e']]),
    ( 'ggi' , [['dZZ','dZZ','i']]),
    ( 'ggio' , [['dZZ','dZZ','o']]),
    ( 'ggiu' , [['dZZ','dZZ','u']]),
    ( 'c' , [['k']]),
    ( 'g' , [['g']]),
    ( 'h' , [[]]),
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
    #apostrofo
    ( '\'' , [[]]),
    ]

VOCALI = [ 'a', 'e', 'i', 'o', 'u']
LETTERE_ACCENTATE = [ 'à', 'á', 'è', 'é', 'ì', 'ì', 'ò', 'ó', 'ù', 'ú']
LETTERE_ACCENTATE_MAP = {
     'à' : 'a1',
     'á' : 'a1',    
     'è' : 'e1',
     'é' : 'e1',
     'ì' : 'i1',
     'í' : 'i1',
     'ò' : 'o1',
     'ó' : 'o1',
     'ù' : 'u1',
     'ú' : 'u1',
    }

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
        
        #here, output = [[[asia]],[[a]],[[s],[z]],[[j,a]]]
        output = product(*output)
        #now, output = [[[asia],[a],[s],[j,a]],[[asia],[a],[z],[j,a]]]

        #merge
        for i in range(len(output)):
            word = output[i] 
            word = [ph for x in word for ph in x]
            output[i] = word
        #now, output = [[asia,a,s,j,a],[asia,a,z,j,a]]
        
        #cerco la penultima vocale
        for word in output:
            last = False
            for i in reversed(range(len(word))):
                phonema = word[i]
                if phonema in LETTERE_ACCENTATE:
                        word[i] = LETTERE_ACCENTATE_MAP[phonema] 
                        break
                if phonema in VOCALI:
                    if not last:
                        # evito l'ultima vocale
                        last = True
                    else:
                        #penultima
                        word[i] = phonema + "1"     # 'e1' may be 'EE' too :( 
                        break
        
        #print
        i = 1
        for word in output: 
            if i > 1:
                word[0] = word[0] + "(" + str(i) + ")"
            print orig_word + " " + " ".join(word)
            i += 1


