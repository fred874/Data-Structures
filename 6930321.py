# github: https://github.com/fred874

cars = {
    "toyota": {
        'model': 's',
        'price': 142000
    },
    "hyundai": {
        'model': 'sweat',
        'price': 20000
    },
    "honda": {
        'model': 'civil',
        'price': 400000
    },
    "kia": {
        "model": 'yz',
        'price': 100000
    },
    "tesla": {
        "model": 'S',
        "price": 250000
    },
    "bmw": {
        "model": 'i8',
        "price": 2550000
    },
    "ford": {
        "model": 'mustang',
        "price": 550000
    },
    "audi": {
        "model": 'g6',
        "price": 2550000
    },
    "cadillac": {
        "model": 'escalade',
        "price": 1000000
    },
    "dodge": {
        "model": 'wallet',
        "price": 350000
    },
    "madza": {
        "model": 'cx-3',
        "price": 250000
    },
    "nissan": {
        "model": 'micra',
        "price": 1550000
    },
    "chevrolet": {
        "model": 'malibu',
        "price": 2550000
    },
    "benz": {
        "model": 'c-250',
        "price": 2550000
    },
    "suzuki": {
        "model": 'swift',
        "price": 2550000
    }
}

user_input = input('what type of car are you looking for: ')

if user_input in cars:
    model = input('your car is available, what model are you looking for: ')
    if model.lower() in cars[user_input]['model']:
        print('your model is available')
        price = cars[user_input]['price']
        print(f'the price on this car is ${price}.00')
    else:
        print('sorry, unfortunately your car isn"t available atm, try again later')