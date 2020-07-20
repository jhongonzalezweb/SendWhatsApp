from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://web.whatsapp.com')

input()
input()

def main():
    try:
        os.system("cls")
        print("Ingresando datos de cliente:\n")

        cl_name = input("Nombre: ").title()
        adress = input("Direccion: ").title()
        ftphone = input("Telefono: ")
        phone = "+56" + str(ftphone)

        os.system("cls")

        dtclient = cl_name +"\n"+ phone +"\n"+ adress

        print(dtclient)

        sleep(1)

        name = "TestBot" #input('Enter the name of user or group : ')
        msg = dtclient
        #msg = input('Enter the message : ')
        #count = int(input('Enter the count : '))

        #Scan the code before proceeding further
        input('Enter anything after scanning QR code')

        while True:
            try:
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()

                msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

                #for i in range(count):
                msg_box.send_keys(msg)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span').click()
                break
                sleep(1)

            except:
                sleep(1)
                input(">>> Error para conseguir parametros!")
                sleep(1)

    except KeyboardInterrupt:
        os.system("cls")
        print("\nSe ha originado un 'KeyboardInterrupt'")

if __name__ == '__main__':
    while True:
        main()
        salir = input("¿Desea salir del sistema (S/N)? ").lower()
        if salir == "s":
            break
driver.close()
