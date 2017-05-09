# CreateCuraModel
# Created by Andrew and Marko Ritachka on 5/6/17.
import sys
import os
import glob

# Uncompress it

print ("Uncompressing Tar...")
des = os.getcwd().replace(" ", "\ ")
tar = sys.argv[1].replace(" ", "\ ")
os.system("tar -xf "+tar+" -C "+des)
print ("Done!")

# Convert the .svg to an .eps to .dxf

print ("Converting Files...")
for file in glob.glob("*.svg"):
	print ("Converting File "+file[0:2])
	filedes = file.replace(".svg", ".eps").replace(" ", "\ ")
	filesrc = file.replace(" ", "\ ")
	os.system("inkscape -E "+des+"/"+filedes+" "+des+"/"+filesrc)
	os.system("pstoedit -dt -f dxf:-polyaslines\ -mm "+des+"/"+filedes+" "+des+"/"+filedes.replace(".eps", ".dxf")+" 2> /dev/null")
print ("Done!")
	
	
	# Create a .scad file with proper lift off the ground
	# Export the .scad file into an .stl
# Run a python script to combine all the .stls into one .amf