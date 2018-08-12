ones = ["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"];
tens = ["","TEN","TWENTY","THIRTY","FORTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINETY"];
teens = ["TEN","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN"];
answer = 0;
for x in range(1,1000):
    numberString = "";
    if(not(x%100==x)):
        if(not(x%100==0)):
            numberString += ones[(x-(x%100))/100] + "HUNDREDAND";
            x = x%100;
        else:
            numberString += ones[x/100] + "HUNDRED";
            x = 0;
    if(not(x%10==x)):
        if(not((x-(x%10))/10== 1)):
            numberString += tens[(x-(x%10))/10];
            x = x%10;
        else:
           numberString += teens[x%10];
           x = 0;
    numberString += ones[x];
    answer += len(numberString);
print ("Problem 17: " + str(answer + len("ONETHOUSAND")));