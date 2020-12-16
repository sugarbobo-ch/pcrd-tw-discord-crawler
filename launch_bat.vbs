Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "YOUR_PROJECT_FOLDER_PATH" & Chr(34), 0
Set WshShell = Nothing