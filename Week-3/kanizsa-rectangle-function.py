import expyriment
from expyriment import design, control, stimuli, misc

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "kanizsa-square", background_colour= misc.constants.C_GREY)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
screenW, screenH = exp.screen.size
square_size= int(screenW*0.25)
circle_r=int(screenW*0.05)
half= square_size / 2

pos1 = (-half, half) #tl
pos2 = (half, half) #tr
pos3 = (-half, -half) #bl
pos4 = (half, -half) #br


# Create a 50px-radius circle
square = stimuli.Rectangle(size=(square_size,square_size), colour=misc.constants.C_GREY, position=(0,0))

C1 = stimuli.Circle(radius=(circle_r), colour='black', position=(pos1))
C2 = stimuli.Circle(radius=(circle_r), colour='black', position=(pos2))
C3 = stimuli.Circle(radius=(circle_r), colour='white', position=(pos3))
C4 = stimuli.Circle(radius=(circle_r), colour='white', position=(pos4))

bg_screen= stimuli.BlankScreen()
C1.plot(bg_screen)
C2.plot(bg_screen)
C3.plot(bg_screen)
C4.plot(bg_screen)
square.plot(bg_screen)

control.start(subject_id=1)
bg_screen.present()
exp.keyboard.wait()
control.end()
