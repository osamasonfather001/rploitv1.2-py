@echo off
setlocal

set "a=RobloxPlayerBeta.exe"

:b
tasklist /FI "IMAGENAME eq %a%" | find /I "%a%" >nul
if %ERRORLEVEL%==0 (
    goto c
) else (
    goto d
)

:c
taskkill /IM "%a%" /F
timeout /t 2 >nul
goto d

:d
start "" "C:\Path\To\RobloxPlayerBeta.exe"
goto e

:e
exit
