package com.greenfoxacademy.webshop.controllers;

import com.greenfoxacademy.webshop.ShopItem;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;



import java.util.*;
import java.util.stream.Collectors;

@Controller
public class MainController {

    protected static List<ShopItem> products = new ArrayList<>(
            List.of(
                    new ShopItem("Shoes", "Running shoes", "shoes for running, Nike brand", 1333, 6),
                    new ShopItem("Car", "Lamborgini", "Car as you wish to have", 100000, 0),
                    new ShopItem("Fruit", "Bananna", "Yellow and tasty", 10000, 50),
                    new ShopItem("Printer", "Hp printer 2223", "Best printer ever", 1004, 9),
                    new ShopItem("Drink", "Coca cola", "When you are thirsty", 166, 0),
                    new ShopItem("T-shirt", "Ramones T", "Ramones Iconic T", 1034, 7),
                    new ShopItem("Pet", "Dog", "very nice and good boy doggie", 1000, 0),
                    new ShopItem("Book", "George Orwell, 1984", "book of the books", 745, 13),
                    new ShopItem("Drink", "Orangina", "orange drink", 125, 5),
                    new ShopItem("Shoes", "Running shoes", "shoes for running, Adidas brand", 1222, 5)
            )
    );

    @GetMapping("/webshop")
    public String welcome(Model model) {

        model.addAttribute("listOfProducts", products);

        return "webshop";
    }

    @GetMapping("/only-available")
    public String availableItems(Model model) {

        List<ShopItem> productsAvailable = products.stream()
                .filter(product -> product.getQuantityOfStock() > 0)
                .toList();
        model.addAttribute("listOfOnlyAvailable", productsAvailable);

        return "onlyavailable";
    }

    @GetMapping("/cheapest-first")
    public String cheapestFirst(Model model) {
        List<ShopItem> cheapest = products.stream()
                .sorted(Comparator.comparing(ShopItem::getPrice))
                .filter(product -> product.getQuantityOfStock() > 0)
                .collect(Collectors.toList());
        model.addAttribute("listOfCheapItems", cheapest);

        return "cheapestfirst";
    }
    @GetMapping("/contains-nike")
    public String containsNike(Model model) {
        List<ShopItem> containsNike = products.stream()
                .filter(product -> product.getType().contains("Shoes"))
                .filter(product -> product.getName().contains("Running shoes"))
                .filter(product -> product.getDescription().contains("Nike"))
                .collect(Collectors.toList());

        model.addAttribute("listContainsNike", containsNike);

        return "containsnike";
    }

    @GetMapping("/average-stock")
    public String avaregeStock(Model model) {

        Long size = products.stream()
                .filter(product -> product.getQuantityOfStock() > 0)
                .count();
        Long sumOfItems = products.stream()
                .filter(product -> product.getQuantityOfStock() > 0)
                .mapToLong(ShopItem::getQuantityOfStock)
                .sum();
        double average = sumOfItems / size;

        model.addAttribute("AverageOfStock", "Average stock: " + average);

        return "averagestock";
    }

    @GetMapping("most-expensive")
    public String mostExpensive(Model model) {
        ShopItem expensiveItem = products.stream()
                .filter(product -> product.getQuantityOfStock() > 0)
                .max(Comparator.comparing(ShopItem::getPrice))
                .orElseThrow(NoSuchElementException::new);

        String item = expensiveItem.getName();

        model.addAttribute("MostExpensive", " Most expensive Item is:  " + item);
        return "mostexpensive";
    }

}