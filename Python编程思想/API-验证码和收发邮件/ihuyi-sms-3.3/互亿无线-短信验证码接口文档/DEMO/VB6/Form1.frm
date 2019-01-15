VERSION 5.00
Object = "{248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0"; "MSWINSCK.OCX"
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   4740
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   5940
   LinkTopic       =   "Form1"
   ScaleHeight     =   4740
   ScaleWidth      =   5940
   StartUpPosition =   2  '屏幕中心
   Begin MSWinsockLib.Winsock Winsock1 
      Left            =   4920
      Top             =   4200
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   393216
   End
   Begin VB.TextBox Text4 
      Height          =   270
      Left            =   360
      TabIndex        =   4
      Text            =   $"Form1.frx":0000
      Top             =   1200
      Width           =   5415
   End
   Begin VB.TextBox Text3 
      Height          =   270
      Left            =   360
      TabIndex        =   3
      Text            =   "手机号码"
      Top             =   840
      Width           =   3495
   End
   Begin VB.TextBox Text2 
      Height          =   270
      Left            =   360
      TabIndex        =   2
      Text            =   "密码可以使用明文密码或使用32位MD5加密"
      Top             =   480
      Width           =   3495
   End
   Begin VB.TextBox Text1 
      Height          =   270
      Left            =   360
      TabIndex        =   1
      Text            =   "用户名"
      Top             =   120
      Width           =   3495
   End
   Begin VB.CommandButton Command1 
      Caption         =   "提 交"
      Height          =   495
      Left            =   4440
      TabIndex        =   0
      Top             =   240
      Width           =   1215
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      Caption         =   "Label2"
      Height          =   180
      Left            =   360
      TabIndex        =   6
      Top             =   2160
      Visible         =   0   'False
      Width           =   540
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "状态"
      Height          =   180
      Left            =   360
      TabIndex        =   5
      Top             =   1920
      Width           =   360
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Form_Load()
    Winsock1.Protocol = sckTCPProtocol
    Winsock1.RemoteHost = "106.ihuyi.cn"
    Winsock1.RemotePort = 80
    Winsock1.Connect
    DoEvents
        
    If Winsock1.State <> 7 Then Label1.Caption = "状态：服务器连接成功" & Chr(13)
        
    Text1.Text = "用户名"
    Text2.Text = "密码可以使用明文密码或使用32位MD5加密"
    Text3.Text = "手机号码&coding=GBK"    '&coding=GBK不要删除
        
End Sub
Private Sub Command1_Click()

    On Error Resume Next

    Dim PostData As String
    Dim Str As String
     
    Dim strWebPage As String
    Dim strCommand As String
        
    PostData = "account=" + Text1.Text + "&password=" + Text2.Text + "&mobile=" + Text3.Text + "&content=" + Text4.Text
    
    Dim Ai() As Byte
    Ai = StrConv(strWebPage, vbFromUnicode)
    CLength = UBound(Ai) + 1
    Str = "POST /webservice/sms.php?method=Submit HTTP/1.1" + vbCrLf
    Str = Str + "Accept: */*" + vbCrLf
    Str = Str + "Content-Type: application/x-www-form-urlencoded" + vbCrLf
    Str = Str + "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; Maxthon; .NET CLR 1.1.4322)" & vbCrLf
    Str = Str + "Language: zh-CN, zh, *" + vbCrLf
    Str = Str + "Connection: Keep-Alive" + vbCrLf
    Str = Str + "Host: 106.ihuyi.cn" + vbCrLf
    Str = Str + "Accept-Language: zh-CN, zh, *" + vbCrLf
    Str = Str + "Accept-Encoding: gzip, deflate" & vbCrLf
    Str = Str & "Content-Length: " & Len(PostData) & vbCrLf & vbCrLf
    Str = Str & PostData & vbCrLf
    'MsgBox str

    
    strWebPage = "http://106.ihuyi.cn/webservice/sms.php?method=Submit&account=" + Text1.Text + "&password=" + Text2.Text + "&mobile=" + Text3.Text + "&content=" + Text4.Text
    strCommand = "GET " + strWebPage + " HTTP/1.0" + vbCrLf
    strCommand = strCommand + vbCrLf
    
    
    If Winsock1.State <> 7 Then
        Winsock1.Protocol = sckTCPProtocol
        Winsock1.RemoteHost = "106.ihuyi.cn"
        Winsock1.RemotePort = 80
        Winsock1.Connect
        DoEvents
        Winsock1.SendData Str
    Else
        Winsock1.SendData strCommand
    End If
    


    'Label1.Caption = "状态：" & strState & Chr(13) & strCommand & Chr(13)
    
End Sub


Private Sub Winsock1_DataArrival(ByVal bytesTotal As Long)
Dim rec() As Byte
Winsock1.GetData rec, vbString
'MsgBox Utf8ToUnicode(Right(rec, 150))

Label2.Visible = True
Label2.Caption = Utf8ToUnicode(rec)

Winsock1.Close
End Sub
