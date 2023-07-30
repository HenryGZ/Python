import pyautogui
import time

print('spotify\nteams\nsteam\ndiscord')
op = str(input('bom dia! O que vamo fz hj meu guerreiro? ')).strip().upper()[0]

pyautogui.position()
pyautogui.moveTo(563, 767)
time.sleep(1)
pyautogui.moveTo(594, 744)                 
pyautogui.click()

#spotify
pyautogui.moveTo(636,377)
pyautogui.click()

#teams
pyautogui.moveTo(743,208)
pyautogui.click()

#steam
pyautogui.moveTo(478,212)
pyautogui.click()

#discord
pyautogui.moveTo(735,748)
pyautogui.click()



