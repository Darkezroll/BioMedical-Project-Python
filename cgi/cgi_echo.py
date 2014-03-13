#!/usr/bin/env python

import cgi
import cgitb
import os

cgitb.enable()
args = cgi.FieldStorage()

def respond():

    

    print("Content-Type: text/html")
    print()
    print("<html>\n<head>")
    print("<style> ss{text-shadow: 3px 3px 3px #707070;} </style>")
    print("<title>Bio-Medical Project Present</title>")
    print("</head>")
    print("<script>function goBack(){window.history.back()}</script>")
    print("<body background = 'images/frame.png' BGCOLOR = #00CCFF ><center>")


    args = cgi.FieldStorage()
    filename = args.getfirst('upload')
    fn = filename
    fh1=open(fn,'r')

    dna = fh1.readlines()

    a = dna[0]
    b = dna[1]
    mutation = 0

    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    ratio = {True: 0.0, False: 0.0}

    for i in zip(a,b):

        if i[0] != i[1] :

            mutation = mutation + 1
            ratio[i in transitions] += 1

    print('</br></br></br></br></br></br></br>')
    print('<p><ss><strong><font color=#FFF face="Trebuchet MS" size="30" >PROCESS OUT..</font></strong></ss></p>')
    print('<p><ss><font color=#FFF face="Trebuchet MS" size=4" >Counting Point Mutations :', mutation, '</font></ss></p>')
    print('<p><ss><font color=#FFF face="Trebuchet MS" size=4" >Transition :', ratio[True], '</font></ss></p>')
    print('<p><ss><font color=#FFF face="Trebuchet MS" size=4" >Transversion :', ratio[False], '</font></ss></p>')
    print('<p><ss><font color=#FFF face="Trebuchet MS" size=4" >Transition/Transversion Ratio :', ratio[True] / ratio[False], '</font></ss></p></br></br></br></br>')
    print('<ss><button onclick="goBack()">Home</button></ss>')
    print("</center>\n</body>\n</html>")

if __name__ == '__main__':
	respond()
    
    

