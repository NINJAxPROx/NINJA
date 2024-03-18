# -*- coding : utf-8 -*-

# Check python versions 
import sys
PY3X = sys.hexversion >= 0x3070000

__version__ = '2021.06'
__doc__ = """

 


      << Code By : @i4m_ninja >> 
                                     
                                           

\x1b[?25l"""

# Function to make unique name
def make_name(n):
    letters = ascii_lowercase + ascii_uppercase
    letters_len = len(letters)
    name = ''
    n += 1
    while n:
        n -= 1
        name = letters[n % letters_len] + name
        n //= letters_len
    return name

def anim_text(x):
    sys.stdout.write(x)
    sys.stdout.flush()
    sys.stdout.write('\r')

if __name__ == '__main__':
    # How to use
    if len(sys.argv) < 2:
        sys.exit('Awa bakar bena : python2' + ['',''][PY3X] + ' power.py filename.py')

    # About this program
    print(__doc__ + '[!] DECOMPILING ' + sys.argv[1] + ' WILL BEGIN. PLEASE WAIT...')

    # Check external modules
    try:
        if PY3X: from decompyle3.main import decompile
        else: from uncompyle6.main import decompile
    except ImportError as e:
        sys.exit('[ERROR] ' + e.message + ' :-\\')

    # Import standard lib modules
    from time import sleep
    from string import ascii_lowercase, ascii_uppercase
    try: from StringIO import StringIO
    except: from io import StringIO
    import itertools, re
    sleep(0.001)

    # Read and write to IO
    f = StringIO()
    f.write(open(sys.argv[1]).read())
    sleep(0.001)

    # Check if there is exec or not
    if not re.search('(exec|eval)', f.getvalue()):
        sys.exit('SORRY, EXEC KEYWORD OR EVAL FUNCTION NOT FOUND :(')
    
    # Some keywords to find and replace
    k = make_name(8)
    w = { 'exec': k + '=', 'eval': k + '=' }
    # Simple spinner based on msf console
    c, g = "DECOMPILING CODE OBJECTS.... ", "-\|/"*11
    d = c.upper()
    s = [c[0:i] + d[i] + c[i+1:] + g[i] for i in range(len(c))]
    s = itertools.cycle(s)
    # Function to replace with multiple patterns
    _ = lambda x, y: re.compile("(%s)" % "|".join(map(re.escape, x.keys()))).sub(lambda z: x[z.string[z.start():z.end()]], y, count=1)
    # Output filename
    o = sys.argv[1][:-3] + '_dec.py'
    # Make it locals and globals
    d = dict(locals(), **globals())
    del(PY3X, g)
    
    # Let's Rock n Roll...
    while True:
        try:
            # ... dance dance dance ...
            c = _(w, f.getvalue()).replace('\0','')
            if not c: break
            # Clean IO
            f.truncate(0)
            # ... dance dance dance ...
            exec(c, d, d)
            c = locals()['d'][k]
            # Show spinner
            anim_text('[!] ' + next(s))
            # Decompile with uncompyle6/decompyle3
            try: decompile(None, c, f)
            except: f.write(c)
            # Check if there is no decode then stop loop
            if not re.search(r'(^exec|eval|module$)', f.getvalue(), flags=re.M): break
        except KeyboardInterrupt:
            sys.exit('\x1b[?25h\n')
        except Exception as e:
            sys.exit('\x1b[?25h' + str(e.message) + '\n')
        # Take a breath
        sleep(0.001)

    # Sit back, relax and enjoy ;)
    c = f.getvalue().replace('\0','').strip().rstrip()
    f.truncate(0)
    sys.stdout.write('[!] DECOMPILING CODE ENCRYPTION BY NINJA... DONE\n')
    anim_text('[!] SAVING DECODED CODE TO ' + o + '...')
    open(o, 'w').write(c)
    sleep(0.8)
    sys.stdout.write('[!] WRITING CODE TO ' + o + '... DONE\n')
    sleep(0.3)
    print('\x1b[?25h\n' + c + '\n')
    del(f, c, k, w, s, d, o, sys, sleep, ascii_lowercase, ascii_uppercase, StringIO, itertools, re)
