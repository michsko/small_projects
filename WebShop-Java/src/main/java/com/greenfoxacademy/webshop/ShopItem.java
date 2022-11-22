package com.greenfoxacademy.webshop;

import javax.naming.InsufficientResourcesException;
import java.math.BigDecimal;
import java.text.DecimalFormat;

public class ShopItem {
    private String type;
    private String name;
    private String description;
    private Integer price;
    private Integer quantityOfStock;

    private String currency;

    public ShopItem(String type, String name, String description, Integer price, Integer quantityOfStock) {
        this.type = type;
        this.name = name;
        this.description = description;
        this.price = price;
        this.quantityOfStock = quantityOfStock;
        this.currency = " $ ";

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Integer getPrice() {

        return price;
    }

    public void setPrice(Integer price) {
        this.price = price;
    }

    public Integer getQuantityOfStock() {
        return quantityOfStock;
    }

    public void setQuantityOfStock(Integer quantityOfStock) {
        this.quantityOfStock = quantityOfStock;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}
