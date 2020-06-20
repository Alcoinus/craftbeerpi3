import time
import threading
from modules import cbpi

try:
    import pigpio
except Exception as e:
    pass


class Buzzer(object):

    sound = ["H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L"]
    def __init__(self, gpio, beep_level):
        try:
            cbpi.app.logger.info("INIT BUZZER NOW GPIO%s" % gpio)
            self.gpio = int(gpio)
            self.beep_level = beep_level
            self.pi = pigpio.pi()
            self.state = True
            cbpi.app.logger.info("BUZZER SETUP OK")
        except Exception as e:
            cbpi.app.logger.info("BUZZER EXCEPTION %s" % str(e))
            self.state = False

    def beep(self):
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        class buzzerThread(threading.Thread):
            def __init__(self, buzzer):
                threading.Thread.__init__(self)
                self.buzzer = buzzer

            def run(self):
                try:
                    for i in self.buzzer.sound:
                        if isinstance(i, str):
                            if i == "H" and self.buzzer.beep_level == "HIGH":
                                self.buzzer.pi.hardware_PWM(self.buzzer.gpio, 1000, 500000)
                            elif i == "H" and self.buzzer.beep_level != "HIGH":
                                self.buzzer.pi.hardware_PWM(self.buzzer.gpio, 1000, 0)
                            elif i == "L" and self.buzzer.beep_level == "HIGH":
                                self.buzzer.pi.hardware_PWM(self.buzzer.gpio, 1000, 0)
                            else:
                                self.buzzer.pi.hardware_PWM(self.buzzer.gpio, 1000, 500000)
                        else:
                            time.sleep(i)
                except Exception as e:
                    cbpi.app.logger.error("BUZZER EXCEPTION %s" % str(e))
                    pass

        buzzerThread(self).run()


@cbpi.initalizer(order=2)
def init(cbpi):
    gpio = cbpi.get_config_parameter("buzzer", 18)
    beep_level = cbpi.get_config_parameter("buzzer_beep_level", "HIGH")

    cbpi.buzzer = Buzzer(gpio, beep_level)
    cbpi.beep()
    cbpi.app.logger.info("INIT OK")
