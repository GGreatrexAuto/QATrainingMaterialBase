#!/usr/local/bin/python

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Sigma final','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

#Format required:
#    The hex value of the character
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character

for pos, cname in enumerate(greek, start=0x03B1):
    try:
        char = chr(pos)
        #print(cname,":",char)
        """
        print("{0:#x} {1:<12s}: {2} {3}".
              format(pos, cname, char, char.upper()))
        """
        print(f"{pos:#x} {cname:<12s}: {char} {char.upper()}")
    except UnicodeEncodeError as err:
        print(cname, 'unknown', err)

