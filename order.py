import pexpect 
import re

def testjulius():	
    child= pexpect.spawn ('julius -input mic -C Sample.jconf')
    child.maxread=8000
    i=0
    pexpect.run("play pizza_order.wav", cwd="/home/ishank/work/htk/dhindi") # wav file containing prompt for pizza order
    while True:
		try:
			if i==0:
				child.expect("please speak")
				pass1=findsentence(child.before)
				if pass1 != None:
					pizza=pass1
					print "Your pizza order is:", pass1
					i=i+1
					pexpect.run("play side_order.wav", cwd="/home/ishank/work/htk/dhindi") # wav file containing containing prompt for side order	
				else:
					pass			
			if i == 1:
				child.expect("please speak")
				pass2=findsentence(child.before)
				if pass2 != None:
					side=pass2
					print "Your side order is:", side
					i=i+1
				else:
					pass
			if i==2:
				print "Your order is: ",pizza," & ",side
				return 0
			else:
				pass			
		except KeyboardInterrupt:
			child.close()
			pass
  	    

def findsentence(text):
    match = re.match(r'(.*?)sentence1(\.*)',text,re.S)
    if match:
		pizza=score_ord(text)
		if pizza != None:
		    return pizza		 	    
    else:
		    print "No match"
		    pass
		
 	    
def score_ord(text):
	i=0
	if checkscore(text,i)[0] == 1:
		return checkscore(text,i)[1]  ##(1,name)
	else:
		print "Please speak again"	


	

def checkscore(text,i):
    tsplit=text.split("\n")
    for w in tsplit:
		if w.find("sentence1") != -1 :
			sentence1 = w
		elif w.find("cmscore1") != -1:
		    cmscore = w	
		elif w.find("score1") != -1 :
			 score1 = w	
    flag= False
    cm=cmscore.split()
    for score in cm[1:]:
	    score= float(score)
	    if score < 0.996 :
		    print "Confidence score is less for",sentence1
		    flag=True
		    
    score1=float(score1.split()[1])
    if score1 < -6600:
	    print "Viterbi score:",score1," is less for",sentence1
	    flag=True
	    	    
    if not(flag):
		print "Recognized"	
		return i+1,storeorder(sentence1)
				     
    else:
		return i,"error"  
    
    
def storeorder(text):
	text=str(text)
	start=text.find("> ")
	end=text.find("</")
	urorder=text[start+2:end-1]
	return urorder

  
def start_order():
		testjulius()
		
			
	
start_order()

	
	
		 
	   	







