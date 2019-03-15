 Social Media Mining with Python
=================================

Setting up the environment
-----

It's strongly recommended to create a virtual environment, with `virtualenv`.

Get the repo:

    git clone https://github.com/PingouInfini/socialmediamining.git
    cd socialmediamining

Install virtualenv:

    pip install virtualenv

Create the environment (replace "my_own_env" by "twitter", "facebook" ...):

    mkdir virtualenv
    cd virtualenv
    virtualenv <my_own_env>

Activate the environment :

    <my_own_env>/Scripts/activate

Deactivate the environment (from any path):

    deactivate

SandBox for social media
-----
##### Twitter
##### Facebook
##### Google Search
##### Google Images
##### Scrapy

###### Coming next...
- ###### LinkedIn
- ###### Snapchat
- ###### forum

Known Pain in this axx (Windows)
-----
Install VS Buildtools (Outils de génération pour Visual Studio [FR]) 
(https://visualstudio.microsoft.com/fr/downloads)

Choose the following options in the Work Loads -> Visual C++ build tools -> Optional
- Windows 10 SDK (10.0.17763.0)
- Visual C++ tools for CMake
- Testing tools core features - Build Tools
- Visual C++ ATL for x86 and x64
- VC++ 2015.3 v14.00 (v140) toolset for desktop

Choose the following options in the Work Loads -> Visual C++ build tools -> Individual Components
- Windows Universal CRT SDK
- Windows 8.1 SDK

Restart the computer (if needed)

Copy following files from "C:\Program Files (x86)\Windows Kits\8.1\bin\x86" to "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin"
- rc.exe
- rcdll.dll