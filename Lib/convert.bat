@ GOTO EndComment
	convert.bat

	Written by John Lukowski 12/29/2017 (lukowskijohn@gmail.com)
	For the purpose of using unovonv and libreoffice
	to convert dcx files to pdf's
:EndComment

@ REM echo off
 cmd /c unoconv -f pdf -o %~dp0..\Final_Product.pdf output.docx
REM cmd /c del output.docx