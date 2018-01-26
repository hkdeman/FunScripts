import turtle
import random
import io
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
from fpdf import FPDF

SPACE = 10
RADIUS = 10
FONT_SIZE = 12
FONT = ("Arial", FONT_SIZE, "normal")
TITLE_FONT_SIZE = 20
TITLE_FONT = ("Arial",TITLE_FONT_SIZE,"normal")
COLORS  = ["red","green","blue","orange","purple","pink","yellow"]
ARROW_LENGTH = 3
graph = {}
canvas = turtle.Turtle()
nodes_labels = [i+1 for i in range(18)]
canvas.getscreen().setworldcoordinates(-300,-600,350,100)
canvas.speed(11)

def tuplize(connection):
	new_connection_tuples = []
	for i in range(1,len(connection)):
		new_connection_tuples.append((connection[i-1],connection[i]))
	return new_connection_tuples

def create_a_line_between_nodes(node1,node2):
	global canvas
	global graph
	if(canvas.isdown()):
		canvas.penup()
	
	node1x,node1y = graph[node1][0],graph[node1][1]
	node2x,node2y = graph[node2][0],graph[node2][1]+RADIUS*2
	canvas.setposition(node1x,node1y)
	canvas.pendown()
	canvas.setposition((node2x+node1x)/2,(node2y+node1y)/2)
	canvas.begin_fill()
	canvas.setposition((node2x+node1x)/2 + ARROW_LENGTH, (node2y+node1y)/2 + ARROW_LENGTH)
	canvas.setposition((node2x+node1x)/2 - ARROW_LENGTH, (node2y+node1y)/2 + ARROW_LENGTH)
	canvas.setposition((node2x+node1x)/2,(node2y+node1y)/2)
	canvas.end_fill()
	canvas.setposition(node2x,node2y)



def create_an_arc_between_nodes(node1,node2,direction="RIGHT"):
	global graph
	if(direction=="LEFT"):
		node1x,node1y = graph[node1][0]-RADIUS,graph[node1][1]+RADIUS
		node2x,node2y = graph[node2][0]-RADIUS,graph[node2][1]+RADIUS
	else:
		node1x,node1y = graph[node1][0]+RADIUS,graph[node1][1]+RADIUS
		node2x,node2y = graph[node2][0]+RADIUS,graph[node2][1]+RADIUS
	
	going_down= True
	if(node2y>node1y):
		going_down=False

	create_an_arc((node1x,node1y),(node2x,node2y),going_down,direction)
	
def create_an_arc(pos1,pos2,going_down,direction="RIGHT"):
	global canvas
	radius = abs(pos2[1]-pos1[1])/2
	direct = 1
	rad_direct = -1

	if(not going_down):
		rad_direct=1

	if(direction=="LEFT"):
		direct=-1
	
	if(canvas.isdown()):
		canvas.penup()

	canvas.setposition(pos1[0],pos1[1])
	canvas.pendown()
	canvas.circle(rad_direct*radius,direct*90)
	x,y = canvas.pos()
	canvas.begin_fill()
	if going_down:
		canvas.setposition(x+ARROW_LENGTH,y+ARROW_LENGTH)
		canvas.setposition(x-ARROW_LENGTH,y+ARROW_LENGTH)
	else:
		canvas.setposition(x+ARROW_LENGTH,y-ARROW_LENGTH)
		canvas.penup()
		canvas.setposition(x-ARROW_LENGTH,y-ARROW_LENGTH)

	canvas.pendown()
	canvas.setposition(x,y)
	canvas.end_fill()
	canvas.circle(rad_direct*radius,direct*90)
	canvas.setheading(0)


def create_nodes(nodes):
	global graph
	global canvas
	y_pos = 0
	min_y=nodes*30*-1
	node_created=1
	while(y_pos>min_y):
		if(not canvas.isdown()):
			canvas.pendown()
		canvas.circle(RADIUS)
		graph[node_created]=(0,y_pos)
		canvas.penup()
		canvas.setposition(0, y_pos)
		canvas.write(nodes_labels[node_created-1], align="center", font=FONT)
		y_pos -= RADIUS*2 + SPACE
		canvas.setposition(0,y_pos)
		node_created+=1
	

def create_connections(nodes_together):
	global canvas
	for connection in nodes_together:
		for node1,node2 in tuplize(connection):
			color = random.choice(COLORS)
			canvas.color(color)
			if(node2-node1==1):
				create_a_line_between_nodes(node1,node2)
			elif(node2-node1==2):
				create_an_arc_between_nodes(node1,node2)
			else:
				create_an_arc_between_nodes(node1,node2,"LEFT")

def create_title(title):
	global canvas
	canvas.penup()
	canvas.setposition(0,50)
	canvas.pendown()
	canvas.write(title,align="center",font=TITLE_FONT)
	canvas.penup()
	canvas.setposition(0,0)

def make_pdf():
	pdf = FPDF()
	images = [f for f in listdir("graphs") if isfile(join("graphs", f))]
	for image in images:
		pdf.add_page()
		pdf.image("graphs/"+image)
	pdf.output("graphs.pdf", "F")	

def read_the_file():
	with open("CircleOOSEData.txt","r") as f:
		lines = f.readlines()
		n_graph = 1
		if not os.path.exists("graphs"):
		    os.makedirs("graphs")

		for i in range(0,len(lines),2):
			create_title("Graph "+str(n_graph))
			create_nodes(int(lines[i]))
			node_connections = [[int(elem) for elem in node.split(",")] for node in lines[i+1].split(";")]
			create_connections(node_connections)			
			ps = canvas.getscreen().getcanvas().postscript(colormode="color")
			im = Image.open(io.BytesIO(ps.encode('utf-8')))
			im.save(os.path.abspath("graphs/Graph"+str(n_graph)+".png"))
			canvas.getscreen().clear()
			n_graph+=1
	make_pdf()
	canvas.getscreen().bye()


if __name__== "__main__":
	read_the_file()


