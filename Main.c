/*
* https://github.com/TheWlr9/CitW2018BattleSim/
*/

#include <stdio.h>
#include <string.h>

int main(){
    char army1Name[100];
    char army2Name[100];
    FILE* army1,* army2;

    printf("Select a battle... ");
    scanf("%s",army1Name);

    printf("Select the second battle... ");
    scanf("%s",army2Name);

    printf("Army 1: %s\tArmy 2: %s",army1Name,army2Name);

    army1= fopen(army1Name,"r");
    army2= fopen(army2Name,"r");
    if(army1 && army2){

    }
    else{
        //There was an error with finding the army data. (maybe it doesn't exist?)
        if(!army1)
            printf("%s is an invalid army name",army1Name);
        if(!army2)
            printf("%s is an invalid army name",army2Name);

        return 1; //Exit with an error code
    }

    return 0;
}