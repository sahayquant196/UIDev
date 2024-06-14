from tkinter import *
from tkinter.ttk import *
from Pricing.EQPricer import *


'''
THESE FUNCTIONS DEFINES THE LAYOUT OF THE EQUITY PRICER
'''



def openEQWindow(root,screenshot):
    EQWindow = Toplevel(root)
    EQWindow.title('Equity Pricer')

    #All variables declared here
    var_product = StringVar()
    var_model = StringVar()
    var_rate = StringVar()
    var_vol = StringVar()
    var_spot = StringVar()
    var_strike = StringVar()
    var_valdate = StringVar()
    var_detdate = StringVar()

    #EQWindow.geometry('400x400')
    frame_selection = LabelFrame(EQWindow,text='Product Selection')
    frame_selection.grid(row=0,column=0)
    frame_model = LabelFrame(EQWindow,text='Model Selection')
    frame_model.grid(row=1,column=0)
    frame_valdate = Label(EQWindow,text='Valuation Date')
    frame_valdate.grid(row=0,column=1)
    input_valdate = Entry(EQWindow,textvariable=var_valdate)
    input_valdate.insert(END,'1/1/2000')
    input_valdate.grid(row=0,column=2)
    frame_detdate = Label(EQWindow,text='Determination Date')
    frame_detdate.grid(row=1,column=1)
    input_detdate = Text(frame_detdate,height=1,width=10,bg='light yellow')
    input_detdate = Entry(EQWindow,textvariable=var_detdate)
    input_detdate.insert(END,'1/1/2100')
    input_detdate.grid(row=1,column=2)
    #frame_pricebutton = LabelFrame(EQWindow)
    #frame_pricebutton.grid(row=40,column=40)


    #frame_rate.grid(row=0,column=2)

    #input_rate.pack(side='top')
    frame_vol = Label(EQWindow,text='Vol(%)')
    frame_vol.grid(row=0,column=3)
    input_vol = Entry(EQWindow,textvariable=var_vol)
    input_vol.insert(END,'20')
    input_vol.grid(row=0,column=4)
    frame_rate = Label(EQWindow,text='Rate(%)')
    frame_rate.grid(row=1,column=3)
    input_rate = Entry(EQWindow,textvariable=var_rate)
    input_rate.insert(END,'1')
    input_rate.grid(row=1,column=4)

    frame_spot = Label(EQWindow,text='Spot')
    frame_spot.grid(row=0,column=5)
    frame_strike = Label(EQWindow,text='Strike')
    frame_strike.grid(row=1,column=5)
    input_spot = Entry(EQWindow,textvariable=var_spot)
    input_spot.insert(END,'100')
    input_strike=Entry(EQWindow,textvariable=var_strike)
    input_strike.insert(END,'110')
    input_spot.grid(row=0,column=6)
    input_strike.grid(row=1,column=6)



    EQ_Products = ('Vanilla Call', 'Vanilla Put', 'Digital Call', 'Digital Put')
    Models = ('BSM', 'Local Vol', 'StoVol')

    combo_product = Combobox(frame_selection,textvariable=var_product)
    combo_product['values'] = EQ_Products
    combo_product['state'] = 'readonly'
    combo_product.pack(side='top')

    combo_model = Combobox(frame_model,textvariable=var_model)
    combo_model['values'] = Models
    combo_model['state'] = 'readonly'
    combo_model.pack(side='top')


    #frame_ss = LabelFrame(EQWindow)
    #frame_ss.grid(row=50,column=40)

    params_list = [var_spot,var_strike,var_valdate,var_detdate,var_vol,var_rate]

    btn_ss = Button(EQWindow, text='Take Screenshot', command=screenshot)
    btn_ss.grid(row=10,column=10)
    btn_price = Button(EQWindow, text='Price', command=lambda: print_price(EQWindow,params_list))
    btn_price.grid(row=9,column=10)

def print_price(window,params_list):


    pricing_params = {'spot': str(params_list[0].get()), 'strike': str(params_list[1].get()),
                      'valdate': str(params_list[2].get()),
                      'detdate': str(params_list[3].get()),
                      'vol': str(params_list[4].get()),
                      'rate': str(params_list[5].get())}
    ret_price = get_price(pricing_params)

    Label_PriceText = Label(window,text='Price',font=('Arial',9))
    Label_Price = Label(window,text=str(ret_price),font=('Arial',9))
    Label_PriceText.grid(row=9,column=1)
    Label_Price.grid(row=9,column=2)




