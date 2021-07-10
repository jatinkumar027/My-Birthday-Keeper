; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7CADEF12-08DC-4336-921A-872DA232DA5B}
AppName=My Birthday Keeper
AppVersion=0.0.1
;AppVerName=My Birthday Keeper 0.0.1
AppPublisher=Jatin Inc.
DefaultDirName={autopf}\My Birthday Keeper
DisableProgramGroupPage=yes
LicenseFile=C:\Users\User\Desktop\BIRTHDAY_PROJECT\license.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\User\Desktop\BIRTHDAY_PROJECT\Setup
OutputBaseFilename=mybirthdaykeeper_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=  C:\Users\User\Desktop\BIRTHDAY_PROJECT\myicon.ico
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\dist\bdayscript.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\Analysis-00.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\bdayscript.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\EXE-00.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\PKG-00.pkg"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\PKG-00.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\PYZ-00.pyz"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\PYZ-00.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\Tree-00.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\Tree-01.toc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\warn-bdayscript.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\build\bdayscript\xref-bdayscript.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\__pycache__\bdayscript.cpython-38.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\bdaydb.sqlite"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\bdayscript.spec"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\license.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\BIRTHDAY_PROJECT\myicon.ico"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\My Birthday Keeper"; Filename: "{app}\bdayscript.exe"
Name: "{autodesktop}\My Birthday Keeper"; Filename: "{app}\bdayscript.exe"; Tasks: desktopicon
Name: "{autoprograms}\My Birthday Keeper"; Filename: "{app}\bdayscript.exe"; IconFilename:"{app}\myicon.ico"
Name: "{autodesktop}\My Birthday Keeper"; Filename: "{app}\bdayscript.exe";  IconFilename:"{app}\myicon.ico"

[Run]
Filename: "{app}\bdayscript.exe"; Description: "{cm:LaunchProgram,My Birthday Keeper}"; Flags: nowait postinstall skipifsilent

