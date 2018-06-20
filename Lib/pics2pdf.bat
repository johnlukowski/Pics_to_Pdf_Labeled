@ GOTO EndComment
	pics2pdf.bat

	Written by John Lukowski 12/27/2017 (lukowskijohn@gmail.com)
	For the purpose of using generate_docx.py to add images to a docx file,
	then converting that file to a pdf with convert.bat
:EndComment

@ ECHO OFF
@ start generate_docx.py

:CheckForFile
IF EXIST "output.docx" GOTO Found

REM File not generated yet, wait for it
TIMEOUT /T 1 >nul
@ GOTO CheckForFile

:Found
@ start convert.bat