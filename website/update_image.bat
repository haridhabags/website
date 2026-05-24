@echo off
REM Simple batch script to update images
REM Usage: update_image.bat old_image.png new_image.png

if "%~2"=="" (
    echo Usage: update_image.bat old_image.png new_image.png
    echo Example: update_image.bat 11.png 5.png
    exit /b 1
)

set OLD_IMAGE=%1
set NEW_IMAGE=%2
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%

echo Updating %OLD_IMAGE% to %NEW_IMAGE% with timestamp %TIMESTAMP%

powershell -Command "(Get-Content index.html) -replace 'assets/images/tote_bags_catlog/%OLD_IMAGE%', 'assets/images/tote_bags_catlog/%NEW_IMAGE%?v=%TIMESTAMP%' | Set-Content index.html"

echo Image updated successfully!
echo Don't forget to upload the new image file to the server.