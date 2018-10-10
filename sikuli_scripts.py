from time import strftime
import time
import datetime

SIX_HOURS = 21600

while(1):
    type("r", Key.WIN)
    time.sleep(1)
    click(Pattern("1538372747501.png").targetOffset(-107,58))
    type("a", Key.CTRL)
    type("chrome")
    type(Key.ENTER)

    wait(Pattern("1538001557343.png"), 3600)

    click("1538001557343.png")
    click("1538001499053.png")
    type("steemhunt.com")
    type(Key.ENTER)
    wait(Pattern(Pattern("1538183550239.png").similar(0.42)), 3600)
    click(Pattern("1538183550239.png").similar(0.42))
    while not exists(Pattern("1538184497953.png").similar(0.42)):
        type(Key.DOWN)
        time.sleep(1)
    click(Pattern("1538184497953.png").similar(0.42).targetOffset(42,4))
    time.sleep(SIX_HOURS)
