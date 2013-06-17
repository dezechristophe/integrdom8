# _*_ coding: iso-8859-1 _*_
#Boa:Frame:Frame1

import wx
import pywintypes
import os,sys
import win32api
import win32netcon, win32file, win32con, win32wnet
import win32process, win32event
from ctypes import *
import  wx.lib.masked as m
import dict4ini
from _winreg import *
import platform
import win32com.client
import win32net
import socket
import wmi
            
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTONJOIN, wxID_FRAME1BUTTONSAVE, 
 wxID_FRAME1CHECKBOXINSTALL, wxID_FRAME1CHECKBOXREBOOT, 
 wxID_FRAME1COMBOBOXDOM, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXTNOMMACH, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1TEXTCTRLADMIN, wxID_FRAME1TEXTCTRLHOSTNAME, wxID_FRAME1TEXTCTRLIP, 
 wxID_FRAME1TEXTCTRLPASSWORD, wxID_FRAME1TEXTCTRLSERV, 
] = [wx.NewId() for _init_ctrls in range(19)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(771, 259), size=wx.Size(288, 376),
              style=wx.TAB_TRAVERSAL | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX,
              title=u'IntegrDom7')
        self.SetClientSize(wx.Size(280, 342))
        self.SetIcon(wx.Icon(u'eole.ico', wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(280, 319),
              style=wx.TAB_TRAVERSAL)

        self.staticTextNomMach = wx.StaticText(id=wxID_FRAME1STATICTEXTNOMMACH,
              label=u'Nom de la machine', name=u'staticTextNomMach',
              parent=self.panel1, pos=wx.Point(2, 8), size=wx.Size(94, 16),
              style=0)

        self.textCtrlServ = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLSERV,
              name=u'textCtrlServ', parent=self.panel1, pos=wx.Point(88, 72),
              size=wx.Size(120, 21), style=0, value=u'')
        self.textCtrlServ.Bind(wx.EVT_SET_FOCUS, self.OnTextCtrlServSetFocus)

        self.textCtrlIP = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLIP,
              name='textCtrlIP', parent=self.panel1, pos=wx.Point(88, 104),
              size=wx.Size(100, 21), style=0, value=u'')
        self.textCtrlIP.Bind(wx.EVT_SET_FOCUS, self.OnTextCtrlIPSetFocus)

        self.textCtrlAdmin = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLADMIN,
              name='textCtrlAdmin', parent=self.panel1, pos=wx.Point(88, 136),
              size=wx.Size(100, 21), style=0, value='admin')

        self.textCtrlPassword = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLPASSWORD,
              name='textCtrlPassword', parent=self.panel1, pos=wx.Point(88,
              168), size=wx.Size(100, 21), style=wx.TE_PASSWORD,
              value='Password')
        self.textCtrlPassword.SetEditable(True)
        self.textCtrlPassword.Bind(wx.EVT_SET_FOCUS,
              self.OnTextCtrlPasswordSetFocus)

        self.checkBoxInstall = wx.CheckBox(id=wxID_FRAME1CHECKBOXINSTALL,
              label=u'Installation du client Scribe', name=u'checkBoxInstall',
              parent=self.panel1, pos=wx.Point(80, 200), size=wx.Size(144, 13),
              style=0)
        self.checkBoxInstall.SetValue(True)

        self.checkBoxReboot = wx.CheckBox(id=wxID_FRAME1CHECKBOXREBOOT,
              label=u'Red\xe9marrage automatique', name=u'checkBoxReboot',
              parent=self.panel1, pos=wx.Point(80, 224), size=wx.Size(144, 13),
              style=0)
        self.checkBoxReboot.SetValue(True)

        self.buttonJoin = wx.Button(id=wxID_FRAME1BUTTONJOIN,
              label=u'&Joindre le domaine', name='buttonJoin',
              parent=self.panel1, pos=wx.Point(80, 248), size=wx.Size(120, 23),
              style=0)
        self.buttonJoin.Bind(wx.EVT_BUTTON, self.OnButtonJoinButton,
              id=wxID_FRAME1BUTTONJOIN)

        self.buttonSave = wx.Button(id=wxID_FRAME1BUTTONSAVE,
              label=u'&Enregistrer', name='buttonSave', parent=self.panel1,
              pos=wx.Point(8, 280), size=wx.Size(75, 23), style=0)
        self.buttonSave.Bind(wx.EVT_BUTTON, self.OnButtonSaveButton,
              id=wxID_FRAME1BUTTONSAVE)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetStatusText(u'Pr\xeat')
        self.SetStatusBar(self.statusBar1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Nom du serveur', name='staticText1', parent=self.panel1,
              pos=wx.Point(4, 76), size=wx.Size(76, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Nom du domaine', name='staticText2', parent=self.panel1,
              pos=wx.Point(4, 44), size=wx.Size(79, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'IP du serveur', name='staticText3', parent=self.panel1,
              pos=wx.Point(4, 108), size=wx.Size(65, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Utilisateur', name='staticText4', parent=self.panel1,
              pos=wx.Point(4, 140), size=wx.Size(48, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Mot de passe', name='staticText5', parent=self.panel1,
              pos=wx.Point(4, 172), size=wx.Size(64, 13), style=0)

        self.comboBoxDom = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOXDOM,
              name=u'comboBoxDom', parent=self.panel1, pos=wx.Point(88, 40),
              size=wx.Size(130, 21), style=wx.TE_PROCESS_ENTER, value=u'')
        self.comboBoxDom.SetLabel(u'')
        self.comboBoxDom.Bind(wx.EVT_COMBOBOX, self.OnComboBoxDomCombobox,
              id=wxID_FRAME1COMBOBOXDOM)
        self.comboBoxDom.Bind(wx.EVT_TEXT_ENTER, self.OnComboBoxDomTextEnter,
              id=wxID_FRAME1COMBOBOXDOM)

        self.textCtrlHostname = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLHOSTNAME,
              name=u'textCtrlHostname', parent=self.panel1, pos=wx.Point(104,
              8), size=wx.Size(112, 21), style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        # passage en m.IpAddrCtrl
        self.textCtrlIP.Destroy()
        self.textCtrlIP = m.IpAddrCtrl(id=wxID_FRAME1TEXTCTRLIP,
          name='textCtrlIP', parent=self.panel1, pos=wx.Point(82, 104),
          size=wx.Size(100, 21), style=0, value='')
        self.textCtrlIP.Bind(wx.EVT_SET_FOCUS, self.OnTextCtrlIPSetFocus)
        # fin IpAddrCtrl
        #self.staticTextNomMach.SetLabel('Nom de la machine : "%s"'%win32api.GetComputerName())
        self.textCtrlHostname.SetValue(win32api.GetComputerName())
        try:
            self.conf_f = sys.argv[1] + '\\ParamIntegr.ini'
        except:
            self.conf_f = 'ParamIntegr.ini'
        self.statusBar1.SetStatusText(self.conf_f)
        
        self.buttonJoin.SetFocus()
        self.loadparam()
        order = (self.comboBoxDom, self.textCtrlServ, self.textCtrlIP, self.textCtrlAdmin, 
            self.textCtrlPassword, self.checkBoxInstall, self.checkBoxReboot , self.buttonJoin)
        for i in xrange(len(order) - 1):
            order[i+1].MoveAfterInTabOrder(order[i])
        self.finddoms()

    def testportscribe(self):
        s = socket.socket()
        try:
            s.settimeout(1)
            s.connect((self.textCtrlIP.GetValue(), 8789))
            s.close()
            self.checkBoxInstall.SetValue(1)
        except socket.error:
            self.checkBoxInstall.SetValue(0)
            s.close() 

    def loadparam(self):
        if not os.path.isfile(self.conf_f): return
        try:
            d = dict4ini.DictIni(self.conf_f)
            sect = 'global'
            if not d.has_key(sect): return
            if d[sect].has_key('serveur'):
                self.textCtrlServ.SetValue(d[sect]['serveur'])
            if d[sect].has_key('ip'):
                self.textCtrlIP.SetValue(d[sect]['ip'])
            if d[sect].has_key('domaine'):
                self.comboBoxDom.Append(d[sect]['domaine'])
                self.comboBoxDom.SetSelection(0)
            if d[sect].has_key('user'):
                self.textCtrlAdmin.SetValue(d[sect]['user'])
            if d[sect].has_key('password'):
                self.textCtrlPassword.SetValue(d[sect]['password'].decode('base64'))
        except Exception, e:
            msg = u"Erreur à l'ouverture de %s"%(self.conf_f)
            self.errbox(msg, e)

        
    def saveparam(self):
        try:
            d = dict4ini.DictIni(self.conf_f)
            sect = 'global'
            d[sect]['serveur'] = self.textCtrlServ.GetValue()
            d[sect]['ip'] = self.textCtrlIP.GetAddress()
            d[sect]['domaine'] = self.comboBoxDom.GetValue()
            d[sect]['user'] = self.textCtrlAdmin.GetValue()
            d[sect]['password'] = self.textCtrlPassword.GetValue().encode('base64')
            d.save()
        except Exception, e:
            msg = u"Erreur à l'enregistrement de %s"%(self.conf_f)
            self.errbox(msg, e)

    def finddc(self):
        try:
            dc = win32net.NetGetDCName(None, self.comboBoxDom.GetValue())
            dc = dc.replace('\\\\','')
            self.textCtrlServ.SetValue(dc)
            self.textCtrlIP.SetValue(socket.gethostbyname(dc))
        except Exception, e:
            self.statusBar1.SetStatusText(str(e))

    def finddoms(self):
        network = win32com.client.GetObject ("WinNT:")
        for group in network:
            try:
                if not group.name == 'WORKGROUP':
                    print group.name
                    self.comboBoxDom.Append(group.name)
            except:
                pass
    
    # surligner le contenu de la case quand on clic dedans
    def OnTextCtrlServSetFocus(self, event):
        wx.CallAfter(self.textCtrlServ.SetSelection, -1, -1)
    
    def OnTextCtrlIPSetFocus(self, event):
        wx.CallAfter(self.textCtrlIP.SetSelection, -1, -1)

    def OnTextCtrlPasswordSetFocus(self, event):
        wx.CallAfter(self.textCtrlPassword.SetSelection, -1, -1)

    # les boutons     :
    # "Enregistrer"
    def OnButtonSaveButton(self, event):
        self.saveparam()

    # "Joindre le domaine"
    def OnButtonJoinButton(self, event):
        dom, servip = self.comboBoxDom.GetValue(), self.textCtrlIP.GetAddress()
        user, passwd = self.textCtrlAdmin.GetValue(), self.textCtrlPassword.GetValue()
        
        winos = testOS()
        if winos == '7':
            cle_registre()
        #TODO
        self.domainpardefaut()
        test_serveur()
        renomme_station(self.textCtrlHostname.GetValue(),self.comboBoxDom.GetValue())
        # joindre le domaine
        self.statusBar1.SetStatusText('Jonction au domaine "%s"...'%dom)
        if self.exec_func(joindom, dom, user, passwd) != 0:
            return
        self.statusBar1.SetStatusText('Jonction au domaine "%s" terminée, redémarrage nécessaire'%dom)
        if self.checkBoxInstall.GetValue():
            # montage du partage "perso"
            unc = r'\\%s\%s'%(servip, 'perso')
            self.statusBar1.SetStatusText('Connexion à "%s"...'%unc)
            drive = self.exec_func(connect,'u:', unc, user, passwd)
            if not drive:
                return
            import wmi
            c = wmi.WMI()
            #self.statusBar1.SetStatusText(str(c.Win32_Processor()[0].AddressWidth))
            #if c.Win32_Processor()[0].AddressWidth == 64:
            #    # Installation du client 64
            #    #try:
            #    #    regkey = OpenKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Eole\\Scribe', 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
            #    #except:
            #    #    regkey = CreateKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Eole\\Scribe', 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
            #    #SetValueEx(regkey, "port_scribe_update", 0, REG_SZ, "8790")
            #    #CloseKey(regkey)
            #    cmd = r'%s\client\cliscribe-setup.exe /SILENT /NORESTART'%drive       
            #    self.statusBar1.SetStatusText('Exécution de "%s"...'%cmd)
            #    if self.exec_func(lancecmd, cmd, hide=True) != 0:
            #        return disconnect(drive)                         
            #else:
                # Installation du client
            cmd = r'%s\client\cliscribe-setup.exe /SILENT /NORESTART'%drive
            self.statusBar1.SetStatusText('Exécution de "%s"...'%cmd)
            if self.exec_func(lancecmd, cmd, hide=True) != 0:
                return disconnect(drive)
            # Installation du service de MAJ du client
            if os.path.exists(unc + '\client\cliscribe-updater-setup.exe'):
                cmd = r'%s\client\cliscribe-updater-setup.exe /SILENT /NORESTART'%drive
                self.statusBar1.SetStatusText('Exécution de "%s"...'%cmd)
                if self.exec_func(lancecmd, cmd, hide=True) != 0:
                    return disconnect(drive)
            disconnect(drive)
        self.statusBar1.SetStatusText('Installation terminée.')
        if self.checkBoxReboot.GetValue():
            self.statusBar1.SetStatusText('Redémarrage...')
            reboot()
    
    def exec_func(self, func, *args, **kwargs):
        try: return func(*args, **kwargs)
        except pywintypes.error, e:
            msg = """Erreur à l'exécution de "%s" """%(func.__name__)
            self.errbox(msg, '%s %s'%(e[0], e[2]))
        except Exception, e:
            msg = """Erreur à l'exécution de "%s" """%(func.__name__)
            self.errbox(msg, e)

    def errbox(self, msg, e):
        wx.MessageBox(u'%s:\n\n%s'%(msg, e), 'Erreur', wx.ICON_ERROR)
        self.statusBar1.SetStatusText(u'Erreur : "%s"'%e)

    def OnComboBoxDomCombobox(self, event):
        self.finddc()
        self.testportscribe()

    def OnComboBoxDomTextEnter(self, event):
        self.finddc()
        self.testportscribe()
        
    def domainpardefaut(self):
        try:
            regkey = OpenKeyEx(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
        except:
            regkey = CreateKeyEx(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)

        SetValueEx(regkey, "DefaultDomainName", 0, REG_SZ, self.comboBoxDom.GetValue())
        CloseKey(regkey)

def joindom(dom, user, passwd):
	netapi32 = windll.LoadLibrary ("netapi32.dll")
	user = '%s\\%s'%(dom, user)
	ret = netapi32.NetJoinDomain(None, dom , None, user, passwd ,int(0x00000001|0x00000002|0x00000020))
	if ret != 0:
	    dicterr = dict()
	    dicterr[1219]='Fermez les connexions existantes sur le serveur'
	    dicterr[1311]='Domaine introuvable'
	    dicterr[1326]='erreur d\'authentification' 
	    dicterr[2691]='Deja dans le domaine'
	    try:
	        msgerr = dicterr[ret]
	    except:
	        msgerr = ''
	    raise pywintypes.error(ret, 'NetJoinDomain', 'Impossible de joindre le domaine ' + dom +  '\n' + msgerr)
	return ret
	

def connect(drive, unc, username=None, password=None, persistent=False):
    """Monte un lecteur
    """
    dliste = ['d:','e:','f:','g:','h:','i:','j:','k:','l:','m:','n:','o:','p:','q:','r:','s:','t:','u:','v:','w:','x:','y:','z:']
    if persistent: flags = win32netcon.CONNECT_UPDATE_PROFILE
    else: flags = 0
    if win32file.GetDriveType(drive) != win32con.DRIVE_NO_ROOT_DIR:
        for drive in dliste:
            if win32file.GetDriveType(drive) == win32con.DRIVE_NO_ROOT_DIR: break
    win32wnet.WNetAddConnection2(
        win32netcon.RESOURCETYPE_DISK,
        drive,
        unc,
        None,
        username,
        password,
        flags
        )
    return drive

def disconnect(drive):
    """Démonte le lecteur "drive"
    """
    if not os.path.exists(drive): return True
    if win32file.GetDriveType(drive) == win32con.DRIVE_REMOTE: # si lecteur réseau déjà présent, déconnexion
        win32wnet.WNetCancelConnection2(drive, 0, 1)
        return True
    return False

def lancecmd(cmd, hide=False, nowait=False, waitinput=False):
    appName = None
    commandLine = cmd
    processAttributes = None
    threadAttributes = None
    inheritHandles = False
    creationFlags = win32con.CREATE_DEFAULT_ERROR_MODE
    newEnvironnement = None
    currentDirectory = None
    startupinfo = win32process.STARTUPINFO()
    if hide:
        startupinfo.dwFlags = win32process.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = win32con.SW_HIDE
    handle, hthread, process_id, thread_id = win32process.CreateProcess(appName,
                                                                       commandLine,
                                                                       processAttributes,
                                                                       threadAttributes,
                                                                       inheritHandles,
                                                                       creationFlags,
                                                                       newEnvironnement,
                                                                       currentDirectory,
                                                                       startupinfo)
     
    if waitinput:
        # attendre au moins que le programme s'initialise
        # NE fonctionne PAS tjrs
        win32event.WaitForInputIdle(handle, win32event.INFINITE)
    if nowait: return 0
    # Sinon on attend que l'application finisse
    win32event.WaitForSingleObject(handle, win32event.INFINITE)
    return int(win32process.GetExitCodeProcess(handle))

def reboot():
    lancecmd('shutdown -r -f -t0', hide=True, nowait=True)
# nécessite l'utilisation de privilèges NT, 
# solution temporaire ci-dessus
##    opts = win32con.EWX_REBOOT | win32con.EWX_FORCE
##    win32api.ExitWindowsEx(opts, 0)
    import subprocess
    subprocess.call(["shutdown.exe", "-r", "-f", "-t", "6"])
    
def testOS():
    if os.name == 'nt':
        ver = sys.getwindowsversion()
        ver_format = ver[3], ver[0], ver[1]
        win_version = {
                        (1, 4, 0): '95',
                        (2, 5, 1): 'XP',
                        (2, 5, 2): '2003',
                        (2, 6, 0): 'Vista',
                        (2, 6, 1): '7',
        }
        if ver_format in win_version:
            return  win_version[ver_format]
            
            
def cle_registre():
    cles = [["Compatibilité Samba",HKEY_LOCAL_MACHINE,"System\CurrentControlSet\Services\LanManWorkstation\Parameters","DomainCompatibilityMode",REG_DWORD,1],
    ["Compatibilité Samba",HKEY_LOCAL_MACHINE,"System\CurrentControlSet\Services\LanManWorkstation\Parameters","DNSNameResolutionRequired",REG_DWORD,0],
    ["Désactivation de l'UAC",HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","EnableLUA",REG_DWORD,0],
    ["Désactivation de l'UAC",HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","ConsentPromptBehaviorAdmin",REG_DWORD,0],
    ["Désactivation de l'UAC",HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","PromptOnSecureDesktop",REG_DWORD,0],
    #["Désactivation de l'UAC",HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","dontdisplaylastusername",REG_DWORD,1],
    ["Délais d'attente du profil",HKEY_LOCAL_MACHINE,"SOFTWARE\Policies\Microsoft\Windows\System","WaitForNetwork",REG_DWORD,1]]
    
    for cle in cles:
        ruche = cle[1]
        keypath = cle[2]
        key = cle[3]
        keytype = cle[4]
        keyval = cle[5]
        
        
        try:
            regkey = OpenKeyEx(ruche, keypath, 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
        except:
            regkey = CreateKeyEx(ruche, keypath, 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
            
        SetValueEx(regkey, key, 0, keytype, keyval)
        CloseKey(regkey)
    
        
def test_serveur():
    pass

def renomme_station(hostname,dom):
    cles = [["computername",HKEY_LOCAL_MACHINE,"System\\CurrentControlSet\\Control\\ComputerName\\ComputerName","ComputerName",REG_SZ,hostname],
    ["computername",HKEY_LOCAL_MACHINE,"System\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName","ComputerName",REG_SZ,hostname],
    ["computername",HKEY_LOCAL_MACHINE,"System\\CurrentControlSet\\Services\\Tcpip\\Parameters","Hostname",REG_SZ,hostname],
    ["computername",HKEY_LOCAL_MACHINE,"System\\CurrentControlSet\\Services\\Tcpip\\Parameters","NV Hostname",REG_SZ,hostname]]
    for cle in cles:
        ruche = cle[1]
        keypath = cle[2]
        key = cle[3]
        keytype = cle[4]
        keyval = cle[5]
        
        
        try:
            regkey = OpenKeyEx(ruche, keypath, 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
        except:
            regkey = CreateKeyEx(ruche, keypath, 0, KEY_ALL_ACCESS|KEY_WOW64_64KEY)
            
        SetValueEx(regkey, key, 0, keytype, keyval)
        CloseKey(regkey)
    c = wmi.WMI ()
    for system in c.Win32_ComputerSystem ():
        system.Rename (hostname)

