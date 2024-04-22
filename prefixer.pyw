import os, datetime, time, cv2 # os for rename / datetime for time in log / time for delayed start / cv2 to take photo
from glob import glob

######### EDIT FIELD #########

storeLocation: str = r'C:\folder\storage'   #For example: C:\folder\storage
targetFolder: str = r'C:\folder\storage'    #For example: C:\folder\target\*
pharseToAdd: str = 'Prefix'                 #For example: Prefix
timeToStart: int = 0                        #Time to start program after start in seconds, 0 for instant start
takePhoto: bool = False                     #True to take photo

######### EDIT FIELD #########

def photo() -> None:
    index: int = 0 # For photo number
    cam_port = 0 # Get build in camera port
    cam = cv2.VideoCapture(cam_port) # Get camera

    result, image = cam.read() # Take photo

    photos: list[str] = glob(storeLocation) # Get list of photos
    for i in photos: # Count photos
        index += 1

    if result:
        cv2.imwrite(f'{storeLocation}\\victim{index - 1}.png', image) # Save photo

def log(fromName: str, toName: str) -> None:
    logFile: str = f'{storeLocation}\\log.log' # Log file location

    with open(logFile, 'a') as file:
        now = datetime.datetime.now() # Get time
        file.write(f'\'{now}\' Log: Change name from {fromName} to {toName}\n') # Write single log

def rename() -> None:
    path: list[str] = glob(targetFolder, include_hidden = True) # Give path
    if takePhoto:
        photo()

    for file in path: # Literate through files
        if file[(len(targetFolder) - 1):(len(targetFolder) + len(pharseToAdd) - 1)] == pharseToAdd: # Check if file have already prefix
            continue
        newName: list[str] = f'{file[:(len(targetFolder) - 1)]}{pharseToAdd} {file[(len(targetFolder) - 1):]}' # Make name with prefix
        os.rename(file, newName) # Apply prefix
        log(file, newName) # Write log

def main() -> None:
    time.sleep(timeToStart) # Set time as you need
    rename()

if __name__ == '__main__':
    main()
