import wx
from wx import Choicebook, Listbook, Notebook, Treebook, Toolbook
from wx import Window
class HelloFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        st = wx.StaticText(pnl, label="Hello")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("welcome to world")
    
    def makeMenuBar(self):

        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item")

        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)


        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):

        self.Close(True)

    def OnHello(self, event):

        wx.MessageBox("hello 111")
    
    def OnAbout(self, event):

        wx.MessageBox("sanple", "about", wx.OK|wx.ICON_INFORMATION)

    
class demoWindow(wx.Window):

    def __init__(self, *args, **kw):
        super(demoWindow, self).__init__(*args, **kw)

if __name__ == '__main__':

    app = wx.App()
    frm = HelloFrame(None, title = 'hello window', pos = wx.Point(500, 500), size = wx.Size(1000, 1000), style = wx.BORDER_DEFAULT, name = "123123")
    frm.SetBackgroundColour()
    # wi = wx.Window(frm, wx.ID_ANY, wx.Point(50, 0), wx.Size(100, 100), wx.BORDER_DEFAULT, "123123")
    # (0,0), (100*100), Window.WindowStyle(), "win")
    frm.Show()
    # wi.Show()
    app.MainLoop()