from xml.dom.xmlbuilder import Options

from selenium import webdriver
from xvfbwrapper import Xvfb
import sys, getopt, time, subprocess, shlex
import os


chrome_driver_path = "/Users/ansal/node_modules/.bin/chromedriver"
def run():
    print('Sreencast website animation')
    # xvfb = Xvfb(width=1280, height=720, colordepth=24)
    # xvfb.start()
    url = "https://demo.airmeet.com/event/session?t=fb8bf3a5-a9e2-4a9f-afea-3b17143da86c"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--kiosk")
    chromeOptions.add_argument("--window-size=1344,756")
    chromeOptions.add_argument("disable-infobars")
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--use-fake-ui-for-media-stream")
    # chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--autoplay-policy=no-user-gesture-required")
    chromeOptions.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })
    browser = webdriver.Chrome(chrome_driver_path, chrome_options=chromeOptions)
    browser.get(url)
    time.sleep(5)
    buttons = browser.find_elements_by_class_name('btn')
    buttons[0].click()


    # ffmpeg_stream = 'ffmpeg -y -f x11grab -s 1344x756 -r 30 -i :%d+nomouse -f pulse -ac 2 -i default  -c:v libx264 -preset superfast -acodec libmp3lame -ar 48000 -pix_fmt yuv420p -s 1344x756 -threads 0 -f matroska "%s.mkv"' % (xvfb.new_display, dir_path + "/" + recording_title)
    # ffmpeg_stream = 'ffmpeg -y -r 30 -f x11grab -s 1280x720 -i :%d+nomouse -c:v libx264rgb -crf 15 -preset:v ultrafast -c:a pcm_s16le -af aresample=async=1:first_pts=0 out.mkv' % xvfb.new_display
    # args = shlex.split(ffmpeg_stream)
    # print(ffmpeg_stream)
    # os.system(ffmpeg_stream)
    time.sleep(300)  # record for 30 secs

    browser.quit()
    # xvfb.stop()



if __name__ == "__main__":
    run()
