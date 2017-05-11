# CreateCuraModel
# Created by Andrew and Marko Ritachka on 5/6/17.
import sys
import os
import glob

# Uncompress it

print ("Uncompressing Tar...")
des = os.getcwd().replace(" ", "\ ")
tar = sys.argv[1]
os.system("tar -xf "+tar+" -C "+des)
print ("Done!")
# Convert the .svg to .ps to .dxf to .scad to .stl

print ("Converting Files...")
for file in glob.glob("*.svg"):
	print ("	Converting File "+file[0:2])
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
	os.system("openscad -o "+des+"/"+file.replace(".svg", ".stl").replace(" ", "\ ")+" " +des+"/"+file.replace(".svg", ".scad").replace(" ", "\ "))
print ("Done!")
lista = []
for file in glob.glob("*.stl"):
	lista.append(file)
mgfile = des+"/"+lista[0].replace(" ", "\ ")
for stl in lista[1:]:
	stl = des+"/"+stl.replace(" ", "\ ")
	print (stl)
	print (mgfile)
	os.system("admesh/admesh --merge="+mgfile+" "+stl+" --write-binary-stl="+mgfile)
print ("Finished! Your final file is located at '"+tar.replace(".tar", ".stl")+"'")

os.system("cp "+mgfile+" "+tar.replace(".tar", ".stl"))

#Delete all leftover files

endings = ["*.svg", "*.stl", "*.dxf", "*.ps", "*.scad"]
for ending in endings:
	os.system("rm "+des+"/"+ending)


	

# Run a python script to combine all the .stls into one .amf