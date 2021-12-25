<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>第二回課題</title>
</head>
<body>
<h1>星座判定 s1922076 南昂汰</h1>
<form action="./20210608.php" method="POST">
誕生月　<input type="text" size="5" name="month"><br>
誕生日　<input type="text" size="5" name="date"><br>
<input type="submit" value="実行">
</form>
<?php
$month=$_POST["month"];
$date=$_POST["date"];
$result="入力内容が不適正";
if($month==3  && $date>=21 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので おひつじ座 です";}
if($month==4  && $date>=1  && $date<=19){$result="あなたは ".$month."月".$date."日 生まれなので おひつじ座 です";}
if($month==4  && $date>=20 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので おうし座 です";}
if($month==5  && $date>=1  && $date<=20){$result="あなたは ".$month."月".$date."日 生まれなので おうし座 です";}
if($month==5  && $date>=21 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので ふたご座 です";}
if($month==6  && $date>=1  && $date<=21){$result="あなたは ".$month."月".$date."日 生まれなので ふたご座 です";}
if($month==6  && $date>=22 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので かに座 です";}
if($month==7  && $date>=1  && $date<=22){$result="あなたは ".$month."月".$date."日 生まれなので かに座 です";}
if($month==7  && $date>=23 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので しし座 です";}
if($month==8  && $date>=1  && $date<=22){$result="あなたは ".$month."月".$date."日 生まれなので しし座 です";}
if($month==8  && $date>=23 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので おとめ座 です";}
if($month==9  && $date>=1  && $date<=22){$result="あなたは ".$month."月".$date."日 生まれなので おとめ座 です";}
if($month==9  && $date>=23 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので てんびん座 です";}
if($month==10 && $date>=1  && $date<=23){$result="あなたは ".$month."月".$date."日 生まれなので てんびん座 です";}
if($month==10 && $date>=24 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので さそり座 です";}
if($month==11 && $date>=1  && $date<=22){$result="あなたは ".$month."月".$date."日 生まれなので さそり座 です";}
if($month==11 && $date>=23 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので いて座 です";}
if($month==12 && $date>=1  && $date<=21){$result="あなたは ".$month."月".$date."日 生まれなので いて座 です";}
if($month==12 && $date>=22 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので やぎ座 です";}
if($month==1  && $date>=1  && $date<=19){$result="あなたは ".$month."月".$date."日 生まれなので やぎ座 です";}
if($month==1  && $date>=20 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので みずがめ座 です";}
if($month==2  && $date>=1  && $date<=18){$result="あなたは ".$month."月".$date."日 生まれなので みずがめ座 です";}
if($month==2  && $date>=19 && $date<=31){$result="あなたは ".$month."月".$date."日 生まれなので うお座 です";}
if($month==3  && $date>=1  && $date<=20){$result="あなたは ".$month."月".$date."日 生まれなので うお座 です";}
echo $result;
?>
</body>
</html>