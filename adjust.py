# Bomberman TSA ROM Adjuster
import subprocess
import os
import sys
#import easygui
import shutil
import random
import pkgutil

import tkinter as tk
from tkinter import filedialog

import logging

from .gamemaps import ADJUST_OFFSET

logger = logging.getLogger("Client")

#patch_bytes = pkgutil.get_data(__name__, f"data/patches/{map_name}.ips")
def getRomPath():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rompath = filedialog.askopenfilename(
        title="Select the Archipelago Patched ROM for adjustments",
        filetypes=(("N64 ROM Image", "*.z64"), ("All files", "*.*")),
        initialdir=script_dir
    )
    #splitpath = rompath.split("/")

    return rompath

def getdatafile(filename, dirpath):
    file_bytes = pkgutil.get_data(__name__, f"data/{filename}")
    with open(f"{dirpath}/{filename}", "wb") as file:
        file.write(file_bytes)
        #file.close()

def getassetpath(workdir):
    rootpath = f"{workdir}/unpacked/"
    assetpath = "assets/"
    return rootpath+assetpath

def decompress_rom(romFile, workdir):
    if not os.path.exists(workdir):
        os.makedirs(workdir)
    getdatafile("pack.exe", workdir)
    getdatafile("baku2.us.bin", workdir)
    replacementpath = f"{workdir}/replace/"
    if not os.path.exists(replacementpath):
        os.makedirs(replacementpath)
        getdatafile("736.bin", replacementpath)
        getdatafile("737.bin", replacementpath)
        getdatafile("738.bin", replacementpath)
    unpackpath = f"{workdir}/unpacked/"
    if not os.path.exists(unpackpath):
        os.makedirs(unpackpath)
    logger.warning(f"Unpacking ROM for adjustments")
    subprocess.check_call([rf"{workdir}/pack.exe", "d", f"{workdir}/baku2.us.bin", romFile, f"{unpackpath}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def compress_rom(romFile, workdir):
    #outsplit = romFile.split(".")[0]
    #outfile = outsplit+"out.z64"
    logger.warning(f"Repacking ROM with adjustments")
    subprocess.check_call([rf"{workdir}/pack.exe", "e", f"{workdir}/baku2.us.bin", romFile, f"{workdir}/unpacked"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logger.warning(f"ROM has been adjusted, please open the ROM for changes.")
    shutil.rmtree(workdir, ignore_errors=False, onerror=None)
    if os.path.exists("temp/"):
        shutil.rmtree("temp/", ignore_errors=False, onerror=None)
    with open(romFile, "r+b") as file:
        file.seek(0x99FDA)
        file.write(b'\x01')
        file.seek(ADJUST_OFFSET)
        file.write(b'\x01')

def copy_and_replace(source_path, destination_path):
    if source_path != destination_path:
        if os.path.exists(destination_path):
            os.remove(destination_path)
        shutil.copy2(source_path, destination_path)

def process_shuffles(workdir):
    symbol_list = {
        "White Bomber":"912.bin",
        "Filled heart":"905.bin",
        "Empty heart":"906.bin",
        "Remote Control":"907.bin",
        "Fire level":"908.bin",
        "Bomb level":"909.bin",
        "Fire Stone":"90a.bin",
        "Water Stone":"90b.bin",
        "Wind Stone":"90c.bin",
        "Earth Stone":"90d.bin",
        "Lightning Stone":"90e.bin",
        "Light Stone":"90f.bin",
        "Shadow Stone":"910.bin",
        "Gold":"911.bin",
    }
    filelist_shuffle(symbol_list, workdir)

def process_powerup(workdir):
    replacementpath = f"{workdir}/replace/"
    replacearray = [
        "736.bin","737.bin","738.bin"
    ]
    assetbasepath = getassetpath(workdir)
    for file in replacearray:
        if os.path.exists(replacementpath+file):
            copy_and_replace(replacementpath+file, assetbasepath+file)
        else:
            print("File "+file+" not found.")

def process_doors(workdir):
    door_map = {
        "822.bin": 0x8C, #Neverland, Entry Point
        "823.bin": 0x8C, #Neverland, Bonus Room
        "824.bin": 0x8C, #Neverland, Through the Line of Fire
        "825.bin": 0x8C, #Neverland, Intersection
        "826.bin": 0x8C, #Neverland, Conveyor Belts
        "827.bin": 0x8C, #Neverland, Potholes
        "828.bin": 0x8C, #0x183, #Neverland, Carrier Works
        "829.bin": 0x8C, #0x183, #Neverland, Switch Room
        "82a.bin": 0x8C, #Neverland, Bridge Room
        "82b.bin": 0x8C, #Neverland, Cage Room
        "82c.bin": 0xB0, #Neverland, Safe Point
        "82d.bin": 0xB0, #Neverland, Underground Corridor
        "82e.bin": 0xB0, #Neverland, Warehousing
        "82f.bin": 0xB0, #Neverland, Furnace
        "830.bin": 0xB0, #Neverland, First Passageway
        "831.bin": 0xB0, #Neverland, Second Passageway
        "832.bin": 0xB0, #Neverland, Landing Point
        "833.bin": 0xB0, #Neverland, Third Passageway
        "834.bin": 0xB0, #Neverland, Gravity Generator Room
        "835.bin": 0x89, #Aquanet, Around the Moat (Starting Point)
        "836.bin": 0x89, #Aquanet, First Room
        "837.bin": 0x89, #Aquanet, Second Room
        "838.bin": 0x89, #Aquanet, Third Room
        "839.bin": 0x89, #Aquanet, Swimming Pool Spa
        "83a.bin": 0x89, #Aquanet, Behind the Moat
        "83b.bin": 0x89, #Aquanet, Beyond the Moat
        "83c.bin": 0x89, #Aquanet, Elevator Hub
        "83d.bin": 0x89, #Aquanet, Hidden Balcony
        "83e.bin": 0x89, #Aquanet, Water Channels
        "83f.bin": 0x89, #Aquanet, Fountain Room
        "840.bin": 0x89, #Aquanet, Secret Room 3
        "841.bin": 0x89, #Aquanet, Elevator Stopping Point
        "842.bin": 0xAD, #Aquanet, Behemos' Lair
        "843.bin": 0xAD, #Aquanet, To the Tower
        "844.bin": 0xAD, #Aquanet, Tower 1F
        "845.bin": 0xAD, #Aquanet, Tower 2F
        "846.bin": 0xAD, #Aquanet, Tower 3F
        "847.bin": 0xAD, #Aquanet, Gravity Generator Room
        "848.bin": 0x88, #Alcatraz, Prison
        "849.bin": 0x88, #Alcatraz, Sewer Entrance
        "84a.bin": 0x88, #Alcatraz, Twisted Sewers
        "84b.bin": 0x88, #Alcatraz, Security Room A
        "84c.bin": 0x88, #Alcatraz, Security Room B
        "84d.bin": 0x88, #Alcatraz, Sewage Disposal
        "84e.bin": 0xAC, #Alcatraz, Through the Pipe
        "84f.bin": 0xAC, #Alcatraz, Prison Bridge
        "850.bin": 0xAC, #Alcatraz, Pipe Room A
        "851.bin": 0xAC, #Alcatraz, Pipe Room B
        "852.bin": 0xAC, #Alcatraz, Final Defense Unit
        "853.bin": 0xAC, #Alcatraz, Gravity Generator Room
        "854.bin": 0x8A, #Horizon, First Intersection
        "855.bin": 0x8A, #Horizon, Eastern Tower
        "856.bin": 0x8A, #Horizon, Push-Block Trial
        "857.bin": 0x8A, #Horizon, Leading Road
        "858.bin": 0x8A, #Horizon, First Trial
        "859.bin": 0x8A, #Horizon, Second Trial
        "85a.bin": 0x8A, #Horizon, Resting Point
        "85b.bin": 0xAE, #Horizon, Floating Temple (Second Intersection)
        "85c.bin": 0xAE, #Horizon, Twin Bridges
        "85d.bin": 0xAE, #Horizon, Final Deposit
        "85e.bin": 0xAE, #Horizon, Last Route
        "85f.bin": 0xAE, #Horizon, Fourth Trial
        "860.bin": 0xAE, #Horizon, Secret Room 1
        "861.bin": 0xAE, #Horizon, Secret Room 2
        "862.bin": 0xAE, #Horizon, Third Trial
        "863.bin": 0xAE, #Horizon, Last Trial
        "864.bin": 0xAE, #Horizon, Gravity Generator Room
        "865.bin": 0x8B, #Starlight, Parking Lot
        "866.bin": 0x8B, #Starlight, Closed Road
        "867.bin": 0x8B, #Starlight, Fountain Square
        "868.bin": 0x8B, #Starlight, Small Inlet
        "869.bin": 0x8B, #Starlight, Alleyway
        #"86a.bin": 0x8B, #Starlight, Casino Entrance ;[Despawns Elevator]
        "86b.bin": 0x8B, #Starlight, Casino Lobby
        "86c.bin": 0x8B, #Starlight, Betting Room
        "86d.bin": 0x8B, #Starlight, Slots Room
        "86e.bin": 0x8B, #Starlight, Waiting Room
        "86f.bin": 0x8B, #Starlight, Stage Area
        "870.bin": 0xAF, #Starlight, Lookout Point
        "871.bin": 0xAF, #Starlight, Wheel of Fortune
        "872.bin": 0xAF, #Starlight, Gravity Generator Room
        "873.bin": 0x8D, #Epikyur, Entrance
        "874.bin": 0x8D, #Epikyur, Center Fountain
        "875.bin": 0x8D, #Epikyur, Tattered Bridge
        "876.bin": 0x8D, #Epikyur, Misaligned Bridge
        "877.bin": 0x8D, #Epikyur, Haunted House (Yard)
        "878.bin": 0x8D, #Epikyur, Haunted House (Lobby)
        "879.bin": 0x8D, #Epikyur, Haunted House (Spike Traps)
        "87a.bin": 0x8D, #Epikyur, Haunted House (Mirror Room)
        "87b.bin": 0x8D, #Epikyur, Haunted House (Spike Pit)
        "87c.bin": 0x8D, #Epikyur, Haunted House (Storeroom)
        "87d.bin": 0x8D, #Epikyur, History Museum (Prehistoric Puzzle)
        "87e.bin": 0x8D, #Epikyur, History Museum (Military Puzzle)
        "87f.bin": 0x8D, #Epikyur, History Museum (Showcase Room)
        "880.bin": 0xB1, #Epikyur, Castle of Time (First Room)
        "881.bin": 0xB1, #Epikyur, Castle of Time (Second Room)
        "882.bin": 0x8D, #Epikyur, Coaster Body 1
        "883.bin": 0x8D, #Epikyur, Haunted House (Coaster Start)
        "884.bin": 0x8D, #Epikyur, Coaster Body 2
        "885.bin": 0x8D, #Epikyur, Coaster Finish
        "886.bin": 0xB1, #Epikyur, Gravity Generator Room
        "887.bin": 0x8E, #Thantos, Starting Point
        "888.bin": 0x8E, #Thantos, Streets
        "889.bin": 0x8E, #Thantos, Up the Ladder
        "88a.bin": 0x8E, #Thantos, Wrecked Lot
        "88b.bin": 0x8E, #Thantos, Battery Ambush
        #"88c.bin": 0x8E, #Thantos, Battle for the Battery; [Breaks]
        "88d.bin": 0x8E, #Thantos, Compactor (Secret Room 2)
        "88e.bin": 0x8E, #Thantos, Subway Entrance
        "88f.bin": 0x8E, #Thantos, Aboard the Subway
        "890.bin": 0x8E, #Thantos, Subway Destination
        "891.bin": 0x8E, #Thantos, Supposed Dead End
        "892.bin": 0x8E, #Thantos, The Crevice
        "893.bin": 0x8E, #Thantos, Voltage Storage Unit
        "894.bin": 0x8E, #Thantos, Secret Room 3
        "895.bin": 0x8E, #Thantos, Hangout
        "896.bin": 0x8E, #Thantos, Secret Room 1
        "897.bin": 0x8E, #Thantos, Back Alley
        "898.bin": 0x8E, #Thantos, Hidden Territory
        "899.bin": 0x8E, #Thantos, Gravity Generator Room
    }
    if not os.path.exists("temp"):
        os.makedirs("temp")
    for mapfile, flag in door_map.items():
        process_map_file(mapfile,flag, workdir)
    

def filelist_shuffle(filelist, workdir):
    assetbasepath = getassetpath(workdir)
    temppath = "temp/"
    if not os.path.exists("temp"):
        os.makedirs("temp")
    newlist = list(filelist.values())
    joinedlist = {}
    for file, path in filelist.items():
        joinedlist[path] = path
        shutil.copy2(assetbasepath+path, temppath+path)
    random.shuffle(newlist)
    outlist = dict(zip(joinedlist, newlist))
    for sourcefile, destfile in outlist.items():
        copy_and_replace(temppath+sourcefile, assetbasepath+destfile)

def process_map_file(filepath,setflag, workdir):
    temppath = "temp/"
    assetbasepath = getassetpath(workdir)
    shutil.copy2(assetbasepath+filepath, temppath+filepath)
    reafilepath = assetbasepath+filepath
    workfile = temppath+filepath
    base_offset = 0
    entry_total = 0
    with open(reafilepath, "rb") as f_read:
        f_read.seek(0xB)
        set_count = int.from_bytes(f_read.read(1))
        base_offset = (set_count * 0x20) + 0x10
        f_read.seek(0xF)
        entry_total = int.from_bytes(f_read.read(1))
        f_read.seek(base_offset)
        with open(workfile, 'r+b') as f_write:
            for mapobj in range(entry_total):
                objoffset = (mapobj * 0x4C) + base_offset
                triggeroffset = objoffset + 0x13
                f_read.seek(triggeroffset)
                if f_read.read(1) == b'\x01':
                    despawn_type = objoffset + 0x1B
                    flag_offset = objoffset + 0x1E
                    clear_offset = flag_offset +2
                    f_write.seek(despawn_type)
                    f_write.write(b'\x02')
                    f_write.seek(flag_offset)
                    f_write.write( setflag.to_bytes(2, 'big') )
                    f_write.seek(clear_offset)
                    f_write.write(bytearray([0xFF,0xFF,0xFF,0xFF]))
                else:
                    continue
        
    copy_and_replace(temppath+filepath, assetbasepath+filepath)
    return

def replace_files(charafile,head,body,arm,leg, workdir):
    assetbasepath = getassetpath(workdir)
    bomberchara = "17e.bin"
    guardhead = "3e7.bin"
    guardbody = "3e8.bin"
    guardarm = "3e9.bin"
    guardleg = "3ea.bin"
    copy_and_replace(assetbasepath+charafile, assetbasepath+bomberchara)
    if head == "None":
        copy_and_replace(assetbasepath+charafile, assetbasepath+guardhead)
    else:
        copy_and_replace(assetbasepath+head, assetbasepath+guardhead)
    
    if body == "None":
        copy_and_replace(assetbasepath+charafile, assetbasepath+guardbody)
    else:
        copy_and_replace(assetbasepath+body, assetbasepath+guardbody)
    
    if arm == "None":
        copy_and_replace(assetbasepath+charafile, assetbasepath+guardarm)
    else:
        copy_and_replace(assetbasepath+arm, assetbasepath+guardarm)
    
    if leg == "None":
        copy_and_replace(assetbasepath+charafile, assetbasepath+guardleg)
    else:
        copy_and_replace(assetbasepath+leg, assetbasepath+guardleg)

def adjust_rom(adjust_data):
    adjust_list = []
    adjust_flags = adjust_data[0]
    if adjust_flags & 0x1 == 0:
        try:
            for adj_offset in range(0x10, ((0x8 * 0x5) + 0x10), 0x8):
                ascii_values = ''.join(chr(b) for b in adjust_data[adj_offset:adj_offset+0x8] if 32 <= b < 128)
                adjust_list.append(ascii_values)

            romFile = getRomPath()
            home_dir = os.path.expanduser("~")
            documents_path = os.path.join(home_dir, "Documents")
            workdir = f"{documents_path}/ap_temp"
            decompress_rom(romFile, workdir)
            replace_files(adjust_list[0],adjust_list[1],adjust_list[2],adjust_list[3],adjust_list[4],workdir)
            #process_shuffles()
            process_doors(workdir)
            process_powerup(workdir)
            compress_rom(romFile, workdir)
            return 1
        except Exception as e:
            logger.warning(f"Rom Adjuster failed {e}")
            return 0
    else: 
        return 1
