import sys
sys.path.append('C:\\Users\\Hall\\Desktop\\edcui\\')
sys.path.append('C:\\Users\\Hall\\Desktop\\edcui\\lib\\')

from commandButton import startProgram, stopProgram

import tkinter as tk
import serial.tools.list_ports
import serial
from tkinter import ttk

def return_data_bit(data_bit):
    if data_bit == '7 bit':
        return serial.SEVENBITS
    else:
        return serial.EIGHTBITS

def return_stop_bit(stopbits):
    if stopbits == '1 bit':
        return serial.STOPBITS_ONE
    else:
        return serial.STOPBITS_TWO

def return_parity(parity):
    if parity == 'None':
        return serial.PARITY_NONE
    elif parity == 'Odd':
        return serial.PARITY_ODD
    else:
        return serial.PARITY_EVEN

def process_kill():
    # stopProgram()
    window.destroy()

def process_run():
    argument = [
        selection_ports.get().split()[0],
        int(baunds_rate.get()),
        return_data_bit(data_bit.get()),
        return_stop_bit(stop_bit.get()),
        return_parity(parity.get())
    ]
    startProgram(argument)
    start_btn.grid_remove()
    ttk.Label(window, text = "Program is Running", 
                foreground ="black", 
                font = ("Times New Roman", 15)).grid(row = 0, column = 1)
    stop_btn = tk.Button(window, text = 'Stop',width=20,padx = 10, pady = 10,
                    command = process_kill)
    stop_btn.grid(column = 1, row = 12)

ports = list(serial.tools.list_ports.comports())
buandRate = ('50','75','110','134','150','200','300','600','1200','1800','2400','4800','9600','19200','28800','38400','57600','76800','115200')
dataBit = ('7 bit', '8 bit')
stopBit = ('1 bit', '2 bit')
parityBit = ('None', 'Odd', 'Even')

if __name__ == "__main__":
    window = tk.Tk()
    window.title('EDC Program')
    window.geometry('400x512')

    # Label
    ttk.Label(window, text = "Configuration", 
            foreground ="black", 
            font = ("Times New Roman", 15)).grid(row = 0, column = 1)
    ttk.Label(window, text = "Select Ports :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 5, padx = 10, pady = 25)
    ttk.Label(window, text = "Baunds Rate :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 6, padx = 10, pady = 25)
    ttk.Label(window, text = "Data Bit :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 7, padx = 10, pady = 25)
    ttk.Label(window, text = "Stop Bit :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 8, padx = 10, pady = 25)
    ttk.Label(window, text = "Parity :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 9, padx = 10, pady = 25)

    # String Var
    n_selection_ports = tk.StringVar()
    n_baunds_rate = tk.StringVar()
    n_data_bit = tk.StringVar()
    n_stop_bit = tk.StringVar()
    n_parity = tk.StringVar()

    # Combobox
    selection_ports = ttk.Combobox(window, width = 27, textvariable = n_selection_ports)
    baunds_rate = ttk.Combobox(window, width = 27, textvariable = n_baunds_rate)
    data_bit = ttk.Combobox(window, width = 27, textvariable = n_data_bit)
    stop_bit = ttk.Combobox(window, width = 27, textvariable = n_stop_bit)
    parity = ttk.Combobox(window, width = 27, textvariable = n_parity)

    # Value Selection
    selection_ports['values'] = ports
    baunds_rate['values'] = buandRate
    data_bit['values'] = dataBit
    stop_bit['values'] = stopBit
    parity['values'] = parityBit

    # Grid
    selection_ports.grid(column = 1, row = 5)
    baunds_rate.grid(column = 1, row = 6)
    data_bit.grid(column = 1, row = 7)
    stop_bit.grid(column = 1, row = 8)
    parity.grid(column = 1, row = 9)

    # Set Default Value
    selection_ports.current(len(ports)-1 if len(ports)-1 > 0 else 0)
    baunds_rate.current(12)
    data_bit.current(1)
    stop_bit.current(0)
    parity.current(0)

    # Button
    start_btn = tk.Button(window, text = 'Start',width=20,padx = 10, pady = 10,
                    command = process_run)
    start_btn.grid(column = 1, row = 10)
    ttk.Label(window, text = "").grid(column = 0,row = 11)

    # Windows
    window.mainloop()