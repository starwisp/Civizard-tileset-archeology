# Civizard tileset archeology ...  
## ... or unearthing the tileset of 'Civizard - Majutsu no Keifu' for the PSX  
(Work In Progress, skip to paragraph 8 for TL;DR on usage of the decompressor script).  
Authors: [Starwisp](https://github.com/starwisp);
[vervalkon](https://github.com/vervalkon)

'Civizard - Majutsu no Keifu' is a turn-based fantasy strategy game published by Asmik Ace Entertainment for the PSX and released exclusively in Japan in 1997. It is the Japanese port of Master of Magic (Simtex, MicroProse) released for DOS PCs in 1994 to the rest of the world. 
What makes Civizard an intriguing case is that Asmik put much work into this port. The most obvious things they changed are parts of the tileset, the camera viewpoint (tilted worldmap, almost isometric as opposed to the top-down view in MoM for DOS PC), and the UI/controls (adapted for using a PSX controller). 

Civizard's distinctive terrain tileset makes it interesting to the Master of Magic modding community. In this article I will describe different approaches and techniques that were attempted to get to the complete tileset including, most importantly, the terrain tiles. Fortunately, experts at the "DYKG / Do you know Gaming" Discord channel provided much advice and help. This is a summary I initially started writing for myself in order to document what was explained to me, what I tested out and what people helped me with, in case it may be of use to someone later. I hope there are not too many technical misunderstandings or mistakes. This is mainly an educationtal project to me in order to learn about and document retro pixelart/animation techniques and Python programming.   

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
<figure>
<img src="https://user-images.githubusercontent.com/81810020/175167706-0ece0100-85cf-4000-afa0-31d439fb6369.JPG"
<figcaption><b> Unzipped savestate loaded into 'PVV'.</b></figcaption>  
</figure>  

#### 2.2. Live view of the PSX VRAM
'No$PSX' emulator/debugger has a nice live VRAM view (thanks [vervalkon](https://github.com/vervalkon) for the tip). It enables us to inspect the terrain tiles while the game is running. Unfortunately, 'No$PSX' is not able to dump textures directly but one could take a screenshot and use a graphics editor on the little window on the bottom right. This is not very practical either but at least that way it is possible to see the terrain tiles in VRAM. 

<figure>
<img src="https://user-images.githubusercontent.com/81810020/175168117-b0ba2e44-c094-45ef-9e9a-a67701add634.png">  
<figcaption> <b>VRAM viewer in No$PSX emulator. Pages of the tileset in VRAM. Clicking on tile in game screen points to corresponding page in VRAM.</b></figcaption>
</figure>   

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
Usage: Execute texmod.exe first and point it to the path of epsxe.exe and launch 'epsxe' through that menu (thanks @R7CrazyCanucks of DYKG Discord channel for pointing me to 'texmod').  
  
Texmod: https://www.moddb.com/downloads/texmod4  
Epsxe emulator: https://www.epsxe.com  

![epsxe plus texmod Arcanus](https://user-images.githubusercontent.com/81810020/175172131-a1687850-119a-42fd-8df9-cec528e75731.JPG)
![epsxe plus texmod Myror](https://user-images.githubusercontent.com/81810020/175172161-ab56ad70-cf0c-4a43-b2d5-3596a29ab676.JPG)  
<b>'Epsxe' emulator with 'texmod' running. The grid highlights boundaries of terrain textures.</b>

Due to the PSX using palettized tilesets, we get every tileset in multiple palettes (Sony called palettes "Color Lookup Tables" or CLUTs). To produce a picture, the PSX uses only a couple "correct" tiles of every one of the differently colored tileset variations (palettes/CLUTs). 

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

<b>Single shore terrain tiles, which seem to be part of an animation. Original size tiles next to enlarged versions.</b>



![d24782df-172e9b9a](https://user-images.githubusercontent.com/81810020/175182754-799e2b05-4894-4947-894a-014c31d64b4f.png)
![d24782df-c8e3bd4f](https://user-images.githubusercontent.com/81810020/175182762-c241b0d5-b4c7-45ef-8df1-2b5da3a52a44.png)  
 <b>Page of tiles from VRAM in 2 different palettes (CLUTS).</b>
_________
### 4. Decompressing the datafiles
Dumping tiles from PSX VRAM yielded a number of tiles. Nevertheless, it is unclear if all tiles could be obtained and unlikely that their structure/order in the datafiles could be found out this way. Some information on the tileset may probably be inferred from the PC version.  

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

#### 4.2. Finding the world map in PSX RAM

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
<b>Wizards.bmf in 'Tim2View'.</b>

4.3.2. Some *.bmf containers are not accessible by *.tim viewers or other software that was tested. These are either compressed or have compressed portions. They can be decompressed by comparing the compressed datafiles with the decompressed files in RAM and subtracting everything that was different. The substracted parts are most probably commands for repetition and the like. See videos on decompression of PSX graphics data in section "Further Information". Also see the decompressor script in the repository. 

![m7](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/b4d7d425-c309-4da1-8173-7425b3004670)  
<b>Decompressed /Monst/7/182.bmf, previously not accessible with *.tim viewers.</b>   

4.3.3. 
The world0.bmf and world1.bmf container files contain each: One normal *.tim file (with icons for important landmarks, see picture below), four large .bin files and four small .bin files. The small files are too small for the terrain graphics data, so it could be deduced that they might be palettes. The larger files were then suspected to be the graphics data files. Searching PSX VRAM for the bytes of the first few pixels from the datafiles was successful and proved the files were indeed the right ones and that they decompressed correctly. 
The end result of having four palette files and four graphic files suggests that one graphics file belongs to one palette file but there is also the chance that more than one *.bin file uses the same palette file. Which ones belong together is guesswork. Most probably the ones that produce at least one correct tile from the game. This is where the VRAM dumps of chapter 3 may come in handy for comparison.
'GGD' or 'TiledGGD-PE-' can be used for combining the graphics data files and palette files. The difference is that 'TiledGGD -PE-' is able to save a full tileset in one action (menu option "save all graphics"), while 'GGD' saves only the visible panel.


![The first few pixels here were searched in the datafiles](https://user-images.githubusercontent.com/81810020/175845801-618c6d18-d470-49b1-9361-d7380dde8676.png)    
<b>The first few pixels of these tiles were searched in the datafiles and a match was found.</b>

![Tim2view of world0 tim file](https://user-images.githubusercontent.com/81810020/175849474-94e310ef-a589-4ec5-8af7-4f8e5f150280.PNG)  
<b>*.tim file of extracted from world0.bmf in tim2view; there are 7 CLUTS/palettes that can be chosen via the menu down right; it contains landmarks like cities, mana nodes, etc. .</b>
  
![World0 color coded](https://user-images.githubusercontent.com/81810020/175849605-f104c7f4-8c81-4133-8e0e-e3c8e40fe64b.JPG)  
<b>Files extracted from world0.bmf, color coded: green - palettes, purple - graphics.</b>  


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
<b>Graphics data and palette data from files in world0.bmf loaded into 'GGD'; note black border in palette window</b>  

![Part of the Terrain tileset world 0](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/b3488afd-ef5c-4e05-9cbb-96791764654a)
<b>Same part of the terrain tileset from world0.bmf as in picture directly above, different CLUT, and in 'TiledGGD-PE-'; different CLUTS can be selected in the palette window on the right. There is no correct CLUT for all tiles of a subset at the same time. It is set by the game on a per tile basis.</b>  

![middle correct tiles](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/9b53760a-cbd9-498d-8268-791067f223b4)
<b>Same subset of tiles in different CLUT, but with correct tiles for this particular CLUT highlighted </b>  

If you see that the first set of tiles look perfect in a certain palette, you could check the other tiles in GGD for good measure and if all other tiles look bad except the first bunch, you could export those and not worry about that particular clut (or tiles) anymore. It is a game of deduction. You need to identify as many palettes as required for every tile to look alright. Every tile has an intended palette, so if you end up with a number of image files and see that one palette has correct colors for some tiles but incorrect colors for other tiles and another palette has correct colors for some tiles but incorrect colors for other tiles, etc., then you will eventually end up with a set of tiles in the correct color. <!-- "I think only 00010384.bin.out CLUT 5 picture offset 0x0 looks correct" -->  

A big thank you to [vervalkon](https://github.com/vervalkon). Without his expertise, work and patience we would not be where we are now.  

No$PSX emulator: https://problemkaputt.de/psx.htm  
GGD: https://randomhoohaas.flyingomelette.com/ai/spriterip/GGD-e.zip  
TiledGGD-PE- (with fixed endianness- endianness is swapped in regular TiledGGD): https://github.com/puggsoy/tiledggd-pe-     

#### 4.4. Terrain tileset 2nd look  

I looked at the 4 larger files with the terrain graphics data in 'TiledGGD-pe-' and noticed 'shifting' and 'tearing' and an area at the end of another bin that looked like it was cut off too early.  

<p align="center">
<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/8415f6df-3058-496c-992e-cdd2ab349f7e" alt="drawing" width="500"/>  
  <br>
    <b>'Shifted' pixels; viewed in 'TiledGGD-PE-'.</b>
</p>



![View in TiledGGD-PE, pixel-shifted](https://user-images.githubusercontent.com/81810020/175186828-95a6090f-c4f6-4833-a787-4a937575c4ef.JPG)  
<b>Extracted tileset - black areas and tearing, viewed in 'TiledGGD-PE-'.</b>  

![middle correct tiles](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/021c45cd-81ed-4c43-9a24-d9351c35a417)  
<b>Arrows point to problems: Last tile has some bytes missing; black areas could be normal. The black area on position 00 in the decompressed terrain datafile occurs in the live game after sequential tile injection (see image in 6.2) as well on position 00. So we can infer that it may be intentional. We will look into this a bit more, though.</b>  

While we were brainstorming this, Vervalkon was able to pinpoint the problem: The shifting pixel issue was because, 00067084.bin.out was missing 20 pixels from the beginning and 00010384.bin.out had an extra 4 pixels in its end. 
Since one tile has 24x24 pixels that would hint at one more tile (20+4 pixels) that was split onto 2 files during decompression. This shifted the pixels of most files around (also the pixels of 24x24 completely black tiles). Since 'TiledGGD-PE-' was set to display that large chunk of grafics data as blocks of 24x24 pixels (the tiles), we ended up with 'shifts'/'tears'. 
If 2 bins are actually one file and the other 2 have the same problems, maybe all 4 bins might be part of one large file that was split at the wrong points. The solution was to manually combine all 4 larger bins into one file (world0.bmf and world1.bmf, respectively). This got rid of the tearing and shifting and left us 2 nicely laid out files (still sans palettes).  

![myror](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/52cb83ea-379f-4326-8c95-dc94d5496f1c)   
<b>Myror tiles from world1.bmf; no "tearing"; mushroom forest tiles highlighted.</b>  

#### 4.5. Terrain tileset part 3 - patching and combining the script output files

Unfortunately the script has a bug that stops it from extracting the terrain files in grph/world0 and grph/world1 and slices them im 4 files with numbered names that read like the game internal names of resource files in the other directories. So while they are extracted from their BMF containers, they are still compressed when combined with one of the palette files. This will be addressed in a later step below. 

![tiledggd-pe- tiles directly after script](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/6c4b2440-a0ed-489d-9781-03fe14a7c3c8)  
<b>Extracted but still compressed terrain graphics data after script; united with palette file</b>  

After using the script on the data files from the Civizard disk we end up with the following graphics data files in the output directory of GRPH/WORLD0 and GRPH/world1:  

world0: 00010384.bin, 00067084.bin, 00114376.bin, 00150948.bin.  
world1: 00010384.bin, 00068968.bin, 00119992.bin, 00162648.bin.  
 
In order to be able to use them, we need to combine them into one file. This can be done with the command shell of your preferred OS.  

Windows:  
Open command prompt/shell in the folder in question or navigate there.   
Command for GRPH/WORLD0: "copy /b 00010384.bin+00067084.bin+00114376.bin+00150948.bin compressedworld0.bin"  

Command for GRPH/WORLD1: "copy /b 00010384.bin+00068968.bin+00119992.bin+00162648.bin compressedworld1.bin"  

As of version 1.1, this step has been added to BMFtool. BMFtool ver. 1.0 has been preserved in case this step does not work on other operating systems than windows. 

[vervalkon](https://github.com/vervalkon) was able to write a custom extractor for the 2 x 4 files from world0 and world1 (hence the "bin.out" files in the images above), but it got lost. Luckily we still had the extracted files. So a binary difference patch from the compressed files to the extracted files for extracting the files from their original game disk was created (see IPS patches for world0 and world1 in this repo). The patch can be applied to its corresponding compressedworld0.bin or compressedworld1.bin using an IPS patcher like "LunarIPS" in order to decompress them. But beware, "LunarIPS" does not change directories automatically in its menus and thus makes it easy to combine the wrong patch and compressed tileset file. Also select "all files" in the menus. Maybe I can come up with a more elegant solution here later such as fixing the python script. "LunarIPS" is not normally used in this context but this method works fine for the moment. This leaves us with one file for the tiles minus palettes and landmarks for Arcanus and Myror, respectively. 

LunarIPS: https://www.romhacking.net/utilities/240/  

#### 4.6. What are the 4 CLUT files in world0.bmf and world1.bmf for?   

There are 4 different palette files in world0.bmf and world1.bmf. While they have the same names and look similar, some of them are NOT the same palettes for both containers (see palette file 00001104.bin used in images in 4.7.).  
So far I could determine in 'TiledGGD-pe-' that palette 00001104.bin of world0.bmf can produce tiles for Arcanus (with greens and blues, see last 2 images of 4.3.3.) and palette 0000040.bin of world1.bmf can be used to create tiles for Myror (with variations of brown, see last image of 5.4.), but also 00001104.bin ow world1.bmf can be used for brownish tiles. The terrain tiles from World0.bmf contain the highlighted green forest tiles that only look correct with a palette from 00001104.bin, so this is probably Arcanus. World1.bmf contains the highlighted mushroom forest tiles that only look correct with 0000040.bin, so this is probably Myror. So, why does each bmf file 2 palette files of unknown purpose and some palettes (= row of 16 colours in a palette files) with 3 seemingly out of place colours only?  

The answer, we suspect, may lie in an interesting animation technique used in classic games. Many of these terrain tiles look muted compared to their in-game appearance. This is due to clever CLUT animations. The palettes if these terrain tiles get changed fast enough that it appears as an animation. But instead of different tiles as animation phases (such as with the monster tiles), it is the same tile but in different palettes. This, for example, leads to the shore wave animations or glow effects in Civizard. This technique is called color cycling. (see 'Example of color cycling' and link to Wikipedia entry on color cycling in "Further Information"). This way the game can change the muted colors of terrain tiles to an almost glowing effect. 
In a way, there is no one true palette to get the ingame look of some of the tiles if the color cycling can not be replicated. Curious is also, that there is an abundance of purple at areas of tiles where colour cycling is used ingame (for example, see first couple rows of tiles in image in 4.7. - the shore areas that have colour cycling animations are purplein one of the palettes/rows of colours of the CLUT/palette file). 



https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/b4635be5-e8a8-48a2-9a64-81ff10217168  

<b>Shore animation. Color cycling in Civizard.</b>   

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/ed0047bc-3f44-4ffe-9589-73f75a75df8e" alt="drawing" width="550"/>   

<imgcaption><b>Same shore tiles in the data files. Note the muted colors.</b></imgcaption>  

Colour cycling is the reason why in earlier stages of this project, tiles with animation phases of waves could be dumped from VRAM (see images end of section 3.1.2.), but later, these could not be found in the decompressed terrain files. "Retroarch beetle hw core" just dumps what is loaded into VRAM and in that case it was the same tile in different CLUTs.    
Let's see if we can figure out how this works in Civizard. It may have something to do with the extra palettes, but we cannot say for sure yet.  


#### 4.7. world0.bmf and world1.bmf - terrain tiles extracted  

Now we reduced the files from world0.bmf and world1.bmf each to one *.tim file for landmarks, one bin file for tiles and four bin files for palettes/CLUTs. 
While there is still a lot of manual work involved, we found a way to extract the terrain tiles.  
  
![all x 1104 rivers](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/8bbeb057-647e-4678-b1ce-8b7cdd06181b)
<b>Screenshot of full tileset WORLD0.bmf/Arcanus in TiledGGD(PE) editor combined with palette file 00001104.bin; presumably with correct palette for river tiles selected; should be compared to ingame footage since there is more than one palette that fits here.</b>  
   
![mountains world1bmf palette 00001104](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/dcba4966-b98b-4c45-83d0-8cffa2ad3c31)
<b>Screenshot of full tileset WORLD1.bmf/Myror in TiledGGD(PE) editor combined with palette file 00001104.bin; with correct palette for mountain tiles selected.</b>   
    
This still involves many manual steps, knowledge of PSX graphics, and the usage of "tiledggd-pe-" and other tools. Then there is the question why so far we only needed 2 of the 4 palette files and if these may be combined with the rest of the tileset graphics data to make them regular PSX *.tim graphics files that do not need 'TiledGGD'. This would make them easier to work with.  
   
TiledGGD-PE- (with fixed endianness- endianness is swapped in regular TiledGGD): https://github.com/puggsoy/tiledggd-pe-  

#### 4.8. Palettes of the terrain tiles



#### 4.9. Figuring out the right palettes for each subset of terrain tiles  
There is one tile sheet for Arcanus and one tile sheet for Myrror. We noticed that the tiles are arranged by groups such as forest, river, shore, sea etc. . These groups usually look correct with the same palettes but most of the times only these and not the rest. Some time after releasing the script, method and results mod author Suppanut (Caster of Magic Warlord) got in contact and figured out how to find the right palette for each group of terrain tiles. With his permission I will now describe how he did it.
Some CLUTs contain have several colors replaced by neon pink. This means the parts using these colors are transparent. So he exported that sheet and added alpha, then deleted the pina areas before overlapping that with a combined sheet. Then the correct group of tiles was visible. Doing that for every CLUT revealed the correct colors for every group of tiles of both worlds.   

#### 4.9.1  
The resulting palettes are listed below. The code for the CLUT can be read in the CLUT area (top right) of TiledGGD-PE- and derives from the blocks of 16 colors that comprise one palette/CLUT. 

CLUT file 1104:  
0x14 grassland  
0x34 forest  
0x54 swamp  
0x74 hills  
0x94 mountains  
0xB4 sea  
0xD4 river  
0xF4 desert  
0x114 tundra  
0x134 volcano  

CLUT file 40:  
0xF4 chaos node  
0x1B4 nature node  
0x1D4 sorcery node  

CLUT file 572:  
Seems to be a reddish glow or fire effect. Might be part of an overland spell animation.  

CLUT file 9852:  
Seems to be a white flash effect. Might also be part of an overland spell animation.  

With this information a full set of terrain tiles with correct CLUTS can be compiled.  

#### 4.9.2
After figuring out the correct palettes for the base set there was still the question of animated tiles such as shore tiles. 

_________
### 5. Results
In the following I will summarize what we have achieved so far. There are a few areas, especially the terrain tiles that are harder to get to. Some speculation on how to proceed from here. Advice and additional information is always welcome.

#### 5.1. It is possible to obtain most many of the tileset's via a Python decompression script... 
...excluding the terrain tiles, the font files and some others which get decompressed to *.bin files that contain unknown chunks of data. Feeding the TIM files into a TIM viewer gives you all the sprites, UI elements etc. in all palettes (or CLUTs as they are also called in PSX viewers). With Tim2View or Yu_Ri PSX file viewer/converter, they can be converted to PNGs or BMPs with or without transparency. For a full tileset you would have to make sure to also convert them in all the palettes. These tools unfortunately do not automatically do this. They also do not automatically export them into appropriately named subfolders but into one folder and seemingly randomly numbered files. The game logic most probably knows what to do with the numbering though. 
#### 5.2. It is possible to obtain some terrain tiles from VRAM. 
Using this method, it was not possible to find out the terrain tiles' correct order and position in the terrain data containers, or if we have all of them. Their correct palettes can be obtained manually in no$psx's VRAM debugger (see section 6.4) but maybe there is a more elegant route.
#### 5.3. It is possible to decompress world0.bmf and world1.bmf into binary files consisting of terrain tile image data plus their palette information - but with problems
The suspicious files from world0.bmf and world1.bmf were indeed the image data for terrain tiles and 4 files with palette information (so one .BMF file for Arcanus and one for Myror). The four bin with the image data can be combined to one file which fixes most of the graphical problems with them. We could match one palette file to Arcanus and one to Myror and suspect the other 2 palette files to be part of color cycling effects that are used by the game.


The dumps from the PSX VRAM were not in vain since in theory they might be used to verify results using other methods such as palette file <-> data file pairs. 

![Left decompressed terrain tiles vs. left dump from PSX VRAM](https://user-images.githubusercontent.com/81810020/175188859-014385ca-0cbb-4229-804f-cf895376d82a.JPG)  
<b>Verification of decompressed tileset - left decompressed terrain tiles after decompression -one of many possible CLUTs, right dump from VRAM which also has the same tiles in different CLUTS but as sheets </b>   

_________
### 6. Further experiments and ideas (may expand in time)
#### 6.1. Alternative method: Getting terrain tiles, their names and CLUTs via savestate hex edit
A big thank you to @darkwolf at DYKG Discord channel for suggesting this. He pointed me to the method and has allowed me to use his explanation (the pictures are also his):
"The game has to store the map (the game's logical structure for the playfield) in memory during gameplay. It may be possible to modify a savestate via hex editor in a way that the game map displays a sequential set of tiles. The game is forced to display the tile numbers we want. Then we would screenshot or dump the tiles from VRAM.
Example: This is Kid Chameleon for Genesis, but it could apply to multiple platforms, if the level data is stored in a similar way.
So I know from past experience that there is a copy of the level kept in RAM for Kid Chameleon, so I grabbed a savestate. I went to the address in the save state where the that copy is kept. I also happen to know that the game stores the level data in two bytes, one for the platform type and the other for the graphical tile. So I updated the graphical tiles $00 to $0F in a hex editor."  

![Hex edit save state to display tiles in sequential order](https://user-images.githubusercontent.com/81810020/175755182-c1f58aec-5823-4efc-8531-6460e6ab1560.png)  
<b>Savestate in HxD</b>  
 
After loading the savestate into the emulator after modification the player needs to jump away from and back to the screen. Then the game displays the manipulated tiles.
![Hexedit to display sequential tiles](https://user-images.githubusercontent.com/81810020/175755200-b13bcadb-5086-454a-b076-8dd5559c1475.png)
<b>After savestate is edited, it displays the expected tiles</b>  

HxD Hex Editor: https://mh-nexus.de/en/hxd/  

#### 6.2. Sequential tile injection...  
...or manipulating the game into showing us the terrain tiles and additional information.     
As proposed in 6.1., a 'Civizard' savestate (aka memory snapshot of an emulator) from 'No$PSX' was modified. The visible game map was located and the names of tiles were replaced with sequential numbers, in order to have the game map display a sequential set of tiles. Every tile comes in a multitude of CLUTS/palettes but has only one correct CLUT. This way one could find the CLUT of the tiles used ingame and later possibly the logic behind it. There is a method for finding a CLUT that hinges these principles but it only works on a savestate basis. It would take too much space to discuss in detail here. A tutorial for this method can be found in section "Further Information" ("Tutorial - How to find PSX palettes").  
 
Opening a no$psx savestate in a hexeditor and searching around shows the following: 

<p align="center">
  <img alt="game map" src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/cb390db8-1f01-4f51-868c-3961dedb0fbb">
  <br>
    <b>Game map in memory snapshot of no$psx</b>
</p>


A representation of the game map can be seen in the hex editor (think of that scene in "The Matrix" when Neo can see the world in green code/symbols).
The area of visibility (no fog of war) could be located by using that representation of the map.  

![map tile injection](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c56fa732-8150-4f97-99e1-05301af97452)  
<b>Game area of visibility</b>   

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/8625df00-bc4b-478e-9bc5-8a6cfb225c9c" alt="drawing" width="400"/>  


<b>Area of visibility from picture above corresponds roughly to this location</b>  

An array of sequential words was pasted onto that area editing the map to display tiles from 00 onwards instead of what the original tiles are. Savestate was saved in the editor and loaded back into no$psx. The manipulated area now displays the tiles by their internal name in sequential order. The terrain tiles could be grabbed or dumped from there in the correct CLUT and order.  

![sequential words in map](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/0828666a-7cea-4afd-b44c-b022332f5fb8)  
<b>Array of sequential words copy pasted on game map</b>   

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/e6928318-921c-4240-95e1-a0aa5ac26a0a" alt="drawing" width="550"/>   

<b>Game shows a sequential number of tiles in the correct CLUTs in no$psx</b>  

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/69dcb982-8b02-4220-a2fa-b511ba615e85" alt="drawing" width="550"/>   

<imgcaption><b>Same as injected tiles from above. In same order, but decompressed from world0.bmf datafiles</b></imgcaption>  
  
The tiles displayed using the manipulated savestate are in the same order as they are stored in the *.tims within the worldx.bmf containers (see the 2 images above). Judging from these experiments, the game seems to use sequential numbering for the tiles in the worldx.bmf containers. The black area on position 00 in the decompressed terrain datafile occurs in the live game as well on position 00, so we can infer that these black areas may be intentional and are most probably not caused by the decompression script. This also confirms that the game uses tiles from world0.bmf for Arcanus. 

#### 6.3. Uncovering the fog of war/"visibility map"... 
...or had I known that earlier.
While searching through no$psx savestates of Civizard for clues to the terrain tiles, their associated CLUTS and the possible location of the game map for sequential tile injection [vervalkon](https://github.com/vervalkon) discovered the "visibility map". Somewhere around the 0x1FEC60 range onwards there is an array of bytes that determine the fog of war. Positions with 00 appear to be unseen, and that small bubble of different numbers showing below is the visibility map in the beginning of a new map/game.  

<p align="center">
  <img alt="game map" src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/d2dc7a4d-432d-4c44-9fc8-2bde92cd3f34">
  <br>
    <b>Visibility bubble at start of a new game</b>
</p>  

It is probably bitwise but it's obvious that 01 is a topright corner, 02 a bottom right one, 04 a bottom left, 08 a top left, etc. (see pic below).  
![fow2](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/bbd9ef48-3673-48c5-8888-68abc6e79274)  
<b>Visibility bubble large</b>  


As can be inferred by comparing the emulator view to the visibility map, 0F must be the "fully visible" index. To uncover the full map, one just has to fill everything in this area with 0Fs and load it back in the emulator.  


<p align="center">
  <img alt="Fow 3" src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c737894d-de31-44aa-a2e3-f76325d49b7e">
  <br>
    <b>Fog of war lifted.</b>
</p>  

Explanation:
The fog of war map/visibility map is a 2-dimensional array that is of unknown size - a "good amount" of 0Fs was pasted over the 00s. If the amount was too small, it all would not be visible, if it was too large, some other important data might have been overwritten.
Before a frame is shown, the game reads the map data and draws the full map. Once it has drawn the full map, it reads the fog data from RAM and draws the fog over it. It knows what kind of a fog pattern to make by reading the area around the 1FEC6C range (not 100% sure of the precise address). It determines the fog status likely by reading bits. Possible values are in binary. There is a logic here - think of the bits as checkboxes that determine the fog patterns on different corners of the position as shown in the picture below.  

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/3d027068-df2b-4d63-88a4-e14b606d5193" alt="drawing" width="300"/>   

<b>Possible values in binary; Numbers represent fog patterns; Arrows represent corners.</b>   

One bit represents one corner state. Think of bit 0 as "fogged" and bit 1 as "shown". 
byte 00 (which is 0000 in binary) means fog all corner, thus any byte in the fog map that is 00 is fogged. 
byte 0F is 1111 in binary, so all corners are "set" so to speak.  
Example: 0E is the cornerpiece in the bottom left of the spotlight of the initial map state, and unsurprisingly it has only one bit as 0.  

#### 6.4. Alternative way of determining the correct CLUT of a tile
So you have either dumped some sheets from VRAM via the methods in described in section 3 and these sheets are in different CLUTS or you were able to decompress worldx.bmf and are able to select a CLUT from a palette file as described in section 4. Most of these tiles look wrong and the longer you look at these the more unsure you are which CLUT looks "correct". There is a way of determining which CLUT to choose that works for single tiles.   
First start Civizard in No$PSX and start a game or load a game. In the overworld map pause the emulation by clicking on the debugger window (the one with the file menu) and start the VRAM viewer by pushing F5.
You can see the stopped game, the loaded tilesets, some text on the top right and a little window with small tiles below that on the right.
Clicking on "Quadtexraw" in the window will select tiles in the game window. Click through the different "Quadtexraw" lines until the tile you would like to know the palette is marked with a red square in the game window.
Then the window down right will display how the tile sheet that contains the tile in question should look like (or what it will look like with the correct CLUT/palette for that particular tile). For more information and a more in-depth technical method see "Tutorial - How to find PSX palettes" from section "Further information".  

![finding CLUTs with No$PSX](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/d5f4de0e-4732-4fc2-bb3a-f65baa449973)  
<b>Terrain tile, corresponding "QuadTexRaw" line and sheet of tiles in the CLUT the tile in question uses.</b>     

Click through the different CLUTs on the right (one line of colored squares is one CLUT, to skip go to next line). This will get you to the right CLUT and to the following following familiar image.
![middle correct tiles](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/9b53760a-cbd9-498d-8268-791067f223b4)
<b>Correct CLUT for group of tiles found.</b>  
 
#### 6.5. Civizard music tracks - an alternate version of the Master of Magic tracks
Civizard has the same tracks as Master of Magic DOS but the devs seem to have ran them on a different midi module and recorded them onto the CD. The instruments sound different and provide an interesting alternate version of the iconic tracks to those used for the newer Master of Magic for Windows. Unfortunately the Civizard tracks have a bad echo to them and are distorted at times. In theory, they could be run through some post-processing software and be used in a mod for Master of Magic. But this would be for someone else to try.
They can be read and exported with the tool jpsxdec. 

jpsxdec: https://github.com/m35/jpsxdec

#### WIP 6.6. Civizard text data - a preliminary exploration into translation
As far as we can tell, there is no English version or fan translation of Civizard. One can of course use translation aids such as google lens and people who have played Master of Magic before will feel right at home.  
That is no substitute for a real translation. Especially if the translated text is already available via Master of Magic for DOS.  
While brainstorming on the texture decompression script, we got talking about other aspects of the game such as the fact that there is no translation and had a look into where the text could be stored.  
A cursory look at the executable of Civizard revealed English text strings inside; which is curious, since while some UI elements are in English, these strings appear in Japanese ingame.  
  
![EXE strings of text data](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/0296f06d-ea49-4102-b608-644ca530a503)  
<b>Text strings of Civizard's "wizards.exe".</b>  

So vervalkon had a deeper look into the text composition algorithm and it is actually very involved. The game does not just load character glyphs from a VRAM page and paste the characters one by one, but actually types the entire sentence to RAM and then copies the precomposed text to VRAM. This is complex and one could argue unnecessary but interesting nonetheless. 
I went through the so far decompressed BMF files with XnViewMP's thumbnail view for folders and found this:  
![japanese from bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c0590f80-1252-4072-8ed4-6e7185c3a333)   
<b>Japanese characters from GRPH/main/00058943.tim.</b>  

While promising, this was not the right file. These glyphs are 8x8 pixels. The game uses 12x12 glyphs for most text, sometimes even 16x16. So this is a font, but not THE font. There are multiple fonts, it seems. The one in the image above is only one of them. Unfortunately, the font file in question is inside a BMF that cannot be uncompressed as of yet. So either this may have to wait until we can fully decompress every BMF file, or maybe we can get at this from another angle. So, back to the methods from the VERY beginning of this jouney: The VRAM dumps with Retroarch. Looking through the images we got from there, we found curious images of Japanese text and the following suspicious text graphics file was among them.  

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/ec8f1a76-ffd6-441e-9963-cd754538bfa4" alt="drawing" width="500"/>  

<b>Graphics file with text orderes characters for hiragana, katakana and western letters from Civizard.</b>  

In the texts of Civizard, several systems of characters can be used: Hiragana, Katakana, Kanji, letters of the western/Latin alphabet, and western numerals. So maybe this is the font file or part of the font we are searching for. We can determine the file contains Hiragana, Katakana, western letters in the expected order, only some Kanji, and special symbols such as cursor arrows; most Kanji and all western numerals are missing. The file's characters have the right size, so this looked promising. If this is indeed the font image, the game most likely picks the characters from the file and puts them into texts such as the one at the end of this section. 
What is missing are the Kanji. So I ran the game again (in Duckstation, another PSX emulator with debug features) and had a look at exactly when that file is used, and if there are hints to the Kanjis.  
Unfortunately for our project, this was a dead end again. The suspected font file matches the screen where you choose your magician's name almost exactly. So we can conclude this is not a font file but text created with the font.  

![no font](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/66acb733-f027-4a0a-a423-0dfe785ff757)  
<b>Font file or not? This is from the very start of the game and looks suspiciously like the suspected font file.</b>  

On to the second text we found in our VRAM dumps (see image below). According to Google Lens, the Kanji there seem to describe units, buildings and the like. Unfortunately the machine translation is very rough and neither of us is proficient in Japanese, so we have to wait until we can dive a deeper into this and also get confirmation from a Japanese speaker. There are repeated characters and a mix of different character systems (Kanji, Hiragana, Katakana, western numbers). It is unlikely that this is another font file since some characters are repeated, the text is narrower than in the small font files we found so far, not ordered, and not complete. From further tests with No$PSX VRAM debugger, we can say, that most test that is on screen is can be found on one page of characters in VRAM (some, but not many, characters are natively on tile sheets). The first pic above and the one below are examples for this where every text element is just on these sheets in the order they appear on screen from top to bottom.   
All in all this did not lead to the font files but we now have an idea what the font file should contain and how it should look like. We will know more after decompressing all the bmf files so we can have a look for a file with the Kanji.   

<img src="https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/e1dd215f-58aa-4cf1-8149-0b527d99b881" alt="drawing" width="500" />    

<b>Text saved from VRAM with Retroarch.</b>   

So we now have one of the font files from a decompressed BMF file, some strings from Civizard's executable ("Wizards.exe") and a cursory look at the game's text composition algorithm. 
Let us see if we find more in the future.  

Duckstation PSX Emulator: https://www.duckstation.org/  
XnViewMP Image Viewer (tim files as thumbnails in folders; cannot easily flip through CLUTs): https://www.xnview.com  
No$PSX Emulator/Debugger: https://problemkaputt.de/psx.htm  

#### 6.7. Palettes
Palettes in Civizard are used to show your flag color on your units or to to be able to used differently coloured fonts. Icons, buildings and battle screen tiles are also palettized.
A special case are the terrain files. As discussed before, with when it comes to the terrain tiles, palettes are heavily used to optimize for the psx's comparatively limited resources in that you have one master file for the image data (the tiles, so to speak) of each, Arcanus and Myror. Depending on the chosen palette, different subsets of tiles "look correct". Palettes are also heavily used for colour cycling animations and other graphical effects.

![Palette 00000040 world0.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/e702fb1a-058f-48c4-b68c-c597f5032546)  
<b>Palette 00000040 world0.bmf</b>  
![Palette 00000572 world0.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/335bc467-d8b8-40a0-a831-09b6323ebe77)  
<b>Palette 00000572 world0.bmf</b>  
![Palette 00001104 world0.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/ada026f5-1d37-4aba-a7c6-4f2a4ed35a9f)  
<b>Palette 00001104 world0.bmf</b>  
![Palette 00009852 world0.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/1cf5f2c5-1d68-46cf-a026-e3cbf2ecfa77)  
<b>Palette 00009852 world0.bmf</b>  
![Palette 00000040 world1.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/afc473fc-a581-40dc-8ea1-d792a018803d)  
<b>Palette 00000040 world1.bmf</b>  
![Palette 00000572 world1.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/c151d78c-3282-4475-ad23-b91b3c8ffd31)  
<b>Palette 00000572 world1.bmf</b>  
![Palette 00001104 world1.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/9fc7f249-1951-450d-8309-a3c0d0bba9db)  
<b>Palette 00001104 world1.bmf</b>  
![Palette 00009852 world1.bmf](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/0f7fc3cc-9cec-4b5f-8215-93ab461d9be9)  
<b>Palette 00009852 world1.bmf</b>  

#### 7. TODO/further ideas/observations:
+ It might be interesting to find out the layout of the BMF container. The order in which the script produces the different files might give us some clues there since the script starts at the first byte and proceeds to work through the file in order, so the first file produced is probably the first file in the BMF file. It is peculiar that it first produces 3 CLUT files in ascending names (lower numbers first), then a TIM file with landmarks (higher number than the CLUTs), then another CLUT file (name still ascending compared to the other 3 CLUTs), then 4 files that can be combined to one file containing the tiles, also in alphabetically ascending order. For both world0 and world0, 3 CLUTs are recognized as 16x16 colour CLUT files by tim2view (one as a 256x1 CLUT file (world0:00001104.bin, world1:00000572.bin), which may point to some irregularities during decompression. (to check... does the script number them by address or the like?)
+ There are 110 black/transparent tiles out of 880 tiles in the world0 and world1 tileset. They are there deliberately and are no error as can be seen in the sequential tiles injection test where they are present and can be called upon by calling them ingame via savestate editing. It would be interesting find out what they are for.  
+ Figuring out the internal game logic with the new information on the CLUT files might be an a cool project for interested parties. We already started looking into the CLUT handling of the executable.   
![CLUT handling of the game](https://github.com/starwisp/Civizard-tileset-archeology/assets/4465384/f7e220e6-1bdd-4ac3-bd9b-2e368912415b)  
<b>Possible hints for the internal CLUT handling of the game</b>        

#### 8. TL;DR Civizard Tileset Extraction  

...though reading the document above is highly recommended for better unterstanding

- put all folders found in the root directory of your Civizard CD into C:\civizard
- download and execute Python script "BMFtool 1.1" from above  
- the script will search for and extract graphics data in *.bmf-files and put it into an automatically created c:\bmfout
- recognized graphics data will be in the PSX image format *.tim. Use a *.tim viewer like XnViewMP or tim2view to view/export
- most folders will contain sheets with animation phases, icons, wizard portraits and the like   
- the terrain tileset data will be in c:\bmfout\grph\world0 and world1 
- world0 and world1 will each contain a *.tim file for landmarks, one larger *.bin file ("compressedworld.bin") for the terrain tileset data and four smaller *.bin files for its palettes/CLUTs
- download LunarIPS and download the IPS-patches in this repo (extract with 7zip)
- apply IPS-patches to respective terrain tileset graphics data *.bin-file. 
- use TiledGGD-PE to combine terrain graphics data (compressedworld.bin) and palette files (for correct settings read paragraphs 4.3 - 4.7 above) and save the tileset in the desired palette (TiledGGD-PE menu "save all graphics"). Caveat: TiledGGD-PE may crash when entering these settings, especially after entering the tile dimensions. In case this happens, just try again until it works.

Tim2View (can easily flip through palettes): https://github.com/lab313ru/tim2view/releases/tag/r90  
XnViewMP Image Viewer (shows *.tim files as thumbnails in folders, better for skimming through folders; cannot easily flip through palettes): https://www.xnview.com  
LunarIPS: https://www.romhacking.net/utilities/240/    
TiledGGD-PE-: https://github.com/puggsoy/tiledggd-pe-  

#### 9. Verification of tileset by comparing to ingame or video

Each part of the terrain tile set (world0 and world1) has multiple possible palettes. Some only differ in a couple of colors. Finding the right palette for every tile without knowing the game's palette assignment logic is manual work.
In order to make this easier we provide some help here with a memory card image of a 100 percent opened map and a video showing it in action recorded with Duckstation.  

![Overview of a game map with all the terrain tiles revealed](https://img.youtube.com/vi/TKQ9TX16uPI/0.jpg)]  
<b>https://www.youtube.com/watch?v=TKQ9TX16uPI</b>  
<b>Click on the video link. Embedding does not work in Github readmes</b>  


_________
### Acknowledgments
[vervalkon](https://github.com/vervalkon) for his invaluable technical knowledge and for writing the extraction script in the repository, all the helpful people of the "DYKG / Do you know Gaming" Discord channel (@darkwolf, @R7CrazyCanucks, etc.),"Master of Magic Fans" Discord channel (@blakessanctum for coming up with the idea of using the Civizard tileset for Master of Magic, [jimbalcomb](https://github.com/jbalcomb) for technical information on Master of Magic).  
Suppanut for figuring out the correct palettes for the terrain tiles and which palettes are used in terrain tileset color cycling animations. Also for his [Caster of Magic for Windows Warlord](https://www.moddb.com/mods/caster-of-magic-for-windows-warlord) mod which enhances the original Master of Magic with many more options.  
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
+ Example of color cycling (click "show options") http://www.effectgames.com/demos/canvascycle/
+ Article on color cycling http://www.effectgames.com/effect/article-Old_School_Color_Cycling_with_HTML5.html
+ Wikipedia entry on color cycling https://en.wikipedia.org/wiki/Color_cycling  
+ Color cycling information - GDC 2016 Talk "8 Bit & '8 Bitish' Graphics-Outside the Box" by Mark Ferrari https://www.youtube.com/watch?v=aMcJ1Jvtef0
+ Technical information on the tim format https://web.archive.org/web/20230702165945/https://rsync.irixnet.org/tutorials/pstutorials/chapter1/3-textures.html or http://lameguy64.net/tutorials/pstutorials/chapter1/3-textures.html
+ Visualized technical information on the tim format from 5:00 onward https://www.youtube.com/watch?v=Nq5rTECKb_w  

