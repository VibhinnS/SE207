def cocomo_ii_effort(mode, size, scale_factors, cost_factors):
    if mode == "organic":
        a = 2.4
        b = 1.05
    elif mode == "semi-detached":
        a = 3.0
        b = 1.12
    elif mode == "embedded":
        a = 3.6
        b = 1.20
    else:
        raise ValueError("Invalid mode. Choose 'organic', 'semi-detached', or 'embedded'.")

    scale_factor_product = 1.0
    for factor in scale_factors:
        scale_factor_product *= factor

    cost_factor_product = 1.0
    for factor in cost_factors:
        cost_factor_product *= factor

    effort = a * (size ** b) * scale_factor_product * cost_factor_product

    return effort

if __name__ == "__main__":    
    mode = int(input("Enter the mode - "))
    size = int(input("Enter the size - "))
    scale_factors = [0.91, 1.0, 1.23, 1.14, 1.07]  
    cost_factors = [1.24, 0.84, 0.92, 1.23, 1.32, 1.10, 1.19, 1.07]  
    mode = input("Enter the mode type - ")
    estimated_effort = cocomo_ii_effort(mode, size, scale_factors, cost_factors)
    print(f"Estimated Effort for {mode} mode: {estimated_effort} person-months")
    print()
