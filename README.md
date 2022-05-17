# China_City_sustainability
Using K neighbors to predict sustainability index for cities in China in future 5 years 
- [x] Searching for data  
- [x] Optimize algorthim 

## What this project does
This project is dedicated to predict future performance of sustainability scores for cities in china. This project is using data from the China statistical book and online resources from the year 1999 to 2018. 

## what is the value of this project 
The score of the prediction could help to project the performances of cities in china and help to identify potential improvements.

## How this work 
By using the k neighbour algorthim, this project successfully could predict sustainability index for cities in China with an accuracy of 99%. 



```mermaid
graph TD;
    China_statistical_book-->17labels;
    China_statistical_book-->Sustainability_Score;
    17labels--> K_neighbours_algorthim;
    Sustainability_Score--> K_neighbours_algorthim;
    K_neighbours_algorthim--> Predicted_score_ForFuture;
    
    
    
```
## How to use
modifiy the "test" xlsx file and enter the data for 17 labels of the city you want to predict. 
```mermaid
graph TD;
    InputedData--> Predicted_score;
    
    
```



## Results 

![image](https://user-images.githubusercontent.com/39557261/168578041-ad313b58-f297-4714-93c9-04a02fa0320c.png)
![image](https://user-images.githubusercontent.com/39557261/168578074-ee628602-07a7-45e9-ac22-6c4fe62dbe6d.png)

