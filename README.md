# Rename all files in a directory to include a postfix

## About
- Python script to rename all files (not folders) in a specific directory to include a postfix.
- E.g. filename 'image' with a '.png' postfix supplied will become 'image.png'.
- The script does not copy the files, it only renames them.
- The script won't add another postfix to a file which already has the same postfix provided. E.g. 'image.png' will stay 'image.png' not 'image.png.png' after running the script twice.

## How to run
```
Usage: python rename.py <Absolute directory> <postfix>
```
For example:
```
python rename.py C:/images .png
```
