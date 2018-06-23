chcp 65001
REM c:
REM cd \pwb
REM c:\Python35\python.exe ParserTempates_SlovariYandex.py %1

REM SET PythonPath = C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Lib\lib-tk;C:\Python27\;C:\Python27\Scripts;D:\scripts.my\vladi_commons;c:\pwb;c:\pwb\scripts;%PythonPath%
REM SET Path = C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Lib\lib-tk;C:\Python27\;C:\Python27\Scripts;D:\scripts.my\vladi_commons;c:\pwb;c:\pwb\scripts;%Path%


REM c:\python34\python \\VBOXSVR\data\scripts.my\4wiki\awb_regexp_replacing_onpage.py %1
rem \\VBOXSVR\data\scripts.my\4wiki\AWBpyScriptRun.bat

d:
cd \scripts.my\4wiki
REM python awb_regexp_replacing_onpage.py %1
python awb_remove_params_from_tpl.py %1
REM pause