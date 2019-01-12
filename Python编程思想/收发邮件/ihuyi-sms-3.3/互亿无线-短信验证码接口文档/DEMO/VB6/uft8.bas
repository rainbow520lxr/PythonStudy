Attribute VB_Name = "UTF8"
Private Declare Function WideCharToMultiByte Lib "kernel32" (ByVal CodePage As Long, ByVal dwFlags As Long, ByVal lpWideCharStr As Long, ByVal cchWideChar As Long, ByRef lpMultiByteStr As Any, ByVal cchMultiByte As Long, ByVal lpDefaultChar As String, ByVal lpUsedDefaultChar As Long) As Long
Private Declare Function MultiByteToWideChar Lib "kernel32" (ByVal CodePage As Long, ByVal dwFlags As Long, ByVal lpMultiByteStr As Long, ByVal cchMultiByte As Long, ByVal lpWideCharStr As Long, ByVal cchWideChar As Long) As Long
Private Const CP_UTF8 = 65001

Public Function Utf8ToUnicode(ByRef Utf() As Byte) As String
    Dim lRet As Long
    Dim lLength As Long
    Dim lBufferSize As Long
    lLength = UBound(Utf) - LBound(Utf) + 1
    If lLength <= 0 Then Exit Function
    lBufferSize = lLength * 2
    Utf8ToUnicode = String$(lBufferSize, Chr(0))
    lRet = MultiByteToWideChar(CP_UTF8, 0, VarPtr(Utf(0)), lLength, StrPtr(Utf8ToUnicode), lBufferSize)
    If lRet <> 0 Then
    Utf8ToUnicode = Left(Utf8ToUnicode, lRet)
    End If
End Function

Public Function URLEncode(vstrIn)
   strReturn = ""
   Dim I
   For I = 1 To Len(vstrIn)
   ThisChr = Mid(vstrIn, I, 1)
   If Abs(Asc(ThisChr)) < &HFF Then
   strReturn = strReturn & ThisChr
   Else
   innerCode = Asc(ThisChr)
  If innerCode < 0 Then
  innerCode = innerCode + &H10000
  End If
  Hight8 = (innerCode And &HFF00) \ &HFF
  Low8 = innerCode And &HFF
  strReturn = strReturn & "%" & Hex(Hight8) & "%" & Hex(Low8)
  End If
  Next
  strReturn = Replace(strReturn, Chr(32), "%20")
  strReturn = Replace(strReturn, "+", "%2B")
  strReturn = Replace(strReturn, " ", "+")
  strReturn = Replace(strReturn, vbCrLf, "%0D%0A")
  strReturn = Replace(strReturn, "#", "%23")
  URLEncode = strReturn
End Function
