<?php
/**
 * Socket PHP客户端
 *
 */
header ( 'Content-type:text/html;charset=utf8' );
//$host = 'tcp://192.168.168.118:8008';
$host = 'tcp://localhost:8001';
$fp = stream_socket_client ( $host, $errno, $error, 30 );
if (! $fp) {

    echo "$error ($errno)\n";
} else {
    $arr=array('username'=>'陈鹏欢','password'=>'123123');
    fwrite ( $fp,json_encode($arr));
    while ( ! feof ( $fp ) ) {
        echo fgets ($fp );
#获取服务器返回的内容
    }
    fclose ( $fp );
}
?>
