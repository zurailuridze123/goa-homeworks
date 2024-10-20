def check_odd_even():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")

# ფუნქციის გამოძახება
check_odd_even()  # მაგალითად, input: 9 >>> output: 9 არის კენტი

