#!/usr/bin/env python2.7
#
# Read a word from stdin, print the corresponding line (word + pronounce) to stdout
# Italian only

FONEMI = [     #order is worth, this is not a dict
    # gn    
    ( 'gn' , ['JJ','JJ']),
    # gl    
    ( 'glia' , ['LL','LL','a']),
    ( 'glie' , ['LL','LL','e']),
    ( 'glio' , ['LL','LL','o']),
    ( 'gliu' , ['LL','LL','u']),
    ( 'gl' , ['LL','LL']),
    # sc
    ( 'sch' , ['s','k']),
    ( 'sc' , ['SS','SS']),
    # c,g    
    ( 'cia' , ['tSS','a']),
    ( 'cio' , ['tSS','o']),
    ( 'ciu' , ['tSS','u']),
    ( 'ce' , ['tSS','e']),
    ( 'ci' , ['tSS','i']),
    ( 'ccia' , ['tSS','tSS','a']),
    ( 'ccio' , ['tSS','tSS','o']),
    ( 'cciu' , ['tSS','tSS','u']),
    ( 'cce' , ['tSS','tSS','e']),
    ( 'cci' , ['tSS','tSS','i']),
    ( 'gia' , ['dZZ','a']),
    ( 'gio' , ['dZZ','o']),
    ( 'giu' , ['dZZ','u']),
    ( 'ge' , ['dZZ','e']),
    ( 'gi' , ['dZZ','i']),
    ( 'ggia' , ['dZZ','dZZ','a']),
    ( 'ggio' , ['dZZ','dZZ','o']),
    ( 'ggiu' , ['dZZ','dZZ','u']),
    ( 'gge' , ['dZZ','dZZ','e']),
    ( 'ggi' , ['dZZ','dZZ','i']),
    ( 'c' , ['k']),
    ( 'g' , ['g']),
    ( 'h' , []),
    # s,z
    ( 's' , ['s']),    #may be 'z' too :(
    ( 'z' , ['dz']),   #may be 'ts' too :(
    # dittonghi
    ( 'ie' , ['j','e']),
    ( 'ia' , ['j','a']),
    ( 'io' , ['j','o']),
    ( 'iu' , ['j','u']),
    #apostrofo    
    ( '\'' , []),
    ]

VOCALI = [ 'a', 'e', 'i', 'o', 'u']

if __name__ == "__main__":
    
    import sys

    for line in sys.stdin:
        line = line.lower().replace('\r','').replace('\n','')
        output = [line]

        # sostituzione fonemi
        while len(line) > 0:
            found = False
            for (x,y) in FONEMI:
                if line.startswith(x):
                    output.extend(y)
                    line = line[len(x):]
                    found = True
                    break
            if not found:
                output.append(line[0]) 
                line = line[1:]
        
        #cerco la penultima vocale
        last = False
        for i in reversed(range(len(output))):
            w = output[i]
            if w in VOCALI:
                if not last:
                    # evito l'ultima vocale
                    last = True
                else:
                    #penultima
                    output[i] = w + "1"     # 'e1' may be 'EE' too :( 
                    break

        #print
        print " ".join(output)

