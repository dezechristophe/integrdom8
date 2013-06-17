# _*_ coding: iso-8859-1 _*_
#!/usr/bin/env python
#Boa:App:BoaApp

import wx, sys
if hasattr(sys, 'setdefaultencoding'):
    import locale
    loc = locale.getdefaultlocale()
    if loc[1]:
        encoding = loc[1]
        sys.setdefaultencoding(encoding)

import Frame1

modules ={'Frame1': [1, 'Main frame of Application', 'Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
