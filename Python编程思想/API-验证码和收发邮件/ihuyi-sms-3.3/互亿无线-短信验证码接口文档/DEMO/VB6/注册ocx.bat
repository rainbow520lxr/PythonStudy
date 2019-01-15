@echo off
copy Mswinsck.OCX %windir%\system32\
regsvr32 Mswinsck.OCX