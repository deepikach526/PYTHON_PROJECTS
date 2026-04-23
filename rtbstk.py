from tkinter import *
from tkinter import messagebox

trains={
    "101":{"name":"Express","fare":150,"seats":50},
    "102":{"name":"Super Fast","fare":200,"seats":40},
    "103":{"name":"Passenger","fare":100,"seats":60}    
}

booked_ticket=None
booked_seats=0

def view_trains():
    text.delete(1.0,END)
    text.insert(END,"Available trains:\n\n")
    for train_no,details in trains.items():
        text.insert(
            END,
            f"Train no:{train_no}\n"
            f"Name:{details["name"]}\n"
            f"Fare:{details["fare"]} Rs/-\n\n"
            f"Available seats:{details["seats"]}\n"
        )
    

def book_ticket():
    global booked_ticket,booked_seats
    train_no=entry_train.get()
    seats_required=int(entry_seats.get())  
    available_seats=trains[train_no]["seats"]-seats_required
    
    if train_no not in trains:
        messagebox.showerror("Error","Invalid train number")
        return
    
    if seats_required <= available_seats:
        trains[train_no]["seats"] -= seats_required
        booked_ticket=train_no
        booked_seats=seats_required
        total_fare=seats_required*trains[train_no]["fare"]
        messagebox.showinfo("Success",f"{seats_required} seat(s) booked\n"f"Total fare:{total_fare} Rs/-")
    else:
        messagebox.showwarning("Full","not enough seats available")


def calculate_fare():
    train_no=entry_train.get()
    seats_required=entry_seats.get()

    if train_no not in trains:
        messagebox.showerror("Error","Invalid train number")
        return
    if not seats_required.isdigit():
        messagebox.showerror("Error","Enter valid number of seats")
        return
    seats_required = int(seats_required)
    fare=trains[train_no]["fare"]
    total_fare=seats_required*fare
    messagebox.showinfo("Fare details",f"Total fare:{total_fare} Rs/-")
    
def cancel_ticket():
    global booked_ticket,booked_seats
    if booked_ticket:
        trains[booked_ticket]["seats"]+=booked_seats
        messagebox.showinfo("Cancelled","Ticket Cancelled Successfully")
        booked_ticket=None
        booked_seats=0
    else:
        messagebox.showerror("Warning","No Ticket Found")

def exit_app():
    root.destroy()





root=Tk()
root.title( "Railway Ticket Booking System")
root.geometry("520x520")

Label(root,text="Railway Ticket Booking System",font=("Arial",16,"bold")).pack(pady=10)

Label(root,text="Enter train number:").pack()
entry_train=Entry(root)
entry_train.pack(pady=5)

Label(root,text="Enter number of seats:").pack()
entry_seats=Entry(root)
entry_seats.pack(pady=5)


button_frame=Frame(root)
button_frame.pack(pady=10)

btn_view=Button(button_frame,text="View Trains",width=20,command=view_trains)
btn_view.pack(pady=3)
btn_book=Button(button_frame,text="Book Ticket",width=20,command=book_ticket)
btn_book.pack(pady=3)
btn_fare=Button(button_frame,text="Calculate Fare",width=20,command=cancel_ticket)
btn_fare.pack(pady=3)
btn_cancel=Button(button_frame,text="Cancel Ticket",width=20,command=cancel_ticket)
btn_cancel.pack(pady=3)
btn_exit=Button(button_frame,text="Exit",width=20,command=exit_app)
btn_exit.pack(pady=3)


text=Text(root,height=12,width=60)
text.pack(pady=10)

root.mainloop()