from xml.dom.xmlbuilder import Options

from selenium import webdriver
from xvfbwrapper import Xvfb
import sys, getopt, time, subprocess, shlex
import os


chrome_driver_path = "/usr/bin/chromedriver"
# chrome_driver_path = "/Users/ansal/node_modules/.bin/chromedriver"

def run():
    print('Sreencast website animation')
    xvfb = Xvfb(width=1280, height=720, colordepth=24)
    xvfb.start()
    url = "https://demo.airmeet.com/e/1eb30ce0-c760-11ea-a9f9-e79c3e7031f6"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--kiosk")
    chromeOptions.add_argument("--window-size=1280x720")
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
    print('Starting browser')
    browser = webdriver.Chrome(chrome_driver_path, chrome_options=chromeOptions)
    print('Getting url')
    browser.get(url)
    print('got url')
    time.sleep(5)
    print('Slept 5 secs')
    ffmpeg_stream = 'ffmpeg -y -r 30 -f x11grab -s 1280x720 -i :%d+nomouse -c:v libx264rgb -crf 15 -preset:v ultrafast -c:a pcm_s16le -af aresample=async=1:first_pts=0 /tmp/out.mkv' % xvfb.new_display
    # ffmpeg_stream = 'ffmpeg -y -f x11grab -s 1280x720 -r 30 -i :%d -f pulse -ac 2 -i default  -c:v libx264 -preset superfast -acodec libmp3lame -ar 48000 -pix_fmt yuv420p -s 1280x720 -threads 0 -f matroska "%s.mkv"' % (
    # xvfb.new_display, '/tmp/out')
    # os.system(ffmpeg_stream)
    print(ffmpeg_stream)
    args = shlex.split(ffmpeg_stream)
    p = subprocess.Popen(args)
    print(p)
    time.sleep(2)

    try:
        browser.find_elements_by_class_name('btn-primary')[0].click()
        time.sleep(0.5)
        browser.find_elements_by_class_name('ml-1')[0].click()
        time.sleep(1)
        browser.find_element_by_id('name').send_keys("Selen")
        time.sleep(1)
        browser.find_element_by_id('designation').send_keys("Selen")
        time.sleep(1)
        browser.find_element_by_id('company').send_keys("Selen")
        time.sleep(1)
        # browser.find_element_by_id('city').send_keys("Selen")
        # time.sleep(0.2)
        # browser.find_element_by_id('country').send_keys("Selen")
        # time.sleep(0.2)
        # browser.find_elements_by_class_name('w-100')[1].click()
        # time.sleep(0.2)
        # browser.find_elements_by_class_name('w-100')[1].click()
        # time.sleep(2)
        # browser.find_elements_by_class_name('inverted')[0].click()
    except Exception as e:
        print(e)
    # ffmpeg_stream = 'ffmpeg -y -f x11grab -s 1344x756 -r 30 -i :%d+nomouse -f pulse -ac 2 -i default  -c:v libx264 -preset superfast -acodec libmp3lame -ar 48000 -pix_fmt yuv420p -s 1344x756 -threads 0 -f matroska "%s.mkv"' % (xvfb.new_display, dir_path + "/" + recording_title)
    # args = shlex.split(ffmpeg_stream)
    # print(ffmpeg_stream)
    time.sleep(30)  # record for 30 secs
    p.terminate()
    browser.quit()
    xvfb.stop()



if __name__ == "__main__":
    run()
