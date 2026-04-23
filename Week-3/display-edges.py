import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Display Edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
screenW, screenH = exp.screen.size
square_size= int(screenW*0.05)
half= square_size / 2

pos1 = (-screenW /2 + half, screenH /2 - half) #tl
pos2 = (screenW /2 - half, screenH /2 - half) #tr
pos3 = (-screenW /2 + half, -screenH /2 + half) #bl
pos4 = (screenW /2 - half, -screenH /2 + half) #br


# Create a 50px-radius circle
square1 = stimuli.Rectangle(size=(square_size,square_size), colour=('red'), line_width=1, position=(pos1))
square2 = stimuli.Rectangle(size=(square_size,square_size), colour=('red'), line_width=1, position=(pos2))
square3 = stimuli.Rectangle(size=(square_size,square_size), colour=('red'), line_width=1, position=(pos3))
square4 = stimuli.Rectangle(size=(square_size,square_size), colour=('red'), line_width=1, position=(pos4))

square1.present (clear=True, update=False)
square2.present (clear=False, update=False)
square3.present (clear=False, update=False)
square4.present (clear=False, update=True)

square1.present (clear=True, update=False)
square2.present (clear=False, update=False)
square3.present (clear=False, update=False)
square4.present (clear=False, update=True)

exp.keyboard.wait()

