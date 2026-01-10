#include <stdio.h>
#include <string.h>


int pin_length_checker(char *pin){
    int checker = 0;
    for (int i = 0; pin[i] != '\0'; i++){
        checker++;
    }

    if (checker == 4){
        return 0;
    }

    return -1;
}

int pin_checker(char *pin){
    char pin_input[9999];
    printf("ENTER PIN: ");
    scanf("%s", &pin_input);

    if (pin_length_checker(pin_input) == -1){
        printf("Invalid PIN length\n");
        return -1;
    }

    if (strcmp(pin_input, pin) != 0){
        printf("Incorrect PIN\n");
        return -1;
    }
    
    return 1;
}

void check_balance(float balance, char *pin){
    if (pin_checker(pin) == -1){
        return;
    }

    printf("CURRENT BALANCE: %f\n", balance);
}

float deposit(float balance, char *pin){
    if (pin_checker(pin) == -1){
        return -1;
    }
    float deposit;
    float new_balance;
    printf("CURRENT BALANCE: %f\n", balance);
    printf("DEPOSIT AMOUNT: ");
    scanf("%f", &deposit);
    
    if (deposit < 0){
        printf("Cannot have a negative deposit\n");
        return -1;
    }

    new_balance = balance + deposit;
    printf("NEW UPDATED BALANCE: %f\n", new_balance);
    return new_balance;
}

float withdraw(float balance, char *pin){
    if (pin_checker(pin) == -1){
        return -1;
    }
    float withdraw;
    float new_balance;
    printf("CURRENT BALANCE: %f\n", balance);
    printf("WITHDRAW AMOUNT: ");
    scanf("%f", &withdraw);

    if (withdraw < 0){
        printf("Cannot have a negative withdrawal\n");
        return -1;
    }

    if (withdraw > balance){
        printf("Not enough money for that withdrawal\n");
        return -1;
    }

    new_balance = balance - withdraw;
    printf("NEW UPDATED BALANCE: %f\n", new_balance);
    return new_balance;
}

char *change_pin (char *pin){
    if (pin_checker(pin) == 0){
        return "";
    }
    static char new_pin[9999];
    printf("ENTER NEW PIN: ");
    scanf("%s", new_pin);

    if (strcmp(new_pin, pin) == 0){
        printf("Error: same password was entered\n");
        return "";
    }

    if (pin_length_checker(new_pin) != 0){
        printf("Invalid PIN length\n");
        return "";
    }

    printf("PIN successfully changed\n");
    return new_pin;
}

int main(){
    float balance = 0;
    char pin[9999] = "1234";
    while (1) {
        int choice;
        float new_balance;
        char new_pin[9999];
        printf("************************\n");
        printf("WELCOME TO MAZE BANK\n");
        printf("************************\n");
        printf("[1] CHECK BALANCE\n");
        printf("[2] DEPOSIT\n");
        printf("[3] WITHDRAW\n");
        printf("[4] CHANGE PIN\n");
        printf("[5] END TRANSACTION\n");
        printf("ENTER INPUT: ");
        scanf("%d", &choice);
        if (choice == 5){
            printf("Bye!\n");
            break;
        } else if (choice == 1){
            check_balance(balance, pin);
        } else if (choice == 2){
            new_balance = deposit(balance,pin);
            if (new_balance != -1){
                balance = new_balance;
            }
        } else if (choice == 3){
            new_balance = withdraw(balance,pin);
            if (new_balance != -1){
                balance = new_balance;
            }
        } else if (choice == 4){
            strcpy(new_pin, change_pin(pin));
            if (strcmp(new_pin, "") != 0){
                strcpy(pin, new_pin);
            }
        } else{
            printf("Invalid choice");
            continue;
        }
    }
}