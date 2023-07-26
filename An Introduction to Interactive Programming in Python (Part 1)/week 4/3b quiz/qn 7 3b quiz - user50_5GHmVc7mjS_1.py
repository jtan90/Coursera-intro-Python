import simplegui

# global state
iteration = 0
current = 217

# helper functions
def init(current):
    """Initializes  n"""
    print "Input is" , current
    
def sequence(current):
    """Sequence generation rule."""
    if current % 2 == 0:
        return current / 2
    else:
        return current * 3 + 1   
    
# timer callback
def update():
    global iteration, current
    iteration =+ 1
    
    # Stop iterating if sequence becomes 1
    
    if current == 1:
        timer.stop()
        print "Last output is", current
    else:
        current = sequence(current)
        print current
        
# register event handlers
timer = simplegui.create_timer(1, update)        

# start
init(current)
timer.start()
        
    


    