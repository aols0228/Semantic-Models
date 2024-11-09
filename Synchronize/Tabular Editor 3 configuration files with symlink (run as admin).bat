@echo off
setlocal EnableDelayedExpansion
chcp 65001 > nul
echo:


REM -----Definition of where to copy from-----
REM Set the directory of the current script
set "currentDir=%~dp0"

REM Use the for loop to set the parental directory with a backslash in the end
for %%A in ("%currentDir%..\") do set "parentalDir=%%~dpA"

REM Output parent directory
echo Parental directory: %parentalDir%
echo.

REM Opdater Git repo manuelt, da det ikke kan gøres automatisk pga. administratoradgang og dubious access
echo Opdater repo manuelt inden du går i gang:
echo 1. Åben programmet GitHub Desktop
echo 2. Skift repo til DAP-PowerBI-Bibliotek
echo 3. Fetch, pull
echo 4. Gå tilbage til dette vindue og klik på en tast for at fortsætte
echo.
REM pause
echo.

REM Determine the DAP model configuration files directory path
set "ModelAppDataDir=%parentalDir%Model\Configuration Files"
echo Copy from: %ModelAppDataDir%

REM -----Definition of where to copy to-----
REM Define how to extract your user name based on your admin user name
set "shortUSERNAME=%USERNAME:~5%"
REM Define the TabularEditor3 directory
set "tabularEditor3Dir=C:\Users\%shortUSERNAME%\AppData\Local\TabularEditor3"
echo Tabular Editor 3 directory: %tabularEditor3Dir%
echo.


REM -----The copy action phase-----
REM Loop through JSON files in the DAP configuration files directory and create hard links
for %%f in ("%ModelAppDataDir%\*.json") do (
    REM Extract filename from the path
    set "fileName=%%~nxf"
    REM Check if the hard link already exists in the target directory
    if exist "%tabularEditor3Dir%\!fileName!" (
        REM Delete the existing hard link
        del /Q "%tabularEditor3Dir%\!fileName!"
    )

REM Create the symlink
REM mklink /H "%tabularEditor3Dir%\%%~nxf" "%%f"
    echo Creating symlink for: %%f
	mklink "%tabularEditor3Dir%\!fileName!" "%%f"
	
    if %ERRORLEVEL% == 0 (
        echo symlink !fileName! created successfully.
    ) else (
        echo ERROR: Failed to create symlink for !fileName!.
    )
	echo.
)

REM Pause to keep the Command Prompt window open
pause