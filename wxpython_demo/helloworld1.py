import wx
from wx import Choicebook, Listbook, Notebook, Treebook, Toolbook

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

        bookMenu = wx.Menu()
        bookItem = bookMenu.Append(wx.ID_ANY)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        menuBar.Append(bookMenu, "book")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.Oncbook, bookItem)

    def bookHello(self):

        cbook = Choicebook()
        lbook = Listbook()
        nbook = Notebook()
        tbook = Toolbook()
        trbook = Treebook()

        self.Bind(cbook, self.oncbook, )

    def OnExit(self, event):

        self.Close(True)

    def OnHello(self, event):

        wx.MessageBox("hello 111")
    
    def OnAbout(self, event):

        wx.MessageBox("sanple", "about", wx.OK|wx.ICON_INFORMATION)

    def Oncbook(self, event):

        wx.Choicebook()
    

if __name__ == '__main__':

    app = wx.App()
    frm = HelloFrame(None, title = '123123')
    frm.Show()
    app.MainLoop()