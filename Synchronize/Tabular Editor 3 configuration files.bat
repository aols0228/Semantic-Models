@echo off
chcp 65001 > nul
echo:

echo Deletes and copies Tabular Editor 3 configuration files via parental folder
echo.


REM -----Definition of where to copy from-----
REM Define the directory of the current script
set "currentDir=%~dp0"
REM Use the for loop to set the parental directory with a backslash in the end
for %%A in ("%currentDir%..\") do set "parentalDir=%%~dpA"
REM Determine the DAP model configuration files directory
set "ModelAppDataDir=%parentalDir%Configuration Files\"
echo %ModelAppDataDir%
echo.

REM -----Definition of where to copy to-----
REM Define the directory of Tabular Editor 3 configuration files
set "tabularEditor3Dir=C:\Users\%USERNAME%\AppData\Local\TabularEditor3"


REM -----The copy action phase-----
REM Call the Git operations script
ReM call "%currentDir%\Git-scripts - Pull.bat" "%parentalDir%" "%currentDir%"

REM Loop through JSON files in the DAP model configuration files directory and call the copy subroutine
for %%f in ("%ModelAppDataDir%\*.json") do (
    call :copyFile "%%f"
)

REM Pause to keep the Command Prompt window open
pause
goto :eof

:copyFile
REM Subroutine to handle file copying
REM Parameters:
REM %1 - File path
set "destFile=%tabularEditor3Dir%\%~nx1"

if exist "%destFile%" (
    del /Q "%destFile%"
    echo %~nx1 deleted.
)

copy /Y "%~1" "%destFile%" > nul
echo %~nx1 copied.
echo.

goto :eof