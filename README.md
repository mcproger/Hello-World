[![travis build](https://img.shields.io/travis/voron434/styleru_py_week1.svg?style=flat-square)](https://travis-ci.org/voron434/styleru_py_week1)
[![codecov coverage](https://img.shields.io/codecov/c/github/voron434/styleru_py_week1.svg?style=flat-square)](https://codecov.io/github/voron434/styleru_py_week1)
[![version](https://img.shields.io/npm/v/styleru_py_week1.svg?style=flat-square)](http://npm.im/styleru_py_week1)
[![downloads](https://img.shields.io/npm/dm/styleru_py_week1.svg?style=flat-square)](http://npm-stat.com/charts.html?package=styleru_py_week1&from=2015-08-01)
[![MIT License](https://img.shields.io/npm/l/styleru_py_week1.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg?style=flat-square)](https://github.com/semantic-release/semantic-release) 


# Work with TMDB data #

This work consist of four programs written in Python 3.x. This programs introduce user with TMDB BaseData and allow to create your own DataBase and work with it. 

# 1. api_TMBD #

This program makes clear how work TMDB. You should to enter your api_key_v3 and program will show you budget of film "Saw II (Пила 2)" (id №215 on TMBD)

### Example of api key v3 ###
1ebe2aa78b39fafdbbf3f9e6833a99e7

# 2. your_DataBase #

This programm allow you to download information about 1000 films and create DataBase. You should to enter your api key v3 and path to place, where you want to save your DataBase.

# 3. movie_by_key_word #

This program can find in your DataBase film by key word. You should point place which contains your DataBase, enter key word and program will show your all films which title contains this word. 

 **Example:**  
 **Enter path to your movie list:**  
 movie_list.txt  
 **Enter key word:**   
 Saw   
 **Saw**  
 **Saw III**  
 **Saw II**  
 **Saw IV**  
    
# 4. search_for_recommendation #

This programm can recommend which film can interest you, after you enter title some film. Also you should point place which contains your DataBase.
 **Example:**  
 **Enter path to your movie list:**  
 movie_list.txt  
 **Enter  word:**  
  Saw II  
 **Recomend films:**    
 **Four Rooms**  
 **Absolute Power**  
 **Las Hurdes**  
 **The Lord of the Rings**  
 **48 Hrs.**  
 **Lost in Translation**  
 **The Interpreter**  
 **Star Trek: Generations**  
 **......................**  

    
    
    


