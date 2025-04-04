@echo off
CLS

WHERE python >nul
IF %ERRORLEVEL% NEQ 0 (
    color c 

    ECHO Python is not installed! 
    PAUSE
)

IF NOT EXIST launch.cmd (
    echo python .\src\main.py > launch.cmd
) ELSE (
    color c
    echo Already installed!
    
    pause
    exit 

    color
)

color e 

echo Installing Requirements...

pip install -r requirements.txt

CLS

echo Installing Requirements...done

color 2

CLS

echo SUCCESS! Winlocky has been installed. 

pause