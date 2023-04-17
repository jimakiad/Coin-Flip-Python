import random
import tkinter as tk
from PIL import Image, ImageTk
import winsound

# Load the images
heads_image = Image.open('heads_image.jpg')
tails_image = Image.open('tails_image.jpg')

# Define the pixel art size
pixel_art_size = (heads_image.width // 5, heads_image.height // 5)

# Define the palette size
palette_size = 8

# Define the counters for the coin flip results
heads_counter = 0
tails_counter = 0

# Define the function for flipping the coin
def flip_coin():
    global heads_counter, tails_counter
    result = random.choice(['heads', 'tails'])
    if result == 'heads':
        image1 = heads_image
        image2 = tails_image
        heads_counter += 1
    else:
        image1 = tails_image
        image2 = heads_image
        tails_counter += 1
    # Resize the images to pixel art size and convert them to a palette of 8 colors
    image1 = image1.resize(pixel_art_size, resample=Image.BILINEAR)
    image1 = image1.quantize(colors=palette_size, method=2)
    image2 = image2.resize(pixel_art_size, resample=Image.BILINEAR)
    image2 = image2.quantize(colors=palette_size, method=2)
    # Save the pixel art images
    image1.save('coin_flip_result1.png')
    image2.save('coin_flip_result2.png')
    winsound.PlaySound('flip_sound.wav', winsound.SND_ASYNC)
    flip_button.config(state='disabled')
    # Show the animation
    animate_coin_flip(image1, image2, 5, 500, lambda: update_counters(), lambda: show_result(result))

# Define the function for updating the result counters
def update_counters():
    global heads_counter, tails_counter
    heads_label.config(text=f"Heads: {heads_counter}")
    tails_label.config(text=f"Tails: {tails_counter}")

# Define the function for showing the final result
def show_result(result):
    if result == 'heads':
        image = heads_image
    else:
        image = tails_image
    # Resize the image to pixel art size and convert it to a palette of 8 colors
    image = image.resize(pixel_art_size, resample=Image.BILINEAR)
    image = image.quantize(colors=palette_size, method=2)
    # Save the pixel art image
    image.save('coin_flip_result.png')
    # Update the image on the canvas
    photo_image = ImageTk.PhotoImage(image)
    canvas.itemconfig(image_item, image=photo_image)
    canvas.image = photo_image
    flip_button.config(state='normal')

# Define the function for animating the coin flip
def animate_coin_flip(image1, image2, num_times, delay, callback1, callback2):
    for i in range(num_times):
        # Alternate between showing the two images
        if i % 2 == 0:
            image = image1
        else:
            image = image2
        # Resize the image to pixel art size and convert it to a palette of 8 colors
        image = image.resize(pixel_art_size, resample=Image.BILINEAR)
        image = image.quantize(colors=palette_size, method=2)
        # Update the image on the canvas
        photo_image = ImageTk.PhotoImage(image)
        canvas.itemconfig(image_item, image=photo_image)
        canvas.image = photo_image
        root.update()
        # Delay before showing the next image
        root.after(delay)
        # Call thecallback functions after the animation is complete
        callback1()
        callback2()

#Set up the GUI

root = tk.Tk()
root.title('Coin Flip')
root.resizable(False, False)
#Set up the canvas for displaying the images

canvas = tk.Canvas(root, width=250, height=pixel_art_size[1])
canvas.pack()
#Load the initial image onto the canvas

initial_image = ImageTk.PhotoImage(heads_image.resize(pixel_art_size, resample=Image.BILINEAR).quantize(colors=palette_size, method=2))
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=initial_image)
canvas.image = initial_image
#Set up the labels for displaying the result counters

heads_label = tk.Label(root, text=f"Heads: {heads_counter}")
heads_label.pack(side=tk.LEFT, padx=10)
tails_label = tk.Label(root, text=f"Tails: {tails_counter}")
tails_label.pack(side=tk.RIGHT, padx=10)
#Set up the button for flipping the coin

flip_button = tk.Button(root, text="Flip", command=flip_coin)
flip_button.pack(pady=10)
#Start the GUI event loop

root.mainloop()






