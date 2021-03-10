import wx
from wx import Window, BORDER_DEFAULT

class demoWindow(wx.Window):

    def __init__(self, *args, **kw):
        super(demoWindow, self).__init__(*args, **kw)
    



if __name__ == '__main__':

    app = wx.App()
    wi = demoWindow(app)
    wi.Show()
    app.MainLoop()

# wi = Window(BORDER_DEFAULT)
# print(wi.WindowStyle)