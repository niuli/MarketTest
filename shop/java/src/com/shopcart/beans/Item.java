package com.shopcart.beans;

public class Item {
	private int num;
	private String name;
	private double price;
	
	public void setNum(int num){
		this.num = num;
	}
	
	public int getNum(){
		return this.num;
	}
	
	public void setName(String name){
		this.name = name;
	}
	
	public String getName(){
		return this.name;
	}

	public void setPrice(double price){
		this.price = price;
	}
	
	public double getPrice(){
		return this.price;
	}
}
