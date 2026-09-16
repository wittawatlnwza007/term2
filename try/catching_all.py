try:
    value = int(input("Enter a number : "))
    result = 0 / value
except Exception as e   :
    print(f"An error occurred : {e}")
print("End of program")