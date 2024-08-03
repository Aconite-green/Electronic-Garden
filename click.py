import pyautogui
import time
import os

# 클릭할 x, y 좌표 값은 필요한 위치에 따라 변경해주세요
coordinates = [(1786 , 36,1), (1786,36,0.1),(675, 306,5),(1858,50,4),(1858, 50, 0.1),
               (1299, 63,1)]

def click_coordinates(coords):
    num=0
    # 해당 튜플에서 값을 왼쪽 부터 순서대로 가져옴
    for x, y, delay in coords:
        # delay 값만큼 쉬어줌 => 임의의 프로그램이 실행되는 시간을 사용자가 지정
        time.sleep(delay)
        # 해당 위치로 마우스 이동
        pyautogui.moveTo(x, y)

        # 클릭함
        pyautogui.click()

        # 몇 번째 클릭인지 터미널 창에 출력
        num += 1
        print(f"click sequence {num}")


click_coordinates(coordinates)

