from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.askyesno('Check Point', 'Are you ready for the next step?', icon='error')

window.deiconify()
window.destroy
window.quit()