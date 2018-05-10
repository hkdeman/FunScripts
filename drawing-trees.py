import turtle

# canvas = turtle.Turtle()

tree = list("(a(b(d(h,i),e),c(f,g)))")

tree_as_dict = {"a":[{"b":[{"d":["h","i"]},"e"]},{"c":["f",{"g":["j",{"k":["l"]}]}]}]}

# canvas.penup()
START_POS = (0,0)
# canvas.setposition(START_POS[0],START_POS[1])
last_pos = START_POS

level = 0
total_inner_nodes = 0

def get_inner_items(tree):
    global level
    global last_pos
    global total_inner_nodes
    for node in tree.keys():
        print("Node :"+node+" (Level : "+str(level)+")")
        for inner_node in tree[node]:
            if(type(inner_node) is dict):
                level+=1                               
                get_inner_items(inner_node)
            else:
                total_inner_nodes+=1
                print("Node :"+node+"---Innest Nodes : "+inner_node+"(Level :"+str(level+1)+")")
        level-=1

get_inner_items(tree_as_dict)
print(total_inner_nodes)
