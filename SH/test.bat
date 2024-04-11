@echo off

REM Get the file extension
set filename=%1
set ext=%filename:~-2%

REM Check if the file is a C or C++ file
if "%ext%" == ".c" (
    gcc %1 -o test
) else if "%ext%" == "pp" (
    g++ %1 -o test
) else (
    echo Unsupported file format
    goto end
)

REM Check compilation result
if %ERRORLEVEL% NEQ 0 goto error

REM Execute the compiled file
test

goto end

:error
echo Compilation failed!

:end
