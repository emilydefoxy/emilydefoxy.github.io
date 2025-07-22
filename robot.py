import time
import ascii_magic
from ascii_magic import AsciiArt

# Create an AsciiArt object from the image file
my_art = AsciiArt.from_image('./brandonAndMe.jpg')

# Generate the ASCII art for the terminal
text = my_art.to_terminal(columns=80)

# Print the ASCII art line by line
lines = text.split('\n')
unique_lines = []

for line in lines:
    if line not in unique_lines:
        unique_lines.append(line)

for line in unique_lines:
    print(line)
