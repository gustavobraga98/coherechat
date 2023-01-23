from tkinter import *
from backend import *
# f9db7zxVAPz6ISFEUjqMydTXdg2AqzDCAQ6ojfyR
# txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
LOGINSUCESS = False

while LOGINSUCESS == False:
    LOGINSUCESS,co,SESSIONID = ask_key()


# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



# Send function
def send():
	send = "You -> " + e.get("1.0",'end-1c')
	txt.insert(END, "\n" + send)
	user = e.get("1.0",'end-1c')
	response = co.chat(user,session_id=SESSIONID)
	txt.insert(END, "\n" + f"COHERE -> {response.reply}")
	e.delete("1.0","end")



lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="COHERE CHAT", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt,orient='vertical')
scrollbar.place(relheight=1, relx=1)

e = Text(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55,height = 10)
#e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()



