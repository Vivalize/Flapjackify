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
mgfil = des+"/"+"final.stl"
for stl in lista[1:]:
	stl = des+"/"+stl.replace(" ", "\ ")
	print (stl)
	print (mgfile)
	os.system("admesh/admesh --merge="+mgfile+" "+stl+" --write-binary-stl="+mgfil)
	mgfile = mgfil
print ("Finished! Your final file is called 'final.stl' and is located at")
print (mgfil)
os.system("cp /Users/andrewritachka/GitHub/Flapjackify/final.stl /Users/andrewritachka/GitHub/final.stl")

#Delete all leftover files

os.system("rm /Users/andrewritachka/GitHub/Flapjackify/"+"*.svg")
os.system("rm /Users/andrewritachka/GitHub/Flapjackify/"+"*.stl")
os.system("rm /Users/andrewritachka/GitHub/Flapjackify/"+"*.dxf")
os.system("rm /Users/andrewritachka/GitHub/Flapjackify/"+"*.ps")
os.system("rm /Users/andrewritachka/GitHub/Flapjackify/"+"*.scad")
os.system("cp /Users/andrewritachka/GitHub/final.stl /Users/andrewritachka/GitHub/Flapjackify/final.stl")
os.system("rm /Users/andrewritachka/GitHub/final.stl")


	

# Run a python script to combine all the .stls into one .amf