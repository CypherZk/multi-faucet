This script is free because I'm too lazy to include a paid membership, feel free to donate :
```

```
# Install instructions

1. Install python
Get it from official website : [here](https://www.python.org/downloads) (disable max length and add it to path)

2. Install pip

First, check if pip isn't already installed by running in a cmd :
(It's supposed to be installed with python, but meh.. wasn't for me)
```
pip -help
```
If you get an error like it was for me right click and save this : [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

Right click anywhere in your browser, "save as".

There's a limit with clipboard, so you'll run into errors trying to can copy/paste it, this file is huge since it's a hashed zip file.

Open a cmd, then type those command, replacing [path_to_file] by actual path you saved the file (copy paste from explorer bar) :
```
cd [path_to_file]
python get-pip.py
```
Run this command again :
```
pip -help
```
If everything worked, you're supposed to see a bunch of text telling you how to use pip.

3. Install pyautogui
Run this command in a cmd :
```
pip install pyautogui
pip install pynput
```
You'll see a of download progress bar : it's installing the package and it's dependencies.

4. Now you can run the script :

```
cd [path_to_file]
python main.py
```

You have 5s to go in Discord and put your cursor in type mode in the desired channel.

Enjoy, no more pain typing all these faucets by hand 🖤

## Supported Faucets :

You can manually modify the main.py script to work only with desired bots

* ARRR
* KMD
* TOKEL
* VRSC
* CHIPS
* BEAN
* CLC
* EDG
* GET
* GP
* KATZ
* MCL
* NMD
* POS
* RAIN
* XGC
* ZILLA
