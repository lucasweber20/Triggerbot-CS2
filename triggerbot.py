import pymem
import pymem.process
import keyboard
import pyautogui


def main():
    dwEntityList = 0x271EB08
    dwLocalPlayerPawn = 0x256A948
    m_iTeamNum = 0x3E7
    m_iHealth = 0x34C
    m_iIDEntIndex = 0x36DC

    pm = pymem.Pymem("cs2.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    is_on = 0

    while True:
        try:
            player = pm.read_ulonglong(client + dwLocalPlayerPawn)
            entity_id = pm.read_int(player + m_iIDEntIndex)

            if keyboard.is_pressed("o"):
                is_on = 1
            elif keyboard.is_pressed("p"):
                is_on = 0

            if entity_id != -1 and is_on == 1:
                pyautogui.click()
        except:
            print("Error occured")

if __name__ == "__main__":
    main()