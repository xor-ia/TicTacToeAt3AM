def flatten(r2d):
	n = []
	for j in r2d:
		for i in j:
			n.append(i)
	return n
class ticctacctoe:
	def __init__(self):
		self.board=[[0,0,0],[0,0,0],[0,0,0]]
		self.lastestmove=[]
		self.turn=0
		self.state=-1
		#-1 = on going
		#0  = drawn
		#1  = x win
		#2  = o win
		#move = 000->122
	def update(self):
		self.board=[[0,0,0],[0,0,0],[0,0,0]] 
		for i in self.lastestmove:
			#print(i)
			turn=int(i[0])
			in1=int(i[1])
			in2=int(i[2])
			self.board[in1][in2]=turn+1
		
		self.checkstate()
	def move(self, chr):
		chr=str(self.turn)+chr
		if not self.isvalid(chr):
			return None
		self.lastestmove.append(chr)
		if self.turn==0:
			self.turn=1
		else:
			self.turn=0
		self.update()
		return True
	def undo(self):
		self.lastestmove.pop()
		self.turn=int(not bool(self.turn))
		self.update()
	def isovr(self):
		board1d=flatten(self.board)
		if not (0 in board1d):
			self.state=0
			return True
		return False
	def checkstate(self):
		
		if self.board[0][0]!=0 and self.board[0][0]==self.board[2][2] and self.board[0][0]==self.board[1][1]:
				self.state=self.board[0][0]
				return self.board[0][0]
		if self.board[0][2]!=0 and self.board[0][2]==self.board[2][0] and self.board[0][2]==self.board[1][1]:
				self.state=self.board[0][2]
				return self.board[0][2] 
		
		buffer=[]
		board1d=flatten(self.board)
		for i in range(3):
			if board1d[i]!=0 and board1d[i]==board1d[i+3] and board1d[i+3]==board1d[i+6]:
				self.state=board1d[i]
				return board1d[i]
		for i in board1d:
			buffer.append(i)
			if len(buffer)==3:
				if buffer==[1,1,1]:
					self.state=1
					return 1
				if buffer==[2,2,2]:
					self.state=2
					return 2
				buffer=[]
		if self.isovr():
			return 0
		return -1
		
	def isvalid(self, nxmov):
		if int(nxmov[0]) != self.turn:
			return False
		in1=int(nxmov[1])
		in2=int(nxmov[2])
				
		if self.board[in1][in2] != 0 or (in1>2 or in2>2 or in1<0 or in2<0):
			return False
		return True 
	def genmov(self):
		lmov=[]
		for i in range(len(self.board)):
			v=self.board[i]
			for j in range(len(v)):
				k=v[j]
				if k==0:
					lmov.append(str(i)+str(j))
		return lmov
	def printboard(self):
		print(" |1|2|3|")
		ind = 0
		for i in self.board:
			print(chr(97+ind),end="|")
			for k in i:
				if k==0:
					print(end=" ")
				elif k==1:
					print(end="x")
				else:
					print(end="o")
				print(end="|")
			print()
			ind+=1