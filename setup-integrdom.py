#!/usr/bin/env python
# _*_ coding: iso-8859-1 _*_

from distutils.core import setup
import py2exe
import os, shutil,glob

from manifest import manifest

os.environ['path']='%s;%s'%(os.environ['path'], os.path.join(os.path.abspath('.'), 'dlls'))

dist_dir = "dists\\integrdom7"
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)

if os.path.exists("build"):
    shutil.rmtree("build")
includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
opts = {"py2exe": {
    "dist_dir": dist_dir,
    "packages":["encodings",],
    "optimize":2,
    "bundle_files": 1,
    "compressed": 2,
    "xref": False,
    "skip_archive": False,
    "ascii": False,
    "includes": includes,
    "excludes": excludes,
    "packages": packages,
    "dll_excludes": dll_excludes,	   
}}
# recuperation des chemins contenant les DLLs
dll1 = os.path.join(os.path.abspath('.'), 'Py26dlls.MFC')
dll2 = os.path.join(os.path.abspath('.'), 'Py26dlls.MSV')
# Ajout de ces chemins au %PATH%
os.environ['path']=';'.join([os.environ['path'], dll1, dll2])
# Ajout des DLLS aux 'data_files'
Py26dllsMFC = glob.glob(r"Py26dlls.MFC\*.*")
Py26dllsMSV = glob.glob(r"Py26dlls.MSV\*.*")

setup(name = 'IntegrDom7',
      version = '1.0',
      description = 'Utilitaire de jonction au domaine Scribe',
      author = '',
      author_email = '',
      options=opts,
      url = '',
      windows = [{'script': 'integrdom7.py',
	      	'uac_info': "requireAdministrator",
                #'other_resources': [(24, 1, manifest%{'prog': 'IntegrDom7'})],
                'icon_resources': [(1, 'eole.ico')]
                }],

      data_files=[('', ['eole.ico']),
     		  ('', Py26dllsMSV),
              	  ('', Py26dllsMFC) 
	          #('', ['MSVCP71.dll']),
      ],
      zipfile = None,
      )


