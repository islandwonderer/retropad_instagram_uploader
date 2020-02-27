from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image as pImage
from PIL import ImageTk
from tkinter import messagebox
from instapy_cli import client
from tkinter.scrolledtext import ScrolledText

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Gui Initialization and Configuration
window = Tk()
window.title("Retropad Instagram Uploader")
# window.geometry("600x650")
window.configure(background="#121212")
lineStart = 4

# images setup
newImage = pImage.new('RGB', (976, 976))
screen = None
thumbnail = None

# Background image
background = 'Images/Gameboy_Background.png'

# Setup NewImage
bg = pImage.open(background)
newImage.paste(bg)


# Function to resize an image based on new width
def resize(img, width):
    w, h = img.size
    newW = width
    newH = int(newW * h / w)
    img = img.resize((newW, newH), pImage.ANTIALIAS)
    return img


# Open file function and dialogue
def open_file(field):
    global screen, thumbnail, profile
    filename = askopenfilename()
    if not filename.endswith('.png'):
        messagebox.showinfo("Visualizer error", "File type must be a .png")
    else:
        if field == "s":
            screen = pImage.open(filename)
            profile = screen.info.get("icc_profile", "")
        else:
            thumbnail = pImage.open(filename)
    return filename


# These opens the image and places the file path into the Tkinter form
def open_screen():
    file = open_file("s")
    ssEntry.delete(0, END)
    ssEntry.insert(0, file)
    return


def open_thumb():
    file = open_file("t")
    tmnEntry.delete(0, END)
    tmnEntry.insert(0, file)
    return


# Open file function and dialogue
def save_file():
    file2Save = asksaveasfilename(initialdir="/", title="Select file", filetypes={("PNG files", "*.png")})
    newImage.save(file2Save + ".png", "PNG", icc_profile=profile)


# This combines the image with the background
def compile_new_image():
    # If image has been added
    modded_image = newImage
    if screen:
        sc = resize(screen, 875)
        modded_image.paste(sc, (50, 155))

    # If image has been added
    if thumbnail:
        tmb = resize(thumbnail, 175)
        modded_image.paste(tmb, (100, 205))

    # Return image to save
    return modded_image


# This creates a preview of the combined images for display
def create_preview():
    preview_img = compile_new_image()
    print("image compiled")
    preview_img = resize(preview_img, int(newImage.width / 2))
    print("image resized")
    modified_preview = ImageTk.PhotoImage(preview_img)
    preview.configure(image=modified_preview)
    preview.image = modified_preview


# Sends an email to user with the information to post on Instagram
def post_instagram():
    username = "retrogamepadawan"
    password = "Pendejo4Eva!"
    cookie_file = username + "_ig.json"

    uploadImage = compile_new_image()

    caption = postEntry.get(1.0, END)
    hash_tags = "\n \n #retrogaming #gameboy #computerscience"
    text = caption + hash_tags
    file_name = "Images/upload.png"
    uploadImage.save(file_name, "PNG", icc_profile=profile)

    try:
        with client(username, password, cookie_file=cookie_file, write_cookie_file=True) as cli:
            print("Sending")
            cli.upload(file_name, text)
        messagebox.showinfo("Upload", "Your post is has been uploaded.", parent=window)
    except:
        messagebox.showinfo("Upload", "Your post failed to upload.", parent=window)


# Resize Image for Display
displayImg = resize(newImage, int(newImage.width/2))
tkImg = ImageTk.PhotoImage(displayImg)


# Gui Structure
Label(window, text="Screenshot:", bg="#121212", fg="white", font="none 12 bold") .grid(row=lineStart, column=1, sticky=W)
ssEntry = Entry(window, width=64, font="none 12 bold", highlightthickness=0)
ssEntry.grid(row=lineStart + 1, column=1, columnspan=3, sticky=W, padx=5)
ssOpen = Button(window, text="Open", command=open_screen, highlightbackground="#121212")
ssOpen.grid(row=lineStart+1, column=3, sticky=E, padx=5)
Label(window, text="Thumbnail:", bg="#121212", fg="white", font="none 12 bold") .grid(row=lineStart + 3, column=1, sticky=W)
tmnEntry = Entry(window, width=64, font="none 12 bold", highlightthickness=0)
tmnEntry.grid(row=lineStart + 4, column=1, columnspan=3, sticky=W, padx=5)
tmnOpen = Button(window, text="Open", command=open_thumb, highlightbackground="#121212")
tmnOpen.grid(row=lineStart+4, column=3, sticky=E, padx=5)
Label(window, text="Preview:", bg="#121212", fg="white", font="none 12 bold") .grid(row=lineStart+5, column=1, sticky=W)
preview = Label(window, image=tkImg, highlightthickness=0, bd=0)
preview.grid(row=lineStart+6, column=1, columnspan=3, padx=5, pady=5)
Label(window, text="Caption", bg="#121212", fg="white", font="none 12 bold") .grid(row=lineStart+7, column=1, sticky=W)
postEntry = ScrolledText(window, height=5, width=69, wrap='word', font="none 12 bold", highlightthickness=0)
postEntry.grid(row=lineStart + 8, column=1, columnspan=3, sticky=W, padx=10, pady=10)
saveBtn = Button(window, text="Save", command=save_file, highlightbackground="#121212")
saveBtn.grid(row=lineStart+9, column=3, sticky=E, padx=5, pady=5)
prevBtn = Button(window, text="Preview", command=lambda: create_preview(), highlightbackground="#121212")
prevBtn.grid(row=lineStart+9, column=1, sticky=W, padx=5, pady=5)
postBtn = Button(window, text="Post", command=lambda: post_instagram(), highlightbackground="#121212")
postBtn .grid(row=lineStart+9, column=2, sticky=E, padx=5, pady=5)

# Display screen
window.mainloop()
