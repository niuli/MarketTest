package com.shopcart.beans;

public class Discount {
	private String time;
	private double discount;	
	
	public void setTime(String time){
		this.time = time;
	}
	
	public String getTime(){
		return this.time;
	}
	
	public void setDiscount(double discount){
		this.discount = discount;
	}
	
	public double getDiscount(){
		return this.discount;
	}
		
}
