package com.shopcart.beans;

public class Category {
	private String cate;
	private String [] catelist;
	
	public void setCate(String cate){
		this.cate = cate;
	}
	
	public String getCate(){
		return this.cate;
	}
	
	public void setCateList(String [] catelist){
		this.catelist = catelist;
	}
	
	public String [] getCateList(){
		return this.catelist;
	}
}
