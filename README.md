## CDN Speed Game Contest

## What Is This About?

* The Christian Developers Network has hosted this event annually since 2006. The goal of this contest is to develop a game in a few weeks based on a Christian theological or Bible verse theme. Go to this page to learn about the [Contest Rules and Details](https://github.com/CDNSpeedgames/2017/wiki/2017-CDN-Speed-Game-Contest).

## GitHub Instructions

##### Overview

* The **CDN Speed Game** uses **GitHub**, for storing game source code and release files. It is **free** to use for Open Source projects. All games hosted here follow one or more of these licenses determined by the game maker.
* Contact <cdnspeedgame@gmail.com> and ask to be added as a contributor if you would like to participate in the contest.
* Go to [https://github.com](https://github.com) and open an account and then download the latest version of the **Git Bash** client here [http://git-scm.com/downloads](http://git-scm.com/downloads). ***Install the Git client with defaults settings***.
* You can also use the **GitHub GUI client for Windows/Mac** from this site [https://desktop.github.com/](https://desktop.github.com/). Refer to the online documentation for using this client.
* We will focus on the standard command line **Git Bash** client for the remaining instructions.

##### First Time Download and Initialization

* Run the **Git Bash** console program for Windows. You should should have an icon on your desktop when it was installed. (Use the built-in Terminal application for Mac.)
* Enter each of these commands in the **Git Bash** console. Replace the name and email details in "" and [] with your information.
<pre>
	Windows
	cd /c/CDNSpeedGame

	Mac
	cd /Users/[username]/Documents/CDNSpeedGame

	git config --global user.name "Leeroy Jenkins"
	git config --global user.email "leeroy@mymail.com"
	git init
	git clone "https://github.com/CDNSpeedgames/2017.git"
</pre>
* You should see several messages as the files are copied from **GitHub** to your local computer. Congratulations, you now have a full copy of the latest source code for all our games!

##### Folder Structure and Files

* Once you have obtained access to this repository, please make a new folder under the **games** folder to store your code. Replace [MyGame] with the folder name for your game. Here is an example of the comand to run in the Bash console.
<pre>
	Windows
	mkdir -p /c/CDNSpeedGame/games/[MyGame]

	Mac
	mkdir -p /Users/[username]/Documents/CDNSpeedGame/games/[MyGame]

</pre>
* Store all of your game files in this folder. Please do not modify or delete files on other folders in this repository.
* Only source code should be stored on **GitHub**. There is a **1GB** limit for all files stored here. Sound and image files should not be uploaded to **GitHub** unless they are small, and in total with the source code, do not exceed 25mb.
* You will have full rights to modify any files on our **GitHub** repository. Please keep our folders clean and organized.
* You are not required to host your source code in our **GitHub** repository, but it is encouraged to do so as long as the size of these files do not exceed 25mb total for the complete game. We have a 1GB limit for all files stored on **GitHub**. See the **Release Files** section below for specifics on source code storage for release builds.
* You should include a header.png image file, max size of (600x600) to be used on your release build as a banner, icon, logo, or screen shot for the game. We will put this image above the description on the release page for our contest winners.
* We have uploaded a sample Pong game to help get you started. Please use it as a guide for your game and how we expect to manage game source code here.

##### Pushing files to GitHub

* Run the **Git Bash** console program for Windows or the built-in Terminal application for Mac.
* Enter these commands.
<pre>
	Windows
	cd /c/MyCDNSpeedGame/games/[MyGame]

	Mac
	cd /Users/[username]/Documents/CDNSpeedGame/games/[MyGame]

	git add SomefileName
	git commit -m "Some Comment"
	git push origin master
</pre>
* Replace **SomeFileName** with the file(s) you modified. You can also use folder names too.
* Make sure you **add meaningful comments** for all changes so it is clear what was updated or added.
* Once you submit the **git push** command, you will be prompted for your user name and password the first time. This is the account you setup on **GitHub**.

##### Pulling files from GitHub

* Run the **Git Bash** console program for Windows or the built-in Terminal application for Mac.
* Enter these commands to get the latest updates.
<pre>
	Windows
	cd /c/CDNSpeedGame

	Mac
	cd /Users/[username]/Documents/CDNSpeedGame

	git pull origin
</pre>

* You can also force a file to be downloaded from **GitHub** if it was deleted on you local computer with this command.
<pre>
	git checkout SomeFileName
</pre>

##### Release Files

* We are using the buit in release service of GitHub to publish the final winners of our contest. You can see this page through the **Release** link at the top of this page or directly [here](https://github.com/CDNSpeedgame/2017/releases).
* Please do not modify the releaase page yourself. Our admins will manage this page once the contest is completed.
* All of the games in this contest are open source projects. We encourage you to store your code in our repository. However, for convencince sake, we also require that you create a .gz or .zip of your source code and all game assets for the release build. At a minimum, you will need to give us your packaged game, and another file, or files, containing the build files. You can see an example of this with the Pong game we have posted on the relese page. The installer and source files are available for download directly here for that game.

##### GitHub - Final Words

* This document is only a starter for **Git** and **GitHub** commands and concepts. Please refer to other documents and tutorials if you wish to be well versed in the technology.
