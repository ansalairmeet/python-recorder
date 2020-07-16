import shlex
import subprocess
import time
import traceback

from selenium import webdriver
from xvfbwrapper import Xvfb

chrome_driver_path = "/usr/bin/chromedriver"
# chrome_driver_path = "/Users/ansal/node_modules/.bin/chromedriver"

def run():
    print('Sreencast website animation')
    xvfb = Xvfb(width=1280, height=720, colordepth=24)
    xvfb.start()
    url = "https://test2.airmeet.com/event/session?t=b8f27257-8082-4a16-b1f9-851ba1e982e8"
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
    # ffmpeg_stream = 'ffmpeg -y -r 30 -f x11grab -s 1280x720 -i :%d+nomouse -f pulse -ac 2 -i default -c:v libx264rgb -crf 15 -preset:v ultrafast -c:a pcm_s16le -af aresample=async=1:first_pts=0 /tmp/out.mkv' % xvfb.new_display
    ffmpeg_stream = 'ffmpeg -y -r 24 -f x11grab -s 1280x720 -i :%d+nomouse -f pulse -ac 2 -i default -c:v libx264rgb -crf 28 -preset:v ultrafast -c:a pcm_s16le -af aresample=async=1:first_pts=0 /tmp/out.mkv' % xvfb.new_display
    # ffmpeg_stream = 'ffmpeg -y  -r 24 -f x11grab -s 640x360 -i :%d+nomouse -f pulse -ac 2 -i default  -c:v libx264 -preset superfast -acodec libmp3lame -ar 48000 -pix_fmt yuv420p -threads 0 -f matroska /tmp/out.mkv' % xvfb.new_display
    # os.system(ffmpeg_stream)
    print("Execute this command")
    print(ffmpeg_stream)
    args = shlex.split(ffmpeg_stream)
    p = subprocess.Popen(args)
    print(p)
    time.sleep(2)

    try:
        time.sleep(1)
        browser.find_elements_by_class_name('broadcast-streams')[0].click()
        # time.sleep(0.5)
        # browser.find_elements_by_class_name('ml-1')[0].click()
        # time.sleep(1)
        # name = browser.find_element_by_name('name')
        # print(name)
        # name.send_keys("Selen")
        # time.sleep(1)
        # designation = browser.find_element_by_name('designation')
        # print(designation)
        # designation.send_keys("Selen")
        # time.sleep(1)
        # company = browser.find_element_by_name('company')
        # print(company)
        # company.send_keys("Selen")
        # time.sleep(1)
        # browser.find_element_by_id('city').send_keys("Selen")
        # time.sleep(0.2)
        # browser.find_element_by_id('country').send_keys("Selen")
        # time.sleep(0.2)
        # browser.find_elements_by_class_name('w-100')[1].click()
        # time.sleep(0.2)
        # browser.find_elements_by_class_name('w-100')[1].click()
        # time.sleep(30)
        # browser.find_elements_by_class_name('inverted')[0].click()
    except Exception as e:
        print("Some error occurred")
        traceback.print_exc()
    # ffmpeg_stream = 'ffmpeg -y -f x11grab -s 1344x756 -r 30 -i :%d+nomouse -f pulse -ac 2 -i default  -c:v libx264 -preset superfast -acodec libmp3lame -ar 48000 -pix_fmt yuv420p -s 1344x756 -threads 0 -f matroska "%s.mkv"' % (xvfb.new_display, dir_path + "/" + recording_title)
    # args = shlex.split(ffmpeg_stream)
    # print(ffmpeg_stream)
    time.sleep(25)  # record for 30 secs
    p.terminate()
    browser.quit()
    xvfb.stop()



if __name__ == "__main__":
    run()
