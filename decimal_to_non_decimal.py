def decimal_to_base(num, base):
    int_part = int(num)
    frac_part = num - int_part

    if int_part == 0:
        int_result = "0"
    else:
        int_result = ""
        while int_part > 0:
            remainder = int_part % base
            if remainder < 10:
                int_result = chr(ord('0') + remainder) + int_result
            else:
                int_result = chr(ord('A') + remainder - 10) + int_result
            int_part //= base

    frac_result = ""
    limit = 10 
    while frac_part > 0 and limit > 0:
        frac_part *= base
        digit = int(frac_part)
        if digit < 10:
            frac_result += chr(ord('0') + digit)
        else:
            frac_result += chr(ord('A') + digit - 10)
        frac_part -= digit
        limit -= 1

    if frac_result:
        return f"{int_result}.{frac_result}"
    else:
        return int_result


def main():
    num = float(input("Enter a decimal number: "))
    base = int(input("Enter base (2-16): "))

    result = decimal_to_base(num, base)
    print(f"Number in base {base} = {result}")


if __name__ == "__main__":
    main()
