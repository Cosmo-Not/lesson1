def discounted(price, discount, max_discount=20):
    try:
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (TypeError):
        raise TypeError ("В функцию были переданы не числовые переменные")

print(discounted (1000, '10'))