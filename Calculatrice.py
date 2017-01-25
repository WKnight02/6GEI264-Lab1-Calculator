# -*- coding: utf8 -*-
from bin import *

core = Core()
app = Interface(core)
key = KeypadModule(app)
app.mainloop()
