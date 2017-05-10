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

# Convert the .svg to .ps to .dxf to .scad

print ("Converting Files...")
for file in glob.glob("*.svg"):
	print ("Converting File "+file[0:2])
	fileheight = int(file[0:2]) * -10
	filedes = file.replace(".svg", ".ps").replace(" ", "\ ")
	filesrc = file.replace(" ", "\ ")
	os.system("inkscape -P "+des+"/"+filedes+" "+des+"/"+filesrc)
	os.system("pstoedit -dt -f dxf:-polyaslines\ -mm "+des+"/"+filedes+" "+des+"/"+filedes.replace(".ps", ".dxf")+" 2> /dev/null")
	scad = open(des+"/"+file.replace(".svg", ".scad"),"w")
	scad.write("translate([0,0,"+str(fileheight)+"])")
	scad.write("\nlinear_extrude(height = 10)")
	scad.write("\nimport(\""+des+"/"+file.replace(".svg", ".dxf")+"\");")
	scad.close()
print ("Done!")
	
	# Create a .scad file with proper lift off the ground
	
	# Export the .scad file into an .stl
# Run a python script to combine all the .stls into one .amf