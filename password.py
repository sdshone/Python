import sys
passwords={
            'gmail':'1234',
            'facebook':'4321',
            'instagram':'5678',
            'quora':'8765',
}
if len(sys.argv) <2:
    print ('Usage password.py [account] -shows password')
    sys.exit()
account=sys.argv[1]

if account in passwords:
    print passwords[account]
else:
    print "No such account"
