@echo off
setlocal EnableDelayedExpansion
chcp 65001 > nul
echo:

REM Define error handling content
set "ERROR_HANDLER=(
    echo Automatisk opdatering af GitHub virker endnu ikke i denne arbejdsgang.
	echo Gør i stedet følgende:
    echo(
    echo Opdater GitHub manuelt:
    echo 1. Åben programmet GitHub Desktop
    echo 2. Klik på "Current repository" og skift repository til "PowerBI-Bibliotek"
    echo 3. Klik "Fetch origin"
    echo 4. Klik "Pull"
    echo 5. Gå tilbage til dette vindue og klik på en tast for at fortsætte
    echo(
    REM det virker alligevel ikke pt.
	REM pause
    exit /b 1
)"

REM Fetch updates for all branches
REM git fetch
REM IF ERRORLEVEL 1 (
REM     call !ERROR_HANDLER!
REM ) ELSE (
    REM Pull changes from the 'main' branch if fetch was successful
REM     git pull
REM )

REM Reuse the error handling block if another error occurs
REM You can simulate another error condition here
REM set /a simulateError=1
REM IF !simulateError! EQU 1 (
REM     call !ERROR_HANDLER!
REM )


call !ERROR_HANDLER!



REM Final pause before exiting
REM pause
