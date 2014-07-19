<?

header ("Cache-Control: no-cache, must-revalidate");

//echo  file_get_contents("a.txt");



sleep(0.5);

$gpio3  = file_get_contents('/sys/class/gpio/gpio3/value');
$gpio16 = file_get_contents('/sys/class/gpio/gpio16/value');
$gpio17 = file_get_contents('/sys/class/gpio/gpio17/value');
$gpio18 = file_get_contents('/sys/class/gpio/gpio18/value');
$gpio19 = file_get_contents('/sys/class/gpio/gpio19/value');
$gpio20 = file_get_contents('/sys/class/gpio/gpio20/value');
$gpio21 = file_get_contents('/sys/class/gpio/gpio21/value');
$gpio22 = file_get_contents('/sys/class/gpio/gpio22/value');
$gpio23 = file_get_contents('/sys/class/gpio/gpio23/value');
$gpio24 = file_get_contents('/sys/class/gpio/gpio24/value');
$gpio25 = file_get_contents('/sys/class/gpio/gpio25/value');
$gpio26 = file_get_contents('/sys/class/gpio/gpio26/value');
$gpio27 = file_get_contents('/sys/class/gpio/gpio27/value');
$gpio28 = file_get_contents('/sys/class/gpio/gpio28/value');

$gpio32 = file_get_contents('/sys/class/gpio/gpio32/value');
$gpio36 = file_get_contents('/sys/class/gpio/gpio36/value');
$gpio37 = file_get_contents('/sys/class/gpio/gpio37/value');
$gpio38 = file_get_contents('/sys/class/gpio/gpio38/value');
$gpio39 = file_get_contents('/sys/class/gpio/gpio39/value');

$gpio3= str_replace("\n","",$gpio3);
$gpio16= str_replace("\n","",$gpio16);
$gpio17= str_replace("\n","",$gpio17);
$gpio18= str_replace("\n","",$gpio18);
$gpio19= str_replace("\n","",$gpio19);
$gpio20= str_replace("\n","",$gpio20);
$gpio21= str_replace("\n","",$gpio21);
$gpio22= str_replace("\n","",$gpio22);
$gpio23= str_replace("\n","",$gpio23);
$gpio24= str_replace("\n","",$gpio24);
$gpio25= str_replace("\n","",$gpio25);
$gpio26= str_replace("\n","",$gpio26);
$gpio27= str_replace("\n","",$gpio27);
$gpio28= str_replace("\n","",$gpio28);

$gpio32= str_replace("\n","",$gpio32);
$gpio36= str_replace("\n","",$gpio36);
$gpio37= str_replace("\n","",$gpio37);
$gpio38= str_replace("\n","",$gpio38);
$gpio39= str_replace("\n","",$gpio39);

$aio0 = file_get_contents('/sys/bus/iio/devices/iio:device0/in_voltage2_raw');
 //  echo $aio0;
	if ($aio0 > 100)
	{
	$aio0 = 1;
	}
	else
         {
	$aio0 = 0;
	}

$aio1 = file_get_contents('/sys/bus/iio/devices/iio:device0/in_voltage0_raw');
//echo $aio1;
	if ($aio1 > 1500)
	{
	$aio1 = 1;
	}
	else
         {
	$aio1 = 0;
	}

$aio2 = file_get_contents('/sys/bus/iio/devices/iio:device0/in_voltage1_raw');
//echo $aio2;
	if ($aio2 > 100)
	{
	$aio2 = 1;
	}
	else
         {
	$aio2 = 0;
	}

$aio3 = file_get_contents('/sys/bus/iio/devices/iio:device0/in_voltage3_raw');

//echo $aio3;
	if ($aio3 > 100)
	{
	$aio3 = 1;
	}
	else
         {
	$aio3 = 0;
	}






$gpio = $gpio3.$gpio16.$gpio17.$gpio18.$gpio19.$gpio20.$gpio21.$gpio22.$gpio23.$gpio24.$gpio25.$gpio26.$gpio27.$gpio28.$gpio32.$gpio36.$gpio37.$gpio38.$gpio39.$aio0.$aio1.$aio2.$aio3;

echo $gpio;














//$stt = file_get_contents('/sys/class/gpio/gpio3/value');
//echo $stt;
//echo "<script language=javascript>alert($aio0);</script>";

?>