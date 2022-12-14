import os
from datetime import date
from datetime import datetime
from progress.bar import Bar, ChargingBar

now = datetime.now()
now = str(now)
print("Installing PIP Packs...")
file = open('0.txt', 'w')
file.write(now + os.linesep)
file.write('installed')
file.close()

battxt2 = open('ins.bat', 'w')
battxt2.write('cd PasswordGenerator pip install werkzeug pip install progress echo "0123456789"cd Datapy confirm.pygoto exit')
battxt2.close()

battxt = open('ins.txt', 'w')
battxt.write('fas')
battxt.close()
battxt2.close()

print("Closing...")

exit()