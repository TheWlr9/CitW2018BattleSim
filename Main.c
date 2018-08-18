/*
* https://github.com/TheWlr9/CitW2018BattleSim/
*/

#include <stdio.h>
#include <string.h>

int main() {
    char battle1[100];
    char battle2[100];

    printf("Select a battle... ");
    scanf("%s",battle1);

    printf("Select the second battle... ");
    scanf("%s",battle2);

    printf("Army 1: %s\tArmy 2: %s",battle1,battle2);

    return 0;
}