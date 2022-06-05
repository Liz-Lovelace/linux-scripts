#!/bin/python3


#All options specific to device `xerox_mfp:libusb:003:002': (get those with scanimage -A)
#  Standard:
#    --resolution 75|100|150|200|300|600|1200dpi [150]
#        Sets the resolution of the scanned image.
#    --mode Lineart|Halftone|Gray|Color [Color]
#        Selects the scan mode (e.g., lineart, monochrome, or color).
#    --highlight 30..70% (in steps of 10) [inactive]
#        Select minimum-brightness to get a white point
#    --source Flatbed|ADF|Auto [Flatbed]
#        Selects the scan source (such as a document-feeder).
#  Geometry:
#    -l 0..215.9mm (in steps of 1) [0]
#        Top-left x position of scan area.
#    -t 0..297.18mm (in steps of 1) [0]
#        Top-left y position of scan area.
#    -x 0..215.9mm (in steps of 1) [215.9]
#        Width of scan-area.
#    -y 0..297.18mm (in steps of 1) [297.18]
#        Height of scan-area.

from subprocess import check_output

view_images = input('View image after every scan? (YES|no) ')
view_images = view_images in ['yes', '']

format = input('Please enter a format (pnm|tiff|png|JPEG) ').strip()

if format == '':
    format = 'jpeg'

if not format in ['pnm', 'tiff', 'png', 'jpeg']:
    raise('Invalid format!!')





cmd = ['scanimage', f'--format={format}']

enumeration = 0
while True:
    name = input('Enter file name, the file extension will be added automatically (ENUM|anything) ')
    if name == '' or name == 'enum':
        enumeration += 1
        name = str(enumeration)
    print('scanning...')
    image = check_output(cmd)
    file_name = f'{name}.{format}'
    print('Done scanning, writing file...')
    with open(file_name, 'wb') as f:
        f.write(image)
    print(f'Created new file "{file_name}"')
    print(''.center(50, '='))
    if view_images:
        check_output(['feh', '-F', file_name])