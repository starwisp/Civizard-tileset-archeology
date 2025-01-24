import sys, os, struct

# Put directories from root of your Civizard CD into c:/civizard. -sw

flist = ["COMB/COMBAT.BMF",
"COMB/COMBAT0.BMF",
"COMB/COMBAT1.BMF",
"COMB/COMBAT2.BMF",
"COMB/COMBAT3.BMF",
"COMB/COMBAT4.BMF",
"COMB/COMBAT5.BMF",
"COMB/COMBAT6.BMF",
"COMB/COMBAT7.BMF",
"COMB/COMBAT10.BMF",
"COMB/COMBAT11.BMF",
"COMB/COMBAT12.BMF",
"COMB/COMBAT13.BMF",
"COMB/COMBAT14.BMF",
"COMB/COMBAT15.BMF",
"COMB/COMBAT16.BMF",
"COMB/COMBAT17.BMF",
"GRPH/BUILD.BMF",
"GRPH/CEFFECT.BMF",
"GRPH/EMBASSY.BMF",
"GRPH/EVENT.BMF",
"GRPH/LAIR.BMF",
"GRPH/LOADGAME.BMF",
"GRPH/MAGIC.BMF",
"GRPH/MAIN.BMF",
"GRPH/NEWGAME.BMF",
"GRPH/NOTIFY.BMF",
"GRPH/POWERON.BMF",
"GRPH/SPELL.BMF",
"GRPH/SWIZARD.BMF",
"GRPH/TITLE.BMF",
"GRPH/WIZARD.BMF",
"GRPH/WIZARD2.BMF",
"GRPH/WIZLAB.BMF",
"GRPH/WORLD0.BMF",
"GRPH/WORLD1.BMF",
"GRPH/WORLDMAP.BMF",
"MONST/0/00.BMF",
"MONST/0/01.BMF",
"MONST/0/02.BMF",
"MONST/0/03.BMF",
"MONST/0/04.BMF",
"MONST/0/05.BMF",
"MONST/0/06.BMF",
"MONST/0/07.BMF",
"MONST/0/08.BMF",
"MONST/0/09.BMF",
"MONST/0/10.BMF",
"MONST/0/11.BMF",
"MONST/0/12.BMF",
"MONST/0/13.BMF",
"MONST/0/14.BMF",
"MONST/0/15.BMF",
"MONST/0/16.BMF",
"MONST/0/17.BMF",
"MONST/0/18.BMF",
"MONST/0/19.BMF",
"MONST/0/20.BMF",
"MONST/0/21.BMF",
"MONST/0/22.BMF",
"MONST/0/23.BMF",
"MONST/0/24.BMF",
"MONST/1/25.BMF",
"MONST/1/26.BMF",
"MONST/1/27.BMF",
"MONST/1/28.BMF",
"MONST/1/29.BMF",
"MONST/1/30.BMF",
"MONST/1/31.BMF",
"MONST/1/32.BMF",
"MONST/1/33.BMF",
"MONST/1/34.BMF",
"MONST/1/35.BMF",
"MONST/1/36.BMF",
"MONST/1/37.BMF",
"MONST/1/38.BMF",
"MONST/1/39.BMF",
"MONST/1/40.BMF",
"MONST/1/41.BMF",
"MONST/1/42.BMF",
"MONST/1/43.BMF",
"MONST/1/44.BMF",
"MONST/1/45.BMF",
"MONST/1/46.BMF",
"MONST/1/47.BMF",
"MONST/1/48.BMF",
"MONST/1/49.BMF",
"MONST/2/50.BMF",
"MONST/2/51.BMF",
"MONST/2/52.BMF",
"MONST/2/53.BMF",
"MONST/2/54.BMF",
"MONST/2/55.BMF",
"MONST/2/56.BMF",
"MONST/2/57.BMF",
"MONST/2/58.BMF",
"MONST/2/59.BMF",
"MONST/2/60.BMF",
"MONST/2/61.BMF",
"MONST/2/62.BMF",
"MONST/2/63.BMF",
"MONST/2/64.BMF",
"MONST/2/65.BMF",
"MONST/2/66.BMF",
"MONST/2/67.BMF",
"MONST/2/68.BMF",
"MONST/2/69.BMF",
"MONST/2/70.BMF",
"MONST/2/71.BMF",
"MONST/2/72.BMF",
"MONST/2/73.BMF",
"MONST/2/74.BMF",
"MONST/3/75.BMF",
"MONST/3/76.BMF",
"MONST/3/77.BMF",
"MONST/3/78.BMF",
"MONST/3/79.BMF",
"MONST/3/80.BMF",
"MONST/3/81.BMF",
"MONST/3/82.BMF",
"MONST/3/83.BMF",
"MONST/3/84.BMF",
"MONST/3/85.BMF",
"MONST/3/86.BMF",
"MONST/3/87.BMF",
"MONST/3/88.BMF",
"MONST/3/89.BMF",
"MONST/3/90.BMF",
"MONST/3/91.BMF",
"MONST/3/92.BMF",
"MONST/3/93.BMF",
"MONST/3/94.BMF",
"MONST/3/95.BMF",
"MONST/3/96.BMF",
"MONST/3/97.BMF",
"MONST/3/98.BMF",
"MONST/3/99.BMF",
"MONST/4/100.BMF",
"MONST/4/101.BMF",
"MONST/4/102.BMF",
"MONST/4/103.BMF",
"MONST/4/104.BMF",
"MONST/4/105.BMF",
"MONST/4/106.BMF",
"MONST/4/107.BMF",
"MONST/4/108.BMF",
"MONST/4/109.BMF",
"MONST/4/110.BMF",
"MONST/4/111.BMF",
"MONST/4/112.BMF",
"MONST/4/113.BMF",
"MONST/4/114.BMF",
"MONST/4/115.BMF",
"MONST/4/116.BMF",
"MONST/4/117.BMF",
"MONST/4/118.BMF",
"MONST/4/119.BMF",
"MONST/4/120.BMF",
"MONST/4/121.BMF",
"MONST/4/122.BMF",
"MONST/4/123.BMF",
"MONST/4/124.BMF",
"MONST/5/125.BMF",
"MONST/5/126.BMF",
"MONST/5/127.BMF",
"MONST/5/128.BMF",
"MONST/5/129.BMF",
"MONST/5/130.BMF",
"MONST/5/131.BMF",
"MONST/5/132.BMF",
"MONST/5/133.BMF",
"MONST/5/134.BMF",
"MONST/5/135.BMF",
"MONST/5/136.BMF",
"MONST/5/137.BMF",
"MONST/5/138.BMF",
"MONST/5/139.BMF",
"MONST/5/140.BMF",
"MONST/5/141.BMF",
"MONST/5/142.BMF",
"MONST/5/143.BMF",
"MONST/5/144.BMF",
"MONST/5/145.BMF",
"MONST/5/146.BMF",
"MONST/5/147.BMF",
"MONST/5/148.BMF",
"MONST/5/149.BMF",
"MONST/6/150.BMF",
"MONST/6/151.BMF",
"MONST/6/152.BMF",
"MONST/6/153.BMF",
"MONST/6/154.BMF",
"MONST/6/155.BMF",
"MONST/6/156.BMF",
"MONST/6/157.BMF",
"MONST/6/158.BMF",
"MONST/6/159.BMF",
"MONST/6/160.BMF",
"MONST/6/161.BMF",
"MONST/6/162.BMF",
"MONST/6/163.BMF",
"MONST/6/164.BMF",
"MONST/6/165.BMF",
"MONST/6/166.BMF",
"MONST/6/167.BMF",
"MONST/6/168.BMF",
"MONST/6/169.BMF",
"MONST/6/170.BMF",
"MONST/6/171.BMF",
"MONST/6/172.BMF",
"MONST/6/173.BMF",
"MONST/6/174.BMF",
"MONST/7/175.BMF",
"MONST/7/176.BMF",
"MONST/7/177.BMF",
"MONST/7/178.BMF",
"MONST/7/179.BMF",
"MONST/7/180.BMF",
"MONST/7/181.BMF",
"MONST/7/182.BMF",
"MONST/7/183.BMF",
"MONST/7/184.BMF",
"MONST/7/185.BMF",
"MONST/7/186.BMF",
"MONST/7/187.BMF",
"MONST/7/188.BMF",
"MONST/7/189.BMF",
"MONST/7/190.BMF",
"MONST/7/191.BMF",
"MONST/7/192.BMF",
"MONST/7/193.BMF",
"MONST/7/194.BMF",
"MONST/7/195.BMF",
"MONST/7/196.BMF",
"MONST/7/197.BMF",
"OVR/BUILDS.BMF",
"OVR/CARTG.BMF",
"OVR/DEAD.BMF",
"OVR/DIPLO.BMF",
"OVR/GEFFECT.BMF",
"OVR/HEROVIEW.BMF",
"OVR/HISTORY.BMF",
"OVR/LVUP.BMF",
"OVR/MEFFECT.BMF",
"OVR/MERCHANT.BMF",
"OVR/NAMEENT.BMF",
"OVR/RATIO.BMF",
"OVR/SETTING.BMF",
"OVR/SPELLMST.BMF",
"OVR/SPELLS.BMF",
"OVR/STSPLM.BMF",
"OVR/UNITVIEW.BMF",
"OVR/WIZSEL.BMF",
"OVR2/ARTIF.BMF",
"OVR2/ENDING.BMF",
"OVR2/LOSE.BMF",
"OVR2/SCORES.BMF",
"OVR2/WIN.BMF",
"SOUND/SOUND.BMF",
"SPEC0/0.BMF",
"SPEC0/1.BMF",
"SPEC0/2.BMF",
"SPEC0/3.BMF",
"SPEC0/4.BMF",
"SPEC0/5.BMF",
"SPEC0/6.BMF",
"SPEC0/7.BMF",
"SPEC0/8.BMF",
"SPEC0/9.BMF",
"SPEC0/10.BMF",
"SPEC0/11.BMF",
"SPEC0/12.BMF",
"SPEC0/13.BMF",
"SPEC0/14.BMF",
"SPEC0/15.BMF",
"SPEC1/16.BMF",
"SPEC1/17.BMF",
"SPEC1/18.BMF",
"SPEC1/19.BMF",
"SPEC1/20.BMF",
"SPEC1/21.BMF",
"SPEC1/22.BMF",
"SPEC1/23.BMF",
"SPEC1/24.BMF",
"SPEC1/25.BMF",
"SPEC1/26.BMF",
"SPEC1/27.BMF",
"SPEC1/28.BMF",
"SUMM/SUMMON0.BMF",
"SUMM/SUMMON1.BMF",
"SUMM/SUMMON2.BMF",
"SUMM/SUMMON3.BMF",
"SUMM/SUMMON4.BMF",
"SUMM/SUMMON5.BMF",
"SUMM/SUMMON10.BMF",
"SUMM/SUMMON11.BMF",
"SUMM/SUMMON12.BMF",
"SUMM/SUMMON13.BMF",
"SUMM/SUMMON14.BMF",
"SUMM/SUMMON15.BMF",
"SUMM/SUMMON16.BMF",
"WIZARDS/0.BMF",
"WIZARDS/1.BMF",
"WIZARDS/2.BMF",
"WIZARDS/3.BMF",
"WIZARDS/4.BMF",
"WIZARDS/5.BMF",
"WIZARDS/6.BMF",
"WIZARDS/7.BMF",
"WIZARDS/8.BMF",
"WIZARDS/9.BMF",
"WIZARDS/09.BMF",
"WIZARDS/10.BMF",
"WIZARDS/11.BMF",
"WIZARDS/12.BMF",
"WIZARDS/13.BMF"]

def mdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def bitmask(num):
    mask = format(num, '08b')
    inlist = list(mask)
    return list(map(lambda x: int(x), inlist))

def getB(rom, number=1):
    return int.from_bytes(rom.read(number), byteorder='little')

def rnd(num):
    return (num // 0x1000) << 12

pad = 0xFEE
trueroot = "c:/civizard/"
trueout = "c:/bmfout/"

for fidx in range(len(flist)):
    path = flist[fidx]
    folname = path.split("/")[-1].split(".")[0]
    parname = os.path.join(*path.split("/")[:-1])
    trueoutpathname = os.path.join(trueout, parname, folname)
    mdir(trueoutpathname)

    try:
        with open(os.path.join(trueroot, flist[fidx]), "rb") as rom:
            file_amount = getB(rom, 4)
            sizes = struct.unpack(f"{file_amount}I", rom.read(file_amount << 2))
            local_root = rom.tell()
            local_adrs = [local_root + sum(sizes[0:i]) for i in range(len(sizes))]

            for sub in range(file_amount):
                rom.seek(local_adrs[sub])
                sniffA, sniffB, sniffC = getB(rom, 4), getB(rom, 4), getB(rom, 4)

                # THE GUESSING GAME
                if sniffA == 0x00000010 and (sniffB & 0xFFFFFFF0 == 0):
                    extension = "TIM"
                    compr = 0
                elif sniffA > 0x00008000 and (sniffB & 0xFFFFFF00) == 0xF0EB1000:
                    extension = "tim"
                    compr = 1
                else:
                    extension = "bin"
                    compr = 0

                rom.seek(local_adrs[sub])

                output_path = os.path.join(trueoutpathname, f"{local_adrs[sub]:08d}.{extension}")
                print(output_path)

                with open(output_path, "wb+") as out:
                    if compr == 0:
                        out.write(rom.read(sizes[sub]))
                    else:
                        fsize = getB(rom, 4)
                        limit = fsize + pad
                        out.write(bytes([0] * pad))
                        while True:
                            ins = getB(rom)
                            blist = bitmask(ins)
                            while blist:
                                if blist.pop():
                                    byte = getB(rom)
                                    out.write(bytes([byte]))
                                else:
                                    word = getB(rom, 2)
                                    amount = 3 + ((word >> 8) & 0xF)
                                    prefix = word >> 12
                                    adress = (word & 0xFF) + (prefix << 8)

                                    for j in range(amount):
                                        rta = out.tell()
                                        root = rnd(out.tell())
                                        if root + adress + j > rta:
                                            root -= 0x1000
                                        out.seek(root + adress + j)
                                        byte = int.from_bytes(out.read(1), byteorder='little')
                                        out.seek(rta)
                                        out.write(bytes([byte]))
                                if out.tell() >= limit:
                                    break
                            if out.tell() >= limit:
                                break
                        out.seek(pad)
                        _ = out.read(fsize)
                        out.seek(0)
                        out.write(_)
                        out.seek(0)
                        out.truncate(fsize)
                        print(f"end at {rom.tell():X}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

# The script outputs the terrain tiles in 2x4 partial binary files. The following commands combine them via OS commands. This works in Windows and may not work in other OSes. Adjust accordingly. -sw
print('Creating terrain file WORLD0 (compressedworld0.bin).')
os.chdir('c:/bmfout/GRPH/WORLD0')
os.system('copy /b 00010384.bin+00067084.bin+00114376.bin+00150948.bin compressedworld0.bin')
os.system('del 00010384.bin')
os.system('del 00067084.bin')
os.system('del 00114376.bin')
os.system('del 00150948.bin')

print('Creating terrain file WORLD1 (compressedworld1.bin).')
os.chdir('c:/bmfout/GRPH/WORLD1')
os.system('copy /b 00010384.bin+00068968.bin+00119992.bin+00162648
