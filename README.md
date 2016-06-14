# Launching a windows machine on ec2

- Follow the directions here:
  - http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-launch-instance_linux
- Make a [Microsoft Windows Server 2012 R2](https://aws.amazon.com/marketplace/pp/B00KQOWCAQ/ref=mkt_ste_windows_amis) box
  - Wait ~4 minutes while the windows machine boots up
- Connect to the box over RDP
  - If you're on mac, download the Microsoft Remote Desktop app from the App Store
  - Don't use the **Connect** button that Amazon gives you. Instead you should open the MRD App and hit the big **New** button to create a new server
  - In the **Edit Remote Dialogs** window, add a redirection folder with your downloaded Broodwar

## Development Environment

We recommend development on Windows 10 (64bit). If you're on OSX, you can use VMWareFusion to set up a development environment in a virtual machine.

## Installing StarCraft and BWAPI

Purchase Starcraft Anthology from Blizzard and install SC and BroodWar:
https://us.battle.net/account/management/download/?show=classic

Patch BroodWar to version 1.16.1:
https://us.battle.net/support/en/article/200684

Download BWAPI and install it: <br>
https://github.com/bwapi/bwapi/releases (if the download fails, use the [mirror](https://drive.google.com/file/d/0B1Iz-CApPh9eQjhTT3FEcml2NlU/view))

Prerequisites for Bot Compiling:
  * [Visual Studio 2013](https://msdn.microsoft.com/en-us/library/dd831853(v=vs.120).aspx) - [Direct Download Link](https://go.microsoft.com/fwlink/?LinkId=532506&clcid=0x409)
  * [BWAPI 4.1.2](https://github.com/bwapi/bwapi/releases/tag/v4.1.2)

If you aren't familiar with compiling with VisualStudio, we recommend that you follow [Dave Churchill's screencast for installing ualbertabot](https://www.youtube.com/watch?v=lSmkDjFm3Tw&ab_channel=serendib7). This has the same dependencies that we do.

Make sure to install BWAPI to the `C:/Libraries/` directory and set your environment variables.

Put the custom maps that we need into `C:\Program Files (x86)\StarCraft\Maps\openai`

Download the git repo (the best way is to use git on windows is using [Github's desktop app](https://desktop.github.com/))

## Installing python and pip

Open up PowerShell and install [Chocolatey](https://chocolatey.org/install) to use as a windows package manager. You can right-click in PowerShell to paste text there.
```bash
iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
```

Install [ConsoleZ](https://github.com/cbucher/console) as a replacement for PowerShell
```bash
choco feature enable -n allowGlobalConfirmation
choco install consolez
```

You can customize ConsoleZ by following [these directions](https://www.maketecheasier.com/console-2-windows-command-prompt-alternative/).

* Set PowerShell as your default shell
* Set `control+v` to paste

Install Python2.7 and pip
```bash
choco install python2 pywin32
```

Install the dependencies for our python app
```bash
cd /Libraries/starcraft-zmq-client
pip install virtualenv
virtualenv venv
./venv/Scripts/activate.ps1
pip install -r requirements.txt
```


## Debugging

**Could not connect to remote server because of this error:**

  ```
   Remote Desktop Connection cannot verify the identity of the computer that you want to connect to."
   ```
You may need to create a Microsoft Remote Desktop profile for this machine from scratch

**Running a local VM with VMWareFusion**


If you are running on a local VM, behind a NAT you might want to use ngrok for port forwarding
```
choco install ngrok.portable
ngrok tcp 80
```



# Usage

Open `PowerShell`

```shell
 C:/Libraries/StarCraftLearningEnv/bin/SCLE.exe
 ```
