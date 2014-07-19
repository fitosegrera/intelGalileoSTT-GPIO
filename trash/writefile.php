<?

if ($_POST['content']=="ktd")
  {  

	$gpio3 = file_get_contents('/sys/class/gpio/gpio3/value');

	if ($gpio3 == 1)
	{
	file_put_contents('/sys/class/gpio/gpio3/value',"0");
	}
	elseif ($gpio3 == 0)
         {file_put_contents('/sys/class/gpio/gpio3/value',"1");
	}
   



  }
elseif ($_POST['content']=="zwd")

	  {
	$io3 = file_get_contents('/sys/class/gpio/gpio18/value');

	if ($io3 == 1)
	{
	file_put_contents('/sys/class/gpio/gpio18/value',"0");
	}
	elseif ($io3 == 0)
         {file_put_contents('/sys/class/gpio/gpio18/value',"1");
	  }
	}

elseif ($_POST['content']=="sfd")

	  {
	$io2 = file_get_contents('/sys/class/gpio/gpio32/value');

	if ($io2 == 1)
	{
	file_put_contents('/sys/class/gpio/gpio32/value',"0");
	}
	elseif ($io2 == 0)
         {file_put_contents('/sys/class/gpio/gpio32/value',"1");
	  }
	}
elseif ($_POST['content']=="cl")

	  {

	$io13 = file_get_contents('/sys/class/gpio/gpio39/value');

	
	if ($io13 == 1)
	{
	file_put_contents('/sys/class/gpio/gpio24/value',"0");
	usleep(800000);

	file_put_contents('/sys/class/gpio/gpio24/value',"1");
	file_put_contents('/sys/class/gpio/gpio39/value',"0");
	}
	elseif ($io13 == 0)
         {file_put_contents('/sys/class/gpio/gpio27/value',"0");
	  usleep(800000);
	  file_put_contents('/sys/class/gpio/gpio27/value',"1");
	file_put_contents('/sys/class/gpio/gpio39/value',"1");
	  }
	}
elseif ($_POST['content']=="ch")

	  {

	$io12 = file_get_contents('/sys/class/gpio/gpio38/value');

	
	if ($io12 == 1)
	{
	file_put_contents('/sys/class/gpio/gpio28/value',"0");
	usleep(600000);

	file_put_contents('/sys/class/gpio/gpio28/value',"1");


	file_put_contents('/sys/class/gpio/gpio17/value',"0");


	  usleep(600000);
	  file_put_contents('/sys/class/gpio/gpio17/value',"1");
	file_put_contents('/sys/class/gpio/gpio38/value',"1");
	  
	}
	}






























elseif ($_POST['content']=="zz")

	  {file_put_contents('/www/pages/a.txt',"004");

	  }






//echo $_POST['content'];


//header ("Cache-Control: no-cache, must-revalidate");
//   $stt = file_get_contents("a.txt");
//   echo "<script language=javascript>alert('$stt');</script>";






?>