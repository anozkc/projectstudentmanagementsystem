from cx_Freeze import *
includerfiles = ["student.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "win32GUI"

shortcut_table=[
    ("DesktopShortcut", #shortcut
     "DesktopFolder", #Directory
     "studentmanagementsystemComplete", #Name
     "TARGETDIR", #Component_
     "[TARGETDIR]\studentmanagementsystemComplete.exe", #Target
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "Student Management System Developed by ANOJ K.C.",
    author ="Anoj k.c.",
    name="Student Management System",
    options={'build_exe':{'includerfiles': includerfiles}, "bdlist_msi": bdist_msi_options, },
    executables=[
      Executable(
          script="studentmanagementsystemComplete.py",
          base=base,
          icon="student.ico",
      )
    ]

)