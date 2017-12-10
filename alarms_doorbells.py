# Several Events in Everyday Life

import tkinter
import time

# Handler for timer event
def alarm():
	print('Calling the Pizza Company.')

# Handler for ringing the doorbell
def doorbell():
	print('Ding Dong!')
	time.sleep(4) # Will wait for 4 seconds before printing 'Opening the Door.'
	print('Opening the Door.')

# Handler for when the phone rings
def phonecall():
	print('Answering the phone.')

# Create buttons and assign callbacks
root = tkinter.Tk()
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call Phone', command=phonecall).pack()

# Set a timer for 4 seconds
root.after(4000, alarm)

# Start the event loop
root.mainloop()


