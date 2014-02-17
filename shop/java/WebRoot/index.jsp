<%@ page language="java" import="java.util.*" pageEncoding="GBK"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>Shop Cart</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
	
	<script>
		function $(o){
			return document.getElementById(o);
		}
	</script>
  </head>
  
  <body>
  	<form name="calform" action="result.jsp" method="post" >
  		<textarea name="input" id="text" style="width:200px;height:300px;">2013.11.11 | 0.7 | 电子

1 * ipad : 2399.00
1 * 显示器: 1799.00
12 * 啤酒 : 25.00
5 * 面包 :9.00

2013.11.11
2014.3.2 1000 200</textarea>
		<Br />
		<input type="submit" value="calculate" id="calculate" />
		<Br />
  	</form>   
  	
  	<a href="javascript:void 0" id="test1">testCase 1</a>
	<a href="javascript:void 0" id="test2">testCase 2</a>
 
 	<script>
 		//test case 1
		$('test1').onclick = function(){
		$('text').value = '2013.11.11 | 0.7 | 电子\r\n\
\r\n\
1 * ipad : 2399.00\r\n\
1 * 显示器: 1799.00\r\n\
12 * 啤酒: 25.00\r\n\
5 * 面包: 9.00\r\n\
\r\n\
2013.11.11\r\n\
2014.3.2 1000 200 ';
}
		//test case 2
		$('test2').onclick = function(){
		$('text').value = '3 * 蔬菜 :5.98\r\n\
8 * 餐巾纸: 3.20\r\n\
\r\n\
2014.01.01';
	
}
	
 	</script>
  </body>
</html>
