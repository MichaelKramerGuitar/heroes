@echo off
REM you can use the NODE environment variable to switch between different settings for different nodes or environments
REM set NODE=DEV
cd ..
start "C:\Program Files\Derivative\TouchDesigner\bin\TouchDesigner.exe" "Heroes.toe"
code .
