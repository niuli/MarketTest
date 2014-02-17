package com.shopcart.model;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import com.shopcart.beans.*;;

public class CartManager {
	private ArrayList<Item> itemlist;
	private HashMap<String, Discount> discountlist;
	private ArrayList<Coupon> couponlist;
	private String ordertime;
	
	private static ArrayList<Category> catelist;
	
	public static void addCategory(String cate, String[] list){
		Category category = new Category();
		category.setCate(cate);
		category.setCateList(list);
		catelist.add(category);
	}
	
	public static void initCatelist(){
		catelist = new ArrayList<Category>();
		
		String [] list1 = {"ipad","iphone","显示器","笔记本电脑","键盘"};
		addCategory("电子", list1);
		
		String [] list2 = {"面包","饼干","蛋糕","牛肉","鱼","蔬菜"};
		addCategory("食品", list2);
		
		String [] list3 = {"餐巾纸","收纳箱","咖啡杯","雨伞"};
		addCategory("日用品", list3);
		
		String [] list4 = {"啤酒","白酒","伏特加"};
		addCategory("酒类", list4);
	}
	
	public double caculate(String inputString){
		//初始化分类列表
		initCatelist();
		
		double allprice = 0.0;
		
		if(itemlist == null)
			itemlist = new ArrayList<Item>();
		
		if(discountlist == null)
			discountlist = new HashMap<String, Discount>();
		
		if(couponlist == null)
			couponlist = new ArrayList<Coupon>();
		
		//split all lines
		String[] lines = inputString.trim().split("\n");
		for(int i =0, l=lines.length, mode = 0; i<l;i++){
			String line = lines[i].trim();
			if(line.length() == 0){
				mode++;
				continue;
			}
			//has no discount
			if(mode == 0 && line.indexOf("*") != -1){
				mode = 1;
			}
			switch(mode){
				case 0:
					//discount
					String[] arr = line.split(" \\| ");
					Discount disc = new Discount();
					disc.setTime(arr[0]);
					disc.setDiscount(Double.parseDouble(arr[1]));					
					discountlist.put(arr[2].trim(), disc);					
					break;
					
				case 1://items
					String [] part1 = line.split(" \\* ");;
					String [] part2 = part1[1].split(":");								
					
					Item item = new Item();
					item.setNum(Integer.parseInt(part1[0].trim()));
					item.setName(part2[0].trim());
					item.setPrice(Double.parseDouble(part2[1].trim()));
					itemlist.add(item);								
					break;
					
				case 2://ordertime
						
					ordertime = line.trim();
					//unset expire discount
					HashMap<String, Discount> newDiscountList = new HashMap<String, Discount>();
					for (Iterator<String> it = discountlist.keySet().iterator(); it.hasNext();) { 
						String cate = it.next();
						if(((Discount)discountlist.get(cate)).getTime().compareTo(ordertime) >= 0){
							Discount distmp = discountlist.get(cate);
							newDiscountList.put(cate, distmp);
						}											
					} 				
					discountlist = newDiscountList;					
					mode++;
					break;
					
				case 3://coupon
					String [] attr = line.split(" ");
					
					Coupon coupon = new Coupon();
					coupon.setExpire(attr[0]);
					coupon.setMiniprice(Double.parseDouble(attr[1]));
					coupon.setDiscountPrice(Double.parseDouble(attr[2]));
					
					couponlist.add(coupon);
					
					break;
				}
			}
		
			for(int i=0,j=itemlist.size();i<j;i++){
				String currentCate = getItemCate(itemlist.get(i).getName());
				double currentPrice = itemlist.get(i).getPrice() * itemlist.get(i).getNum();
				
				if(currentCate != null && discountlist.containsKey(currentCate)){
					currentPrice *= discountlist.get(currentCate).getDiscount();
				}
				
				allprice += currentPrice;
			}
			
			for(int i=0,j=couponlist.size();i<j;i++){
				if(couponlist.get(i).getExpire().compareTo(ordertime)>=0 && allprice >= couponlist.get(i).getMiniprice()){
					allprice -= couponlist.get(i).getDiscountPrice();
				}
			}
			
			DecimalFormat dFormat = new DecimalFormat("0.00");			
			return Double.parseDouble(dFormat.format(allprice));				
	}

	public String getItemCate(String name){
		for(int i = 0; i< catelist.size(); ++i){
			Category category = catelist.get(i);
			String [] list = category.getCateList();
			int j = list.length;			
			while(j-- > 0){
				if(name.compareTo(list[j]) == 0){
					return category.getCate();
				}
			}
		}
		return null;
	}
}
