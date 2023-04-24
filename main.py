import pyautogui
import time

if __name__ == '__main__':
    square_size = 200
    side_length = 50

    screen_width, screen_height = pyautogui.size()
    center_x, centrer_y = screen_width // 2, screen_height // 2
    top_left = (center_x - square_size // 2, centrer_y - square_size // 2)
    top_right = (center_x + square_size // 2, centrer_y - square_size // 2)
    bottom_right = (center_x + square_size // 2, centrer_y + square_size // 2)
    bottom_left = (center_x - square_size // 2, centrer_y + square_size // 2)

    pyautogui.moveTo(top_left[0], top_left[1], duration=0.5)

    while True:
        pyautogui.moveTo(top_left[0] + side_length, top_left[1], duration=1)
        pyautogui.moveTo(bottom_left[0], bottom_left[1] - side_length, duration=1)
        pyautogui.moveTo(bottom_left[0] - side_length, bottom_left[1], duration=1)
        pyautogui.moveTo(top_left[0], top_left[1], duration=1)
        time.sleep(1)
