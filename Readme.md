Chrome install

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo ln -s /opt/google/chrome/chrome /usr/local/bin/
sudo ln -s /opt/google/chrome/chrome /usr/bin/

Install chrome driver
wget -N http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -P ~/Downloads
sudo apt install unzip
unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads
sudo ln -s /home/ubuntu/Downloads/chromedriver /usr/local/bin/
sudo ln -s /home/ubuntu/Downloads/chromedriver /usr/bin/


Install python
pyhton3 if not installed
sudo apt install python3-pip


Install Xvfb if not there
sudo apt-get install xvfb


Install pip dependencies
pip3 install selenium xvfbwrapper


install ffmpeg
sudo apt-get install ffmpeg


Install pulse equalizer
sudo apt install pulseaudio-equalizer










/usr/bin/chromedriver: error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory
 sudo apt-get install libgconf-2-4


