# Retropad Instagram Uploader
## Introduction
This is a simple program I created to solve a simple problem. I needed to upload images every day to Instagram, and I found myself repeating the same tasks over and over. Take screenshots of the game and cover art on my laptop. Copy cover art into screenshot, resize it and position it. Email the picture to myself. Open the image on my cellphone and post it to Instagram. Even Grammarly thinks this monotonous.
 
This program takes care of most of those steps. Once I have taken the screenshots, all I have to do open each file in the app. It takes care of the rest.

This full application is one of the first that I completed outside of work or school environment. As such, there are several things I wish I'd done differently. Probably the biggest is the need to separate the app into the frontend, controller, and connection modules. See the git issues for other things that could be improved.

![Screenshot displaying files and compiled image](https://i.imgur.com/QSIK9Kt.png)

## Helpful Notes
### Configuration
1. I've included a file named sample_config.json. This file must be renamed config.json and populated with the your login in for the 'gram.'
2. The utils folder contains a file called create_cookie.py. You must run this file to create the needed cookie to connect.
3. If you wish to change the background that file can be found in the images file.

### Package Requirements
* Pillow 6.1.0 +
* Instapy_cli 0.0.12+

Use this command to install the necessary packages:
```commandline
pip install Pillow instapy-cli
```
### Contributing
As explained in the introductions this software is only my first attempt. We (royal) 
welcome contributions that give the application more versatility in use cases. 

Please just follow the simple guidelines:

* When contributing to this repository, please first discuss the change you wish to make 
via issue, email, or any other method with the owners of this repository before making 
a change.
* In all interactions please be kind and respectful.


## License
   MIT License

   Copyright (c) 2020 Gabriel Ruiz  

   Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
