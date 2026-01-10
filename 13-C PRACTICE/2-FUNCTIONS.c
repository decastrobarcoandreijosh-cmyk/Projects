#include <stdio.h>

int main(){

    while (1){
        int choice;
        float bmi;
        float weight;
        float height;
        float height_metric;
        int height_standard_feet;
        int height_standard_inches;
        printf("===MENU===\n");
        printf("[1] METRIC\n");
        printf("[2] STANDARD\n");
        printf("[0] EXIT\n");
        printf("ENTER INPUT: ");
        scanf("%d", &choice);
        if (choice == 0){
            break;
        } else if (choice == 1){
            printf("\n");
            printf("METRIC CALCULATION\n");
            printf("PLEASE ENTER WEIGHT IN KILOGRAMS: ");
            scanf("%f", &weight);
            printf("PLEASE ENTER HEIGHT IN CENTIMETERS: ");
            scanf("%f", &height_metric);
            height = height_metric / 100;
            bmi = weight/(height*height);
            printf("BMI in METRIC CALCULATION is %f\n", bmi);
        } else if (choice == 2){
            printf("\n");
            printf("STANDARD CALCULATION\n");
            printf("PLEASE ENTER WEIGHT IN POUNDS: ");
            scanf("%f", &weight);
            printf("PLEASE ENTER HEIGHT IN FEET AND INCHES: ");
            scanf("%d'%d", &height_standard_feet, &height_standard_inches);
            height = (height_standard_feet * 12) + height_standard_inches;
            bmi = (weight/(height*height)) * 703;
            printf("BMI in STANDARD CALCULATION is %f\n", bmi);
        } else{
            printf("Invalid Choice");
            continue;
        }
        
        if (bmi<18.5){
            printf("BMI CLASS: UNDERWEIGHT\n");
        } else if (bmi >= 18.5 & bmi < 25 ){
            printf("BMI CLASS: NORMAL WEIGHT\n");
        } else if (bmi >= 25 & bmi < 30){
            printf("BMI CLASS: OVERWEIGHT\n");
        } else {
            printf("BMI CLASS: OBESE\n");
        }


    } 
}