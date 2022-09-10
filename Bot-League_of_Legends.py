import pyautogui
import time

pyautogui.PAUSE = 2.0
pyautogui.alert('seu bot será executado agora')
#buscar e abrir o League
pyautogui.press('winleft')
pyautogui.write('league')
time.sleep(2)
pyautogui.press('enter')

#fazer o login
time.sleep(25)
pyautogui.write('seu usuario')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')

#clicar em jogar
time.sleep(35)
pyautogui.click(160, 38)
#selecionar solo/duo
time.sleep(5)
pyautogui.click(200, 578)
pyautogui.click(577, 686)
#colocar as rotas
time.sleep(2)
pyautogui.click(698, 680)
pyautogui.click(715, 621)        #ATIRADOR
time.sleep(1)
pyautogui.click(734, 677)
pyautogui.click(700, 622)        #MID
pyautogui.alert('fim da execução do seu bot')