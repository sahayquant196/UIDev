from Layout.EQLayout import *
from Layout.IRLayout import *
from Layout.FXLayout import *


root = Tk()
root.title('DVC Pricer')
root.geometry('400x400')


def run_application():
    #global image_logo
    Label_Info = Label(root,
                       text='Welcome to DVC Pricer!',
                       font=('Arial', 9))
    Label_Info.grid(row=0,column=3)

    Label_Info_Next = Label(root,text='Please click the asset class button to get started!')
    Label_Info_Next.grid(row=1,column=3)
    button_eq = Button(root, text='Equity', command= lambda: openEQWindow(root,screenshot))
    button_eq.grid(row=2,column=3)
    button_ir = Button(root, text='IR', command= lambda: openIRWindow(root))
    button_ir.grid(row=3,column=3)
    button_fx = Button(root, text='FX', command= lambda: openFXWindow(root))
    button_fx.grid(row=4,column=3)
    '''IMAGE FUNCTIONS'''
    #image_logo = Image.open('ey_logo.png')
    #image_logo = ImageTk.PhotoImage(file='ey_logo.png')
    #canvas_logo = Canvas(root)
    #canvas_logo.grid(row=5,column=4)
    #canvas_logo.create_image(5,4,image=image_logo)




    # Tkinter event loop


def screenshot():
    now = dt.datetime.now()
    datetime_string = now.strftime('%Y-%m-%d-%H-%M-%S')+'_DVC_SS'
    login_string = str(os.getlogin())
    filename = 'C:/Users/'+login_string+'/Documents/'+datetime_string+'.jpg'
    print(filename)
    ss = pg.screenshot(filename)
    #ss.show() to display the screenshot (which is not required)






