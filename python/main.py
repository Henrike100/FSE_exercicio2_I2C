from time import sleep
import RPi_I2C_driver
import smbus2
import bme280

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

mylcd = RPi_I2C_driver.lcd()

while(True):
    calibracao_paramentros = bme280.load_calibration_params(bus, endereco)
    dado = bme280.sample(bus, endereco, calibracao_paramentros)
    #mylcd.lcd_clear()
    mylcd.lcd_display_string_pos("T:{:.2f}".format(dado.temperature), 1, 0)
    mylcd.lcd_display_string_pos("U:{:.2f}".format(dado.humidity), 1, 9)
    mylcd.lcd_display_string("P:{:.2f} **".format(dado.pressure), 2)

    sleep(1)
    