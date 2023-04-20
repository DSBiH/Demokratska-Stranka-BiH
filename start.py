import os

# create directories
os.makedirs("img")
os.makedirs("js")
os.makedirs("css")

# create files
with open("index.html", "w") as f:
    f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>My Website</title>\n<link rel='stylesheet' href='css/style.css'>\n<script src='js/index.js'></script>\n</head>\n<body>\n<h1>Welcome to my website!</h1>\n<img src='img/myimage.jpg' alt='My Image'>\n</body>\n</html>")

with open("css/style.css", "w") as f:
    f.write("/* Add your CSS styles here */")

with open("js/index.js", "w") as f:
    f.write("// Add your JavaScript code here")
    
print("Folders and files created successfully!")
