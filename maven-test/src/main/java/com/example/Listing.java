package com.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Listing {
    public static void main(String[] args) {
        // 文字列操作: 前後の空白をトリムする
        String input = " hello world ";
        String trimmed = input.trim();
        System.out.println("Trimmed String: " + trimmed);

        // リスト操作: リストを作成して不変リストに変換する
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("cherry");

        // 不変リストを作成する (Collections.unmodifiableListを使用)
        List<String> immutableList = Collections.unmodifiableList(list);
        System.out.println("Immutable List: " + immutableList);

        // リストの要素を大文字に変換
        List<String> upperList = new ArrayList<>();
        for (String item : list) {
            upperList.add(item.toUpperCase());
        }
        System.out.println("Uppercase List: " + upperList);
    }
}

