package com.greenfoxacademy.webshop.controllers;

import com.greenfoxacademy.webshop.ShopItem;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;
import java.util.stream.Collectors;

import static com.greenfoxacademy.webshop.controllers.MainController.products;

@Controller
public class SearchController {


    @GetMapping("/search")
    public String generateSearch() {
        return "search";
    }

    @PostMapping("/search")
    public String searchedItem(Model model, @RequestParam
                               String searchedItem){

        List<ShopItem> searchedItemList = products.stream()
                .filter(product -> product.getType().contains(searchedItem) || product.getName().contains(searchedItem)
                        || product.getDescription().contains(searchedItem))
                .collect(Collectors.toList());
       model.addAttribute("SearchedItems", searchedItemList);
       model.addAttribute("item" , searchedItem);
        return "search";
    }
}
