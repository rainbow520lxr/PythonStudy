<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=gb2312" />
<title>demo</title>
</head>
<script type="text/javascript" src="jquery.js"></script>
<script language="javascript">
	function get_mobile_code(){
        $.get('Post.aspx', {mobile:jQuery.trim($('#mobile').val())}, function(msg) {
            alert(jQuery.trim(unescape(msg)));
			if(msg=='�ύ�ɹ�'){
				RemainTime();
			}
        });
	};
	var iTime = 59;
	var Account;
	function RemainTime(){
		document.getElementById('zphone').disabled = true;
		var iSecond,sSecond="",sTime="";
		if (iTime >= 0){
			iSecond = parseInt(iTime%60);
			iMinute = parseInt(iTime/60)
			if (iSecond >= 0){
				if(iMinute>0){
					sSecond = iMinute + "��" + iSecond + "��";
				}else{
					sSecond = iSecond + "��";
				}
			}
			sTime=sSecond;
			if(iTime==0){
				clearTimeout(Account);
				sTime='��ȡ�ֻ���֤��';
				iTime = 59;
				document.getElementById('zphone').disabled = false;
			}else{
				Account = setTimeout("RemainTime()",1000);
				iTime=iTime-1;
			}
		}else{
			sTime='û�е���ʱ';
		}
		document.getElementById('zphone').value = sTime;
	}	
</script>
<body>
<form action="reg.aspx" method="post" name="formUser" onSubmit="return register();">
	<table width="100%" border="0" align="left" cellpadding="5" cellspacing="3">
		<tr>
		<td align="right">�ֻ�<td>
		<input id="mobile" name="extend_field5" type="text" size="25" class="inputBg" /><span style="color:#FF0000"> *</span> 
        <input id="zphone" type="button" value=" �����ֻ���֤�� " onClick="get_mobile_code();"></td>
        </tr>
		<tr>
			<td align="right">��֤��</td>
			<td><input type="text" size="8" name="captcha" class="inputBg" /></td>
		</tr>
	</table>
</form>
</body>
</html>