import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a 50px-radius circle
square_1 = stimuli.Rectangle(size=(50,50), colour=('red'), position=(-400,0)) 
                            
square_2 = stimuli.Rectangle(size=(50,50), colour=('green'))

# Start running the experiment
control.start(subject_id=1)

#Position initiale

#Déplacement

while square_1.position[0] < -50 :
    square_1.move ((5,0))
    square_1.present (update=False)
    square_2.present (clear=False)

distance = 400 
frames = int(distance/5)

for n in range(frames):
    square_2.move((5,0))
    square_1.present (update=False)
    square_2.present (clear=False)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()