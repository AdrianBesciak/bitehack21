import PySimpleGUI as sg

w=None

def init():
	layout = [
		[sg.Text("Please put your guest card on the reader",
				 key="message",
				 font=("Comic", 30),
				 text_color='#EBF2FA',
				 background_color='#064789',
				 justification='center', size = (20,16))
		 ]]
	global w
	w = sg.Window("No title", layout, no_titlebar=True, location=(0,0), size=(480,800), background_color='#064789')

	w.read(timeout=10)

def message(message):
	if w is not None:
		w['message'].update(message)
		w.read(timeout=10)
	else:
		print("window does not exist")
	