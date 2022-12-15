import random
import math
import time
from tictac import ticctacctoe
def flatten(r2d):
	n = []
	for j in r2d:
		for i in j:
			n.append(i)
	return n
possiblegame=[0]
def genval(game):
	if game.checkstate()!=-1:
		st=game.checkstate()
		if st==0:
			return 0
		return ((st-1)*2-1)*(game.turn*2-1)
	stv=-math.inf
	for i in game.genmov():
		game.move(i)
		possiblegame[0]+=1
		stv=max(-genval(game), stv)
		game.undo()
	#print(stv)
	return stv
def aimove(game):
	na={}
	if sum(flatten(game.board))==0:
		print("Random first move")
		return {random.choice(game.genmov()):0}
	if "11" in game.genmov():
		print("Bookmove")
		return {"11" : 0}
	for i in game.genmov():
		game.move(i)
		na[i]=genval(game)
		game.undo()
	return na

def choosemov(dic):
	mov=[]
	for i in range(-1,2):
		#print(i,mov)
		if mov!=[]:
			break
		for j in dic.keys():
			v=dic[j]
			if v == i:
				mov.append(j)
	print(mov)
	return random.choice(mov)
ticc=ticctacctoe()
ticc.printboard()
#print("perfect state",genval(ticc))
playx=input("Play as (x/o) : ")=="x"
if not playx:
	ev=aimove(ticc)
	print("Evaluated :", ev,f"\n{possiblegame[0]} position has been considered")
	botmov=choosemov(ev)
	possiblegame=[0]
	ticc.move(botmov)
	ticc.printboard()
	
while ticc.checkstate()==-1:
	
	#print(ticc.genmov())
	v=input("human > ")
	v = str(ord(v[0])-97)+str(int(v[1])-1)
	if v=="u":
		ticc.undo()
		ticc.printboard()
		continue
	if not v in ticc.genmov():
		print("Invalid move")
		continue
	ticc.move(v)
	
	ticc.printboard()
	#print print(ticc.checkstate())
	if ticc.checkstate()!=-1:
		break
	st=time.time()
	print("Thinking...", end="\r")
	ev=aimove(ticc)
	print("Evaluated :", ev,f"\n{possiblegame[0]} position has been considered")
	print("Took :",time.time()-st,"s")
	botmov=choosemov(ev)
	possiblegame=[0]
	ticc.move(botmov)
	ticc.printboard()
	print("Bot moved :",botmov)
	ticc.checkstate()
	print("-"*20)
print("Game ended")
st=ticc.checkstate()
if st == 0:
	print("Draw!")
elif st==1:
	print("x win!")
else:
	print("o win!")