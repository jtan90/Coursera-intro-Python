# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
total_stop = 0
Stop_stop = 0
is_running = False 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = t % 600 // 100
    C = t % 100 // 10  
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 

# define helper function score that returns current score
def score():
    return str(Stop_stop) + "/" + str(total_stop)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running
    timer.start()
    is_running = True
    
def stop():
    global is_running, total_stop, Stop_stop
    if is_running:
        total_stop += 1
        if counter % 10 == 0:
            Stop_stop += 1
    is_running = False     
           
    
def reset():
    global is_running, total_stop, Stop_stop, counter
    timer.stop()
    is_running = False
    counter = 0
    Stop_stop = 0
    total_stop = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [60, 85], 36, "White")
    canvas.draw_text(score(), [155, 25], 26, "Green")
    
# create frame
frame = simplegui.create_frame("Timer", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start,100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
#timer.start()

# Please remember to review the grading rubric
