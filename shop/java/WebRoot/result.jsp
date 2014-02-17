<%@ page language="java" import="java.util.*" pageEncoding="GBK"%>
<%@ page import="com.shopcart.model.CartManager" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>Shop Cart Result</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
    <% 
    	request.setCharacterEncoding("GBK"); 
    	String inputinfo = request.getParameter("input"); 
    	 
    	CartManager carmgr = new CartManager(); 
    	double allprice = carmgr.caculate(inputinfo); 
    	 
    	out.print("Total = " + allprice); 
     %>
  </body>
</html>
