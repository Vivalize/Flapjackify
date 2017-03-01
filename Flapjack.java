package Flapjackify;

import Flapjackify.ImageTracer;
import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Comparator;
import java.nio.file.Path;
import java.io.File;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.*;

class Flapjack {
	public static void main(String[] args) {
		
		String input = "Kritin.png";
		String output = "batchTest";
		
		System.out.println("Hi I'm Buddy Valastro and welcome to CAKE BOSS");
		System.out.println("Did you ever hear the tragedy of Darth Java the Casual?");

		// Options
		HashMap<String,Float> options = new HashMap<String,Float>();

		// Tracing
		options.put("numberofcolors",8f);
		
		try{
			System.out.println("Tracing image");
			ImageTracer.saveString(output, ImageTracer.imageToSVG(input,options,null));
		} catch(Exception e){
			System.out.println("OH FuuuuuuüCK SOMETHING BROKE");
			System.out.println(e);
		}
		
		System.out.println("Splitting trace into layers");
		try{
			String[] paths = readLines(output);
			System.out.println("Got "+paths.length+" paths");
			
			//Load all relevant paths into allPaths
			singlePath allPaths[] = new singlePath[paths.length-2];
			for (int i = 1; i < paths.length-1; i++) {
				allPaths[i-1] = new singlePath(paths[i]);
			}
			
			
			List<String> allColors = new ArrayList<String>();
			for (singlePath path : allPaths) {
				if (path.opacity != 0.0 && !allColors.contains(path.color)) {
					allColors.add(path.color);
				}
			}
			
			//Make a corresponding list of color pairs and sort
			List<colorPair> allColorPairs = new ArrayList<colorPair>();
			for (String clr : allColors) {
				allColorPairs.add(new colorPair(clr));
			}
			allColorPairs.sort((o1, o2) -> Double.compare(o1.brightness, o2.brightness));

			System.out.println(allColorPairs.size() + " colors found:");
			
			for (colorPair color : allColorPairs) {				
				List<String> fileLines = new ArrayList<String>();
				fileLines.add(paths[0]);
				for (singlePath path : allPaths) {
					if (path.opacity != 0.0 && color.color.equals(path.color)) {
						fileLines.add(path.pathData);
					}
				}
				fileLines.add("</svg>");
				
				Path file = Paths.get(output + "_" + allColorPairs.indexOf(color) + ".svg");
				Files.write(file, fileLines, Charset.forName("UTF-8"));
			}
			
			
		} catch(Exception e){
			System.out.println("OH FRICK SOMETHING BROKE");
			System.out.println(e);
		}
	}
	
	public static String[] readLines(String filename) throws IOException {
		FileReader fileReader = new FileReader(filename);
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		List<String> lines = new ArrayList<String>();
		String line = null;
		while ((line = bufferedReader.readLine()) != null) {
			lines.add(line);
		}
		bufferedReader.close();
		return lines.toArray(new String[lines.size()]);
	}
	
	public static String getStringByBounds(String full, String pre, String post) {
		String[] splitAtPre = full.split(pre);
		String[] splitAtPost = splitAtPre[1].split(post);
		return splitAtPost[0];
	}
}

class singlePath {
	String pathData;
	String color;
	double opacity;

	public singlePath(String str) {
		pathData = str;
		color = Flapjack.getStringByBounds(pathData, "fill=\\\"rgb\\(", "\\)\"");
		opacity = Double.parseDouble(Flapjack.getStringByBounds(pathData, "opacity=\"", "\""));
	}
}

class colorPair {
	String color;
	double brightness;
	public colorPair(String clr) {
		color = clr;
		String[] indivColors = color.split(",");
		int red = Integer.parseInt(indivColors[0]);
		int green = Integer.parseInt(indivColors[1]);
		int blue = Integer.parseInt(indivColors[2]);
		brightness = ((double) (red+green+blue))/3.0;
	}
}