# Civizard tileset archeology ...  
## ... or possible methods for unearthing the tileset of 'Civizard - Majutsu no Keifu' for the PSX (Work In Progress; may change with new information and corrections)    
collected by [Starwisp](https://github.com/starwisp)  

'Civizard - Majutsu no Keifu' is a turn-based fantasy strategy game published by Asmik Ace Entertainment for the PSX and released exclusively in Japan in 1997. It is the Japanese port of Master of Magic (Simtex, MicroProse) released for DOS PCs in 1994 to the rest of the world. 
What makes Civizard an intriguing case is that Asmik put much work into this port. The most obvious things they changed are parts the tileset, the camera viewpoint (tilted worldmap, almost isometric as opposed to the top-down view in MoM for DOS PC), and the UI/controls (adapted for using a PSX controller). 

Civizard's distinctive terrain tileset makes it interesting to the Master of Magic modding community for use in Master of Magic mods. In this article I will describe different approaches and techniques that were attempted to get to the complete tileset including, most importantly, the terrain tiles. Fortunately, experts at the "DYKG / Do you know Gaming" Discord channel provided much advice and help. This is a summary I initially started writing for myself in order to document what was explained to me, what I tested out and what people helped me with, in case it may be of use to someone later. I hope there are not too many technical misunderstandings or mistakes.
_________
### 1. Extracting pictures from the *.BMF files via standard file viewers
Graphics data files in Civizard are in *.BMF containers with compressed and/or uncompressed *.TIM graphics files inside. *.TIM files are a standard PSX picture format.  
At first, the *.BMF data files from Civizard were loaded into several TIM file viewers/converters, such as 'Tim2view' or 'Yu_Ri', and which are able to see and extract some game assets (such as the wizard portraits and spell icons). Unfortunately, many expected assets could not be found that way (e.g. the terrain tileset). The rest of the data files seemed to be unreadable, particularly WORLD0.BMF and WORLD1.BMF, in which we suspected the terrain tileset. So this method proved to be a dead end at first. 

Tim2View: https://github.com/lab313ru/tim2view/releases/tag/r90   
Yu_Ri: https://www.romhacking.net/utilities/133
_________
### 2. Examining the PSX VRAM
We know that during normal play, the active tilesets of this game reside in VRAM. So if the graphics data cannot be accessed via the files, what about getting the tiles from VRAM?
#### 2.1. Static view of the PSX VRAM
Unzipping an 'epsxe' PSX emulator savestate and loading it into a VRAM viewer like 'PVV' or 'PSX-vram' shows the contents of the VRAM. 
Usage: Go to epsxe\sstates, pick one of the bigger files (about 1-2 mb), load it into an extraction program such as '7zip' and extract once. The received file can be loaded into 'PSX-vram' or 'PVV', which will then show something like the picture below. It shows tables with the active tilesets during the savestate's creation. Even though it is possible to take a screenshot of some of the active tiles and obtain some of them, it is not that practical.

Epsxe emulator: https://www.epsxe.com   
7zip: https://www.7-zip.org    
PVV ('PlayStation VRAM Viewer'): https://www.romhacking.net/utilities/675    
PSX-vram: https://wiki.vg-resource.com/PSX-vram  

![PVV](https://user-images.githubusercontent.com/81810020/175167706-0ece0100-85cf-4000-afa0-31d439fb6369.JPG)  
<b> Unzipped savestate loaded into 'PVV'.</b>

#### 2.2. Live view of the PSX VRAM
'No$PSX' emulator/debugger has a nice live VRAM view (thanks [vervalkon](https://github.com/vervalkon) for the tip). It enables us to inspect the terrain tiles while the game is running. Unfortunately, 'No$PSX' is not able to dump textures directly but one could take a screenshot and use a graphics editor on the little window on the bottom right. This is not very practical either but at least that way it is possible to see the terrain tiles in VRAM. 

![VRAM viewer in No$PSX](https://user-images.githubusercontent.com/81810020/175168117-b0ba2e44-c094-45ef-9e9a-a67701add634.png)  
<b>VRAM viewer in No$PSX emulator. You can see different pages of the tileset loaded in VRAM. Clicking on a tile in the game screen will point to the corresponding page in VRAM.</b>  

No$PSX emulator: https://problemkaputt.de/psx.htm  
_________
### 3. Dumping textures from VRAM
Drawback of dumping textures from VRAM: The terrain tiles seem to get dumped one after the other in the order they are called by the game as you play - not the full set as is the case with other tiles such as units. So someone would have to uncover a full map of both worlds and probably could still not be sure if they covered all the tiles. I tried it anyway to see if we get any further this way. 
The game spell "Nature Awareness" could be used to uncover the complete map, but it is not a spell you can obtain early in the game (thanks @marzepain of "Master of Magic Fans" Discord for the information). In order to speed things up, 'gameshark' cheat codes where used. Using the built in 'gameshark' codes engine in 'Retroarch' I generated some useful codes (Infinite 32767 Gp - 8019C514 7FFF; Infinite Mp [32767] - 8019C41A 7FFF, see gamehacking.org discord channel for advice on  "gameshark" code generation, also see primer on code generation in retroarch in section "Further Information" at the bottom of this readme).
After that, I used these unlimited mana and gold cheats and completed one playthrough of the game. This still took hours with a gamepad and the PSX controller UI and me not being versed in Japanese. The "Google Lens" app on a smartphone helped immensely with on-the-fly translation of menus. Eventually, the spell 'Nature Awareness' helped to uncover the complete map. This gives a higher chance to see a greater variety of tiles, but as discussed before, there is still no certainty that all available tiles in the terrain tileset are used in one playthrough. This may have to be repeated multiple times in order to see all tiles possible. Caveat: VRAM dumps only give you what is drawn into the framebuffer, i.e. what is visible on screen. So one has to move the "camera" of the overland map view window at least once over the whole game map while dumping.

As for using the terrain tiles obtained by this method in a mod for Master of Magic, one would probably have to figure out, in which order the tiles are in the data files, which name and position each single one has (for ideas on that see 6.1.). One would have to find out if Asmic has kept MoM's tileset structure or changed things significantly, since the PC version is fairly well understood. One hint was that there are two prospective terrain data files (world0.bmf and world1.bmf) which would correspond nicely to Arcanus and Myror. This may be due to PSX hardware limitations.

Retroarch: https://www.retroarch.com/  
Google Lens: https://lens.google/  

#### 3.1. Methods to dump tiles directly from PSX VRAM during play
In the section above we can see the active tileset in VRAM and we have a savestate with a fully uncovered map. Below I will show two methods for dumping the tiles from VRAM; but there may be more. Both methods lead to different results, so in the following both shall be described.

##### 3.1.1. 'Texmod' + 'epsxe' PSX emulator
This resulted in sheets with tiles in different palettes. As a proof of concept, I played a couple of turns and it filled up one sheet of terrain tiles and also produced sheets with UI elements and the like.
Usage: Execute texmod.exe first and point it to the path of epsxe.exe and launch 'epsxe' through that menu (thanks @R7CrazyCanucks of DYKG Discord channel for pointing me to texmod).  
  
Texmod: https://www.moddb.com/downloads/texmod4  
Epsxe emulator: https://www.epsxe.com  

![epsxe plus texmod Arcanus](https://user-images.githubusercontent.com/81810020/175172131-a1687850-119a-42fd-8df9-cec528e75731.JPG)
![epsxe plus texmod Myror](https://user-images.githubusercontent.com/81810020/175172161-ab56ad70-cf0c-4a43-b2d5-3596a29ab676.JPG)  
<b>'Epsxe' emulator with 'texmod' running. The grid highlights boundaries of terrain textures.</b>

Due to the PSX using palettized tilesets, we get every tileset in multiple palettes (Sony called palettes "Color Lookup Tables" or CLUTS). To produce a picture, the PSX uses only a couple "correct" tiles of every one of the differently colored tileset variations (palettes/CLUTs). 

![EPSXE EXE_0x39F8CAE1](https://user-images.githubusercontent.com/81810020/175177070-a88a1542-d2cc-4470-b88b-ebfa0c4fb6b1.png)
![EPSXE EXE_0x8FD183D3](https://user-images.githubusercontent.com/81810020/175176695-09f26973-92b1-449d-a6ac-302d85046aba.png)  
<b>Example tile sheets produced this way in different palettes.</b>  
 
##### 3.1.2. 'Retroarch' using Vulkan API + beetle PSX hw core with texture dumping 
'Retroarch' is an emulation frontend for many different systems. It can download emulation cores for emulating the desired system. The 'Beetle PSX hw' emulation core can be downloaded from the frontend and texture dumping is a toggle inside its settings when the Vulkan graphics API is used.  
As a proof of concept, I played a couple of turns which produced terrain tiles in the order they are loaded into VRAM but in contrast to the method in 3.1.1., it dumped them as one tile per file. Animation phases for the shore tiles are separate files and UI elements and other animations get dumped as sheets. Note: The single terrain tiles do not seem to be dumped in every possible CLUT/palette i.e. they seem to be dumped in the correct palette. This may be helpful later on to determine which tile is used in which palette. The sheets with other graphical elements are palettized.

Retroarch: https://www.retroarch.com/

![cd3b768e-5c91e29a](https://user-images.githubusercontent.com/81810020/175182604-57f0e645-5790-4a06-a2ae-26927eadf4cd.png)  <img src="https://user-images.githubusercontent.com/81810020/175182604-57f0e645-5790-4a06-a2ae-26927eadf4cd.png" alt="drawing" width="200"/>
![cd3b768e-6f24d07b](https://user-images.githubusercontent.com/81810020/175182637-b6844d63-a0a3-4cbf-b584-63e17280a058.png)  <img src="https://user-images.githubusercontent.com/81810020/175182637-b6844d63-a0a3-4cbf-b584-63e17280a058.png" alt="drawing" width="200"/>
![cd3b768e-5d14f602](https://user-images.githubusercontent.com/81810020/175182613-c45047ef-7774-4b75-841b-e155921c549b.png)  <img src="https://user-images.githubusercontent.com/81810020/175182613-c45047ef-7774-4b75-841b-e155921c549b.png" alt="drawing" width="200"/>

<b>Single shore terrain tiles, which seem to be part of an animation.</b>



![d24782df-172e9b9a](https://user-images.githubusercontent.com/81810020/175182754-799e2b05-4894-4947-894a-014c31d64b4f.png)
![d24782df-c8e3bd4f](https://user-images.githubusercontent.com/81810020/175182762-c241b0d5-b4c7-45ef-8df1-2b5da3a52a44.png)  
 <b>Page of tiles from VRAM in 2 different palettes (CLUTS).</b>
_________
### 4. Decompressing the datafiles
Dumping tiles from PSX VRAM yielded a number of tiles. Nevertheless, it is unclear if all tiles could be obtained and unlikely that their structure/order in the datafiles could be found out this way. Nevertheless, some information on the tileset may probably be inferred from the PC version. 
Meanwhile, [vervalkon](https://github.com/vervalkon) took a deeper look at the datafiles. 

#### 4.1. Decompressing all the tiles except the terrain tiles  
[vervalkon](https://github.com/vervalkon) suspected that the parts of the *.BMF files that were not viewable by TIM viewers were using some kind of compression. He very generously wrote a Python script to scan for and decompress image data in *.BMF files that cannot be read by standard TIM viewers. It is able to decompress most of the graphics data files of the game, and he also ended up with some suspicious files from world0.bmf and world1.bmf. Since we could not find the terrain tiles yet, and their file names were self-explanatory, we suspected them to contain the terrain tiles with one file for Arcanus and one file for Myror. See his decompressor Python script in this repository. Also see the videos on the theoretical background of the decompressor in the section "Further Information" at the end of this document.  
He has allowed me to use his explanation of the method used in the script (slightly shortened, picture is his) and to share his script:   
"Generic TIM searchers will find uncompressed TIMs but not the compressed ones. My method was eyeballing the VRAM viewer of no$psx and I saw that the vram is populated by graphics that appear piece by piece when you enter the title screen. I then viewed the TITLE.BMF file and noticed how it contains most of the same graphics as the ones that appeared in the vram." 

"Essentially, I just noticed that...  
...in title.bmf = 'a bunch of garbage', but also five readable graphic files.  
...in VRAM = six readable graphic files.  So it follows that the 'garbage' could be the sixth graphic, just compressed. 
So I extracted the sixth graphic from VRAM and started comparing its bytes with the "garbage data" and noticed similarities."

![Binary view of VRAM of title screen vs. title BMF data file](https://user-images.githubusercontent.com/81810020/175754048-c3d9e710-074b-4bff-a88e-15b30eb39c06.png)  
<b>Binary view of VRAM of title screen vs. title.BMF data file.</b>
 
" top row = bytes from VRAM
bottom row = the 'garbage' bytes from TITLE.BMF, just laid out a bit more nicely by adding spaces here and there. 
You see the top and bottom match often, but every now and then there are a few weird byte pairs on the bottom, whereas on the top there is repetition. The main idea of compression is the elimination of repetition, so I figured the byte pairs act as some kind of command words to do the repetition." 

Running the script revealed that this works very well with most *.BMF containers and most probably gives us all the graphical assets excluding the data in world0.bmf and world1.bmf which which were harder to deal with (see section 4.3). There is still the possibility that the script missed something.

Script usage:  
Copy all folders except folder "X" from the Civizard disc root to a folder on your PC.  
Make a folder named "BMFOUT".  
Load script in your preferred Python environment and adjust paths of source folder and BMFOUT folder in script (search for lines "trueroot" and "trueout").  
Run script.  
The script should decrypt most files into *.tim, *.TIM and *.bin files (.tim = decompressed file, .TIM = file was not compressed, .bin = unknown). *.TIM files and *.tim files are essentially the same only that they underwent different treatment by the script (see in script). They can both be loaded into any timviewer/converter (see section 1). Sidenote: In some Windows versions file explorer cannot distinguish between *.TIM and *.tim extensions.

#### 4.2. Finding the world map in PSX RAM (not PSX VRAM)

After this approach did not yield the terrain tileset, [vervalkon](https://github.com/vervalkon) tried a different approach in searching for the world map, which may have information on the terrain tileset. 

In order to find the game map, a binary RAM dump from the following scene was created with 'No$PSX' emulator. To do this, navigate to address 00000000 and under menu item 'Utility' hit 'Binarydump to .bin File' (set size to 400000).  

![RAM dump is from this scene](https://user-images.githubusercontent.com/81810020/175843178-2c5c90a0-863c-422c-a73b-a97cfbfa8b7b.png)  
<b>Game view in Civizard of which the RAM was dumped.</b>

![binary dump with no$psx](https://user-images.githubusercontent.com/81810020/175842578-be8601e8-8ce3-42ba-8905-087272073a66.png)  
<b>Binary dump function in no$psx emulator; game state from above shown in editor.</b>

After that, he visualized the bytes in the binary dump of the RAM content as pixels in 'GGD' graphics editor and found the game map. Though interesting, this was also a dead end.

![RAM dump in GGD](https://user-images.githubusercontent.com/81810020/175846492-cde6bee4-e1e7-4d06-b33d-e44165ca03f8.png)  
<b>Binary dump of RAM shows the Arcanus game map in 'GGD'.</b>

 ![Map in RAM](https://user-images.githubusercontent.com/81810020/175846726-4501e2d1-ac3c-4d48-980e-590d17a567f6.png)  
<b>Binary dump of RAM shows Arcanus and Myror in 'GGD'.</b>

No$PSX emulator: https://problemkaputt.de/psx.htm  
GGD ('General Graphical Dump tool'): https://randomhoohaas.flyingomelette.com/ai/spriterip/GGD-e.zip

#### 4.3. Finding the terrain tileset

The Civizard tilesets are embedded within *.bmf containers in the standard PSX *.tim graphics format. We suspected the terrain tileset within world0.bmf and world1.bmf. 

4.3.1. Some *.bmf containers can be directly read by *.tim viewers and do not seem to be compressed such as  wizard.bmf, for example, which contains the images for wizard portraits and some UI elements.
![tim2view merlin](https://user-images.githubusercontent.com/81810020/177438248-fdf4d1b5-006c-4e15-8a47-9300c689640f.JPG)  
<b>Wizards.bmf in Tim2View</b>

4.3.2. Some *.bmf containers are not accessible by *.tim viewers or other software that was tested. These are either compressed or have compressed portions. They can be decompressed by comparing the compressed datafiles with the decompressed files in RAM and subtracting everything that was different. The substracted parts are most probably commands for repetition and the like. See videos on decompression of PSX graphics data in section "Further Information". Also see the decompressor script in the repository. 

4.3.3. 
The world0.bmf and world1.bmf container files contain each: One normal *.tim file (with icons for important landmarks, see picture below), four large .bin files and four small .bin files. The small files are too small for the terrain graphics data, so it could be deduced that they might be palettes. The larger files were then suspected to be the graphics data files. Searching PSX VRAM for the bytes of the first few pixels from the datafiles was successful and proved the files were indeed the right ones and that they decompressed correctly. 
The end result of having four palette files and four graphic files suggests that one graphics file belongs to one palette file but there is also the chance that more than one *.bin file uses the same palette file. Which ones belong together is guesswork. Most probably the ones that produce at least one correct tile from the game. This is where the VRAM dumps of chapter 3 may come in handy for comparison.
'GGD' or 'TiledGGD-PE-' can be used for combining the graphics data files and palette files. The difference is that 'TiledGGD -PE-' is able to save a full tileset in one action (menu option "save all graphics"), while GGD saves only the visible panel.


![The first few pixels here were searched in the datafiles](https://user-images.githubusercontent.com/81810020/175845801-618c6d18-d470-49b1-9361-d7380dde8676.png)    
<b>The first few pixels of these tiles were searched in the datafiles and a match was found.</b>

![Tim2view of world0 tim file](https://user-images.githubusercontent.com/81810020/175849474-94e310ef-a589-4ec5-8af7-4f8e5f150280.PNG)  
<b>*.tim file of extracted from world0.bmf in tim2view; there are 7 CLUTS/palettes that can be chosen via the menu down right; it contains landmarks like cities, mana nodes, etc. .</b>
  
![World0 color coded](https://user-images.githubusercontent.com/81810020/175849605-f104c7f4-8c81-4133-8e0e-e3c8e40fe64b.JPG)  
<b>Files extracted from world0.bmf, color coded: green - palettes, purple - graphics</b>  


Tileset data can be merged with palette data using 'TiledGGD-PE-' in order to export a tileset in a specific palette as follows: 
+ Load *.bin file with image data, load file with palette information.
+ Set values as shown in the 2nd picture in the 2 squares on the right hand side: 4 bits, palette und image data in Little Endian (use 'Tiledggd-PE-' as standard 'TiledGGD' has a bug where Little Endian and Big Endian are swapped), palette skip size 16 colours, tile skip as needed (the first picture below has tile skip set to rows and the second picture has tile skip set to one tile). 
+ Then set the palette as shown in the palette view of 'TiledGGD-PE-': : black area on the bottom and left edges (the square with the rows of small coloured squares and the big yellow area - see picture below on the right side). Every row of colored squares represents one palette. 
+ Palettes can be flipped through by skipping one row of colors up or down (16 colors) ("end" and "home" keys). 
+ Use export function from menu.

Values to set in 'GGD'/'TiledGGD-PE-' (also see picture below):  
Data file: 00010384.bin.out, Palettefile: 00001104.bin.out, Imagesize: 24 x anything (one tile is 24x24 pixels, tiles are arranged as one column), Pixel/Bit: 4Bit, Palette Offset: 20, pixel width: 24; Graphics data for data file and palette file: little endian  
Advice: Always check if the palette window has a black border as shown in the picture below.

Example: If we open 00010384.bin.out as the graphics data file and 00001104.bin as the palette file in 'GGD' or 'TiledGGD-PE-' and set the right values (see top right panel in picture below), we end up with some of the terrain tiles we were looking for.  


![Graphics data and palette data in ggd ](https://user-images.githubusercontent.com/81810020/175851165-8cd09d3e-f0a3-413c-bf5b-483f83711e2a.png)  
<b>Graphics data and palette data loaded into 'GGD'; note black border in palette window</b>




Vervalkon's advice: "If you see that the first set of tiles look perfect in a certain palette, you could check the other tiles in GGD for good measure and if all other tiles look bad except the first bunch, you could export those and not worry about that particular clut (or tiles) anymore. It is a game of deduction. You need to identify as many palettes as required for every tile to look alright. Every tile has an intended palette, so if you end up with a number of image files and see that one palette has correct colors for some tiles but incorrect colors for other tiles and another palette has correct colors for some tiles but incorrect colors for other tiles, etc., then you will eventually end up with a set of tiles in the correct color." <!-- "I think only 00010384.bin.out CLUT 5 picture offset 0x0 looks correct" -->

A big thank you to [vervalkon](https://github.com/vervalkon). Without his expertise, work and patience we would not be where we are now.  


No$PSX emulator: https://problemkaputt.de/psx.htm  
GGD: https://randomhoohaas.flyingomelette.com/ai/spriterip/GGD-e.zip

_________
??? delete later  - this is being worked on ... for everyone just looking... WIP 
Combining the suspected palette bin files with the larger graphics bin data files after they were generated by the Python script, showed something akin to terrain tiles but the result was still not correct.

![tiledggd-pe- tiles directly after script](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/6c4b2440-a0ed-489d-9781-03fe14a7c3c8)


<b>decompressed terrain graphics data united with palette data ??? most probably needs to be removed</b>  

Explanation:
??? It turned out the Python script linked in this github repo cannot unpack the terrain tiles correctly. The script seems to be an older version.
??? His comment on this after sending the decompressed files samples: "when i did the initial unpacking, my code wasn't smart enough to understand to decompress those files so this is a quick 'n dirty hackjob i did — that zip contains the world0 and world1 folders but with the appropriate files decompressed" 
??? this is being actively worked on now ...
_________
### 5. Results
In the following I will summarize what we have achieved so far. There are a few areas, especially the terrain tiles, that will need some more work and trial and error (see discussion in 5.4). An some speculation on how to proceed from here. Advice and help would be appreciated.

#### 5.1. It is possible to obtain most probably all the tileset's tiles as *.TIM files via a Python decompression script excluding the terrain tiles. 
*.Tim files are standard PSX image containers and can be read and exported to standard formats by a standard TIM viewer such as 'TIM2View' and suspicious *.bin files that unknown chunks of data. 
Feeding the the TIM files into a TIM viewer gives you all the sprites, UI elements etc. in all palettes (or CLUTs as they are also called in PSX viewers). With Tim2View or Yu_Ri PSX file viewer/converter, they can be converted to PNGs or BMPs with or without transparency. For a full tileset you would have to make sure to also convert them in all the palettes. These tools unfortunately do not automatically do this. They also do not automatically export them into appropriately named subfolders but into one folder and seemingly randomly numbered files. The game logic most probably knows what to do with the numbering though. 
#### 5.2. It is possible to obtain some terrain tiles from VRAM. 
Using this method, it was not possible to find out the terrain tiles' correct order and naming scheme in the terrain data containers, their correct palettes, or if we have all of them.
#### 5.3. It is possible to decompress world0.bmf and world1.bmf into binary files consisting of terrain tile image data plus their palette information - but with problems
The suspicious files from world0.bmf and world1.bmf were indeed each 4 files with the image data for terrain tiles and 4 files with corresponding palette information (so one .BMF file for Arcanus and one for Myror). Now we have to find the correct pairs of image data files and palette files. The dumps from the PSX VRAM were not in vain since in theory they might be used to verify the correct palette file <-> data file pairs. I have not been able to do that for all files since I could only match one pair with one VRAM dump so far (see below).

![Left decompressed terrain tiles vs. left dump from PSX VRAM](https://user-images.githubusercontent.com/81810020/175188859-014385ca-0cbb-4229-804f-cf895376d82a.JPG)  
<b>Verification of decompressed tileset - left decompressed terrain tiles with correct palette, right dump from VRAM</b>

<!-- ??? Delete later ????  vervalkon said this is the wrong clut... he only sent the appropriate ones, the others are for UI elements and so on, ???but all of the cluts are in VRAM that'S why they get dumped...??? If it is already in VRAM in this clut, then it looks like some tiles of this clut have to be used. . Correct: For example the mountains are used on the Myror map. ???? -->

#### 5.4. Problems with the decompressed terrain tiles and where we are at with this project 
+ The names of the terrain tiles (or some kind of index by which they are called by the game) could not be retrieved with the decompression Python script since it only searches for graphics data. Maybe one could infer from Master of Magic's handling of tiles in its *.lbx container format. 
+ I suspect, you would also need a way to find out for every tile, in which palette it is used in the game. Every terrain tile can be used in a multitude of palettes/CLUTS. All that is left is figuring out if the game has a table that assigns the correct CLUT/palette to the corresponding tiles.
+ Some of the image data were pixel shifted in one or two directions. One tileset looked good. This may be rectified by using the image data offset function in editors like 'GGD' or 'TiledGGD-PE-'. The problem here is that I have not found an editor that can apply this offset, fuse image files and palette files, and save the whole set at once with all the settings needed. It will work in increments of a of a couple of tiles in 'GGD' but then you would somehow have to put the set back together afterwards. 
+ The last tile in some of tileset files seems to have a couple of pixels missing, probably an artefact of the script.
+ There were areas with no tiles/black areas in every terrain tileset (see picture below). I have no idea if these are supposed to be there or if they are some kind of corruption.
+ Unlike the other tiles in the Civizard data files, the extracted terrain tiles are separated from their palette information. 
Within the world0 and world1 output directory we ended up with files with image data and files with palette data. The palette files can be read and reunited with the image data with the tools 'TiledGGD-PE-' or 'GGD'. In this case, 'TiledGGD-PE' was used. Which image data file goes with which palette file and if some files use the same palette file will be guesswork.

TiledGGD-PE- (with fixed endianness- endianness is swapped in regular TiledGGD): https://github.com/puggsoy/tiledggd-pe-   
GGD: https://randomhoohaas.flyingomelette.com/ai/spriterip/GGD-e.zip  

![View in TiledGGD-PE, pixel-shifted](https://user-images.githubusercontent.com/81810020/175186828-95a6090f-c4f6-4833-a787-4a937575c4ef.JPG)  
<b>Extracted tileset - black areas and pixel-shifted, viewed in 'TiledGGD-PE-'</b>
   
![Pixels shifted 8 pixel columns horizontally 1 pixel vertically](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/8415f6df-3058-496c-992e-cdd2ab349f7e)



<b>More detailed view of pixel shifts, viewed in 'TiledGGD-PE-'; also see used values and palette view</b> 
_________
### 6. Future ideas and miscellanious side ventures
#### 6.1. Get terrain tiles and their names via savestate hex edit
A big thank you to @darkwolf at DYKG Discord channel for suggesting this. He has allowed me to use his explanation of this method (the pictures are also his):
"The game has to store the map (the game's logical structure for the playfield) in memory during gameplay. It may be possible to modify a savestate via hex editor in a way that the game map displays a sequential set of tiles. The game is forced to display the tile numbers we want. Then we would screenshot or dump the tiles from VRAM.
Example: This is Kid Chameleon for Genesis, but it could apply to multiple platforms, if the level data is stored in a similar way.
So I know from past experience that there is a copy of the level kept in RAM for Kid Chameleon, so I grabbed a savestate. I went to the address in the save state where the that copy is kept. I also happen to know that the game stores the level data in two bytes, one for the platform type and the other for the graphical tile. So I updated the graphical tiles $00 to $0F in a hex editor."  

![Hex edit save state to display tiles in sequential order](https://user-images.githubusercontent.com/81810020/175755182-c1f58aec-5823-4efc-8531-6460e6ab1560.png)  
<b>Savestate in HxD</b>  
 
"When I load that save state in, then move away from the area and come back, I get my tiles."
![Hexedit to display sequential tiles](https://user-images.githubusercontent.com/81810020/175755200-b13bcadb-5086-454a-b076-8dd5559c1475.png)
<b>After savestate is edited, it displays the expected tiles</b>
 
I wonder if one could also get the number/name of every terrain tile in this way. Unfortunately I know too little in this area to do this or how feasible this would be. We would probably have to know more information on the Civizard save states and find the tilemap data. He suggested to try with 'GGD'. I thought this method is worth being documented.

HxD Hex Editor: https://mh-nexus.de/en/hxd/

#### 6.2. Uncovering the fog of war/game map.
While searching through no$psx savestates of Civizard for clues to the tiles and how to apply the principles of 6.1. [vervalkon](https://github.com/vervalkon) made a nice discovery. Somewhere around the 0x1FEC60 range onwards there is an array of bytes that determine the fog of war. 00 appears to be unseen, and that small bubble is the visibility map in the beginning of a new map/game.  

![visibility bubble at start of a new game](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/d2dc7a4d-432d-4c44-9fc8-2bde92cd3f34)
<b>Visibility bubble at start of a new game</b>  

It is probably bitwise but it's obvious that 01 is a topright corner, 02 a bottom right one, 04 a bottom left, 08 a top left, etc. (see pic below).  
![fow2](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/bbd9ef48-3673-48c5-8888-68abc6e79274)  
<b>Visibility bubble large</b>  

0F being the "fully visible" index, then just fill everything with 0Fs and load it.
![fow3](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c737894d-de31-44aa-a2e3-f76325d49b7e)
<b>Fog of war lifted</b>  

Explanation:
The fog of war map/visibility map is a 2-dimensional array that's of unknown size - I just pasted a good amount of 0Fs over the 00s. If I had written too little, it all wouldn't be visible, if I had written too much, I might've overwritten some other important data.
Before a frame is shown, the game reads the map data and draws the full map. Once it has drawn the full map, it reads the fog data from RAM and draws the fog over it. I knows what kind of a fog pattern to make by reading the area around the 1FEC6C range (not 100% sure of the precise address). 
It determines the fog status likely by reading bits.
In binary:
00 = 0000  
01 = 0001  
02 = 0010  
03 = 0011  
04 = 0100  
05 = 0101  
06 = 0110  
07 = 0111  
08 = 1000  
09 = 1001  
0A = 1010  
0B = 1011  
0C = 1100  
0D = 1101  
0E = 1110  
0F = 1111  

![fow3](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c737894d-de31-44aa-a2e3-f76325d49b7e)
<b>Numbers represent fog patterns</b>  

For example: Empty cells are 00 . There is a logic here - think of the bits as like checkboxes

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/3d027068-df2b-4d63-88a4-e14b606d5193" alt="drawing" width="300"/>   

<b>Numbers represent fog patterns; Arrows represent corners</b>   

One bit represents one corner state. Think of bit 0 as "fogged" and bit 1 as "shown". 
byte 00 (which is 0000 in binary) means fog all corner, thus any byte in the fog map that is 00 is fogged. 
byte 0F is 1111 in binary, so all corners are "set" so to speak.  
Example: 0E is the cornerpiece in the bottom left of the spotlight of the initial map state, and unsurprisingly it has only one bit as 0.  

#### 6.3. Sequential tile injection 
As proposed in 6.1., if one would modify a savestate (aka memory snapshot of an emulator), locate the visible game map and replace the names of tiles with a sequential number, in order to have the game map display a sequential set of tiles. Every tile comes in a multitude of CLUTS/palettes but has only one correct CLUT. This way one could find the CLUT of the tiles used ingame and later possibly the logic behind it.  
![game map in memory snapshot](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/cb390db8-1f01-4f51-868c-3961dedb0fbb)  
<b>Game map in memory snapshot of no$psx</b>     



#### 6.4. Civizard music tracks - an alternate version of the Master of Magic tracks
Civizard has the same tracks as Master of Magic DOS but the devs seem to have ran them on a different midi module and recorded them onto the CD. The instruments sound different and provide an interesting alternate version of the iconic tracks to those used for the newer Master of Magic for Windows. Unfortunately the Civizard tracks have a bad echo to them and are distorted at times. In theory, they could be run through some post-processing software and be used in a mod for Master of Magic. But this would be for someone else to try.
They can be read and exported with the tool jpsxdec. 

jpsxdec: https://github.com/m35/jpsxdec
_________
### Acknowledgments
[vervalkon](https://github.com/vervalkon) for his invaluable technical knowledge and for writing the extraction script in the repository, all the helpful people of the "DYKG / Do you know Gaming" Discord channel (@darkwolf, @R7CrazyCanucks, etc.),"Master of Magic Fans" Discord channel (@blakessanctum for coming up with the idea of using the Civizard tileset for Master of Magic, [jimbalcomb](https://github.com/jbalcomb) for technical information on Master of Magic).
_________
### Disclaimer 
The contents of this repository are for educational use only. Use at your own risk. The game, all its game assets and the game's IP are properties of their respective owners / rights holders. Links are being provided as a convenience and for informational purposes only; they do not constitute an endorsement or an approval.
_________
### Further information
+ Primer on sprite ripping and on the usage of 'GGD' https://randomhoohaas.flyingomelette.com/ai/spriterip/#ggd 
+ "DYKG / Do you know Gaming" Discord channel https://discord.gg/dykg
+ "Master of Magic Fans" Discord channel https://discord.gg/69qMbHtV
+ "Realms Beyond" Master of Magic forum https://www.realmsbeyond.net
+ Primer on the creation of gameshark cheat codes using "Retroarch" https://docs.libretro.com/guides/cheat-codes/
+ Theoretical background of the decompressor script using a similar case as example by [vervalkon](https://github.com/vervalkon) https://www.youtube.com/watch?v=LASE8IiGB9Q
+ Video on decompression for the psx game Tomba 2 by [vervalkon](https://github.com/vervalkon) https://www.youtube.com/watch?v=f6Vh9b1Kiw8
+ Tutorial - How to find PSX palettes by [vervalkon](https://github.com/vervalkon) https://www.vg-resource.com/thread-41343.html
