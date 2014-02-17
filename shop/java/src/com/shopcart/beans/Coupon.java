package com.shopcart.beans;

public class Coupon {
	private String expire;
	private double miniprice;
	private double discountPrice;
	
	public void setExpire(String expire){
		this.expire = expire;
	}
	
	public String getExpire(){
		return this.expire;
	}
	
	public void setMiniprice(double miniprice){
		this.miniprice = miniprice;
	}
	
	public double getMiniprice(){
		return this.miniprice;
	}
	
	public void setDiscountPrice(double discountPrice){
		this.discountPrice = discountPrice;
	}
	
	public double getDiscountPrice(){
		return this.discountPrice;
	}
	
}
