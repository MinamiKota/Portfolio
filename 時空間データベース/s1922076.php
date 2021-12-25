<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>スポット検索アプリ</title>
</head>
<body>
<h1>スポット検索アプリ</h1>
<form action="./s1922076.php" method="POST">
<p>入力した座標の5km以内のスポットを表示する</p>
経度　<input type="text" size="50" name="longitude"><br>
緯度　<input type="text" size="50" name="latitude"><br>
<input type="submit" value="実行">
</form>
<?php
$longitude=$_POST["longitude"];
$latitude=$_POST["latitude"];
$query = "select id, name, cat, lon, lat, location<->ST_GeomFromText('POINT($longitude $latitude)',4326) as distance from spot where location<->ST_GeomFromText('POINT($longitude $latitude)',4326) < 5000 order by distance;";
if(empty($longitude) || empty($latitude)){$query = "SELECT * FROM spot;";}else{echo "経度：".$longitude." 緯度：".$latitude." から5km以内のスポット 距離が近い順\n";}
$dbconn = pg_connect("host=localhost dbname=s1922076 user=s1922076 password=yyxLFDvX") or die('Could not connect: ' . pg_last_error());
$result = pg_query($query) or die('Query failed: ' . pg_last_error());
echo "<table>\n";
while ($line = pg_fetch_array($result,null,PGSQL_ASSOC)){
    echo "\t<tr>\n";
    foreach($line as $col_value){echo "\t\t<td>$col_value</td>\n";}
    echo "\t</tr>\n";
}
echo "</table>\n";
?>
</body>
</html>