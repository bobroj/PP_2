def is_prime (num):
    if num<1:
        return False
    
    if num==2 or num%2==0:
        return False
    
    for i in range (3, int(num**0.5)+1, 2):       #шаг два, потому что нет смысла проверять делимость на четные числа
         if num%i==0:
             return False

    return True

def filterforprimes (numbers):
    primes=[]

    for num in numbers:
        if is_prime(num):
            primes.append(num)

    print(primes)

numbers = [int(x) for x in  input("Введите список: ").split()]

print("Простые числа из списка:")

filterforprimes(numbers)
