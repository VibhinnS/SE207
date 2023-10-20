#include <stdio.h>

int calculate_function_points(int ei, int eo, int eq, int ilf, int eif) {
    int weights[5] = {4, 5, 4, 7, 7};
    int function_points = (ei * weights[0] +
                           eo * weights[1] +
                           eq * weights[2] +
                           ilf * weights[3] +
                           eif * weights[4]);
    return function_points;
}

int main() {
    int ei, eo, eq, ilf, eif;
    printf("Enter the ei value: ");
    scanf("%d", &ei);
    printf("Enter the eo value: ");
    scanf("%d", &eo);
    printf("Enter the eq value: ");
    scanf("%d", &eq);
    printf("Enter the ilf value: ");
    scanf("%d", &ilf);
    printf("Enter the eif value: ");
    scanf("%d", &eif);
    
    int total_function_points = calculate_function_points(ei, eo, eq, ilf, eif);
    
    printf("Total Function Points: %d\n", total_function_points);
    return 0;
}
