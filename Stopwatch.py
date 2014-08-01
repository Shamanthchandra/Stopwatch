# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
x = 0
y = 0
stop = False
a = 0
b = 0
c = 0
d = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    global a,b,c,d
    d = counter % 10
    c = (counter % 100) / 10
    b = (counter / 100) % 6
    a = (counter / 600)
    return str(a)+':'+str(b)+str(c)+'.'+str(d)

def percentage():
    global x,y
    if y != 0:
        return 'Correctly stopped % is '+str(((float(x) /float(y))*100))+' %'
    else:
        return 'Game starts'
            
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startbut():
    global stop
    stop = False
    timer.start()
    
def stopbut():
    global stop,a,b,c,d
    if stop == False and not(a==0 and b==0 and c==0 and d==0):
        stop = True
        timer.stop()
        global x,y
        y+=1
        if counter % 10 == 0:
            x+=1
    
    
def resetbut():
    global counter,stop,x,y
    counter = 0
    timer.stop()
    stop = False
    x = 0
    y = 0
    
    

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter+=1

# define draw handler
def draw(canvas):
    global counter
    canvas.draw_text(str(format(counter)),[90,165],55,'white')
    canvas.draw_text((str(x)+ '/' +str(y)),[230,35],35,'white')
    canvas.draw_text(str(percentage()),[20,260],15,'black')
    
# create frame
frame = simplegui.create_frame('Stopwatch',300,300)
frame.set_canvas_background('Blue')
timer = simplegui.create_timer(100,tick)
startbutton = frame.add_button('Start',startbut,100)
stopbutton = frame.add_button('Stop',stopbut,100)
resetbutton = frame.add_button('Reset',resetbut,100)


# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()

# Please remember to review the grading rubric
