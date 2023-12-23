import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Restaurant, Foods

def add_restaurant(db: Session, name: str, description: str, image: str):
    restaurant = Restaurant(name=name, description=description, image=image)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

def add_food(db: Session, restaurant_id: int, name: str, description: str, image: str, price: int):
    food = Foods(restaurant_id=restaurant_id, name=name, description=description, image=image, price=price)
    db.add(food)
    db.commit()
    db.refresh(food)
    return food
def main():
    db = SessionLocal()

    # Sample data for restaurants
    restaurants = [
            {"name": "Italian Bistro", "description": "Authentic Italian cuisine", "image": "restaurants/italian_bistro.png"},
            {"name": "Sushi House", "description": "Fresh sushi and Japanese dishes", "image": "restaurants/sushi_house.png"},
            {"name": "Taco Fiesta", "description": "Mexican street food and tacos", "image": "restaurants/taco_fiesta.png"},
            {"name": "Burger Joint", "description": "Gourmet burgers and fries", "image": "restaurants/burger_joint.png"},
            {"name": "Pizza Palace", "description": "Wood-fired pizzas", "image": "restaurants/pizza_palace.png"},
            {"name": "Indian Spice", "description": "Traditional Indian curries and tandoori", "image": "restaurants/indian_spice.png"},
            {"name": "Thai Delight", "description": "Flavorful Thai dishes and noodles", "image": "restaurants/thai_delight.png"},
            {"name": "Chinese Wok", "description": "Classic Chinese cuisine and dim sum", "image": "restaurants/chinese_wok.png"},
            {"name": "Mediterranean Grill", "description": "Fresh Mediterranean flavors and kebabs", "image": "restaurants/mediterranean_grill.png"},
            {"name": "French Bistro", "description": "Elegant French dining and pastries", "image": "restaurants/french_bistro.png"},
            {"name": "Steakhouse", "description": "Premium steaks and seafood", "image": "restaurants/steakhouse.png"},
            {"name": "Vegan Cafe", "description": "Plant-based dishes and smoothies", "image": "restaurants/vegan_cafe.png"},
            {"name": "Greek Taverna", "description": "Greek classics and seafood", "image": "restaurants/greek_taverna.png"},
            {"name": "Southern Comfort", "description": "Homestyle Southern cooking", "image": "restaurants/southern_comfort.png"},
            {"name": "BBQ Shack", "description": "Smoked meats and barbecue", "image": "restaurants/bbq_shack.png"},
            {"name": "Seafood Delight", "description": "Fresh seafood and fish dishes", "image": "restaurants/seafood_delight.png"},
            {"name": "Veggie Heaven", "description": "Delicious vegetarian and vegan dishes", "image": "restaurants/veggie_heaven.png"},
            {"name": "Chicken Coop", "description": "Grilled and fried chicken dishes", "image": "restaurants/chicken_coop.png"},
            {"name": "Pasta Paradise", "description": "A variety of pasta dishes", "image": "restaurants/pasta_paradise.png"},
            {"name": "Bakery Bliss", "description": "Freshly baked breads and pastries", "image": "restaurants/bakery_bliss.png"},
            {"name": "Salad Bar", "description": "Healthy and delicious salads", "image": "restaurants/salad_bar.png"},
            {"name": "Ramen House", "description": "Japanese ramen and noodle dishes", "image": "restaurants/ramen_house.png"},
            {"name": "Ice Cream Shop", "description": "Variety of ice cream flavors and desserts", "image": "restaurants/ice_cream_shop.png"},
            {"name": "Sandwich Shop", "description": "Freshly made sandwiches and wraps", "image": "restaurants/sandwich_shop.png"},
            {"name": "Pancake House", "description": "Sweet and savory pancakes", "image": "restaurants/pancake_house.png"}
        ]

    # Sample data for foods
    foods = [
        # Italian Bistro
        {"restaurant_id": 1, "name": "Margherita Pizza", "description": "Classic pizza with tomato sauce, fresh mozzarella, and basil", "image": "foods/margherita_pizza.png", "price": 12},
        {"restaurant_id": 1, "name": "Spaghetti Carbonara", "description": "Creamy pasta with pancetta, egg, and Pecorino Romano cheese", "image": "foods/spaghetti_carbonara.png", "price": 14},
        {"restaurant_id": 1, "name": "Caprese Salad", "description": "Fresh salad with tomatoes, mozzarella, basil, and balsamic glaze", "image": "foods/caprese_salad.png", "price": 10},
        {"restaurant_id": 1, "name": "Tiramisu", "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream", "image": "foods/tiramisu.png", "price": 8},
        {"restaurant_id": 1, "name": "Risotto", "description": "Creamy risotto with mushrooms and Parmesan cheese", "image": "foods/risotto.png", "price": 16},
        {"restaurant_id": 1, "name": "Chianti", "description": "Italian red wine", "image": "beverages/chianti.png", "price": 8},
        {"restaurant_id": 1, "name": "Espresso", "description": "Strong Italian coffee", "image": "beverages/espresso.png", "price": 3},
        {"restaurant_id": 1, "name": "Limoncello", "description": "Italian lemon liqueur", "image": "beverages/limoncello.png", "price": 7},

        # Sushi House
        {"restaurant_id": 2, "name": "California Roll", "description": "Sushi roll with crab, avocado, and cucumber", "image": "foods/california_roll.png", "price": 8},
        {"restaurant_id": 2, "name": "Spicy Tuna Roll", "description": "Sushi roll with spicy tuna, mayo, and cucumber", "image": "foods/spicy_tuna_roll.png", "price": 9},
        {"restaurant_id": 2, "name": "Salmon Nigiri", "description": "Sushi with a slice of fresh salmon on top of sushi rice", "image": "foods/salmon_nigiri.png", "price": 7},
        {"restaurant_id": 2, "name": "Shrimp Tempura Roll", "description": "Sushi roll with tempura shrimp, avocado, and cucumber", "image": "foods/shrimp_tempura_roll.png", "price": 10},
        {"restaurant_id": 2, "name": "Miso Soup", "description": "Traditional Japanese soup with tofu and seaweed", "image": "foods/miso_soup.png", "price": 4},
        {"restaurant_id": 2, "name": "Sake", "description": "Japanese rice wine", "image": "beverages/sake.png", "price": 6},
        {"restaurant_id": 2, "name": "Green Tea", "description": "Hot Japanese green tea", "image": "beverages/green_tea.png", "price": 3},
        {"restaurant_id": 2, "name": "Plum Wine", "description": "Sweet Japanese wine made from plums", "image": "beverages/plum_wine.png", "price": 7},

        # Taco Fiesta
        {"restaurant_id": 3, "name": "Carne Asada Taco", "description": "Taco with grilled steak, onions, and cilantro", "image": "foods/carne_asada_taco.png", "price": 3},
        {"restaurant_id": 3, "name": "Carnitas Taco", "description": "Taco with slow-cooked pork, onions, and cilantro", "image": "foods/carnitas_taco.png", "price": 3},
        {"restaurant_id": 3, "name": "Chicken Taco", "description": "Taco with grilled chicken, onions, and cilantro", "image": "foods/chicken_taco.png", "price": 3},
        {"restaurant_id": 3, "name": "Fish Taco", "description": "Taco with battered fish, cabbage, and chipotle mayo", "image": "foods/fish_taco.png", "price": 4},
        {"restaurant_id": 3, "name": "Churros", "description": "Fried dough pastry with cinnamon sugar", "image": "foods/churros.png", "price": 5},
        {"restaurant_id": 3, "name": "Margarita", "description": "Classic Mexican cocktail with tequila, lime, and triple sec", "image": "beverages/margarita.png", "price": 7},
        {"restaurant_id": 3, "name": "Mexican Beer", "description": "Refreshing Mexican lager", "image": "beverages/mexican_beer.png", "price": 5},
        {"restaurant_id": 3, "name": "Horchata", "description": "Sweet Mexican drink made from rice", "image": "beverages/horchata.png", "price": 4},

        # Burger Joint
        {"restaurant_id": 4, "name": "Classic Cheeseburger", "description": "Juicy burger with cheese, lettuce, tomato, and onion", "image": "foods/classic_cheeseburger.png", "price": 10},
        {"restaurant_id": 4, "name": "Bacon Burger", "description": "Delicious burger with bacon, cheese, lettuce, tomato, and onion", "image": "foods/bacon_burger.png", "price": 12},
        {"restaurant_id": 4, "name": "Mushroom Swiss Burger", "description": "Tasty burger with Swiss cheese and sautéed mushrooms", "image": "foods/mushroom_swiss_burger.png", "price": 11},
        {"restaurant_id": 4, "name": "Veggie Burger", "description": "Healthy vegetarian burger with lettuce, tomato, and onion", "image": "foods/veggie_burger.png", "price": 10},
        {"restaurant_id": 4, "name": "French Fries", "description": "Crispy golden fries served with ketchup", "image": "foods/french_fries.png", "price": 4},
        {"restaurant_id": 4, "name": "Craft Beer", "description": "Local craft beer", "image": "beverages/craft_beer.png", "price": 6},
        {"restaurant_id": 4, "name": "Milkshake", "description": "Creamy milkshake with vanilla, chocolate, or strawberry", "image": "beverages/milkshake.png", "price": 5},
        {"restaurant_id": 4, "name": "Soda", "description": "Refreshing carbonated drink", "image": "beverages/soda.png", "price": 3},

        # Pizza Palace
        {"restaurant_id": 5, "name": "Pepperoni Pizza", "description": "Delicious pizza with tomato sauce, mozzarella, and pepperoni", "image": "foods/pepperoni_pizza.png", "price": 12},
        {"restaurant_id": 5, "name":"Veggie Pizza", "description": "Healthy pizza with tomato sauce, mozzarella, bell peppers, onions, and olives", "image": "foods/veggie_pizza.png", "price": 14},
        {"restaurant_id": 5, "name": "Meat Lovers Pizza", "description": "Hearty pizza with tomato sauce, mozzarella, pepperoni, sausage, and bacon", "image": "foods/meat_lovers_pizza.png", "price": 16},
        {"restaurant_id": 5, "name": "BBQ Chicken Pizza", "description": "Tasty pizza with BBQ sauce, mozzarella, chicken, red onion, and cilantro", "image": "foods/bbq_chicken_pizza.png", "price": 15},
        {"restaurant_id": 5, "name": "Hawaiian Pizza", "description": "Sweet and savory pizza with tomato sauce, mozzarella, ham, and pineapple", "image": "foods/hawaiian_pizza.png", "price": 14},
        {"restaurant_id": 5, "name": "Italian Soda", "description": "Refreshing soda with a choice of fruit syrup", "image": "beverages/italian_soda.png", "price": 4},
        {"restaurant_id": 5, "name": "Chianti", "description": "Italian red wine", "image": "beverages/chianti.png", "price": 8},
        {"restaurant_id": 5, "name": "Limoncello", "description": "Italian lemon liqueur", "image": "beverages/limoncello.png", "price": 7},

        # Indian Spice
        {"restaurant_id": 6, "name": "Chicken Tikka Masala", "description": "Grilled chicken in a creamy tomato sauce served with basmati rice", "image": "foods/chicken_tikka_masala.png", "price": 14},
        {"restaurant_id": 6, "name": "Lamb Curry", "description": "Tender lamb in a spiced curry sauce served with basmati rice", "image": "foods/lamb_curry.png", "price": 16},
        {"restaurant_id": 6, "name": "Saag Paneer", "description": "Indian cheese in a creamy spinach sauce served with naan bread", "image": "foods/saag_paneer.png", "price": 12},
        {"restaurant_id": 6, "name": "Vegetable Biryani", "description": "Aromatic rice dish with mixed vegetables and spices served with raita", "image": "foods/vegetable_biryani.png", "price": 10},
        {"restaurant_id": 6, "name": "Garlic Naan", "description": "Leavened bread with garlic and butter", "image": "foods/garlic_naan.png", "price": 4},
        {"restaurant_id": 6, "name": "Mango Lassi", "description": "Refreshing yogurt-based drink with mango", "image": "beverages/mango_lassi.png", "price": 4},
        {"restaurant_id": 6, "name": "Masala Chai", "description": "Spiced tea with milk", "image": "beverages/masala_chai.png", "price": 3},
        {"restaurant_id": 6, "name": "Kingfisher Beer", "description": "Indian lager beer", "image": "beverages/kingfisher_beer.png", "price": 5},

        # Thai Delight
        {"restaurant_id": 7, "name": "Pad Thai", "description": "Stir-fried rice noodles with shrimp, tofu, eggs, and peanuts", "image": "foods/pad_thai.png", "price": 12},
        {"restaurant_id": 7, "name": "Green Curry", "description": "Spicy green curry with chicken, eggplant, and basil served with jasmine rice", "image": "foods/green_curry.png", "price": 14},
        {"restaurant_id": 7, "name": "Tom Yum Soup", "description": "Hot and sour soup with shrimp, lemongrass, and mushrooms", "image": "foods/tom_yum_soup.png", "price": 8},
        {"restaurant_id": 7, "name": "Papaya Salad", "description": "Spicy salad with green papaya, tomatoes, and peanuts", "image": "foods/papaya_salad.png", "price": 10},
        {"restaurant_id": 7, "name": "Mango Sticky Rice", "description": "Sweet dessert with sticky rice, fresh mango, and coconut milk", "image": "foods/mango_sticky_rice.png", "price": 6},
        {"restaurant_id": 7, "name": "Thai Iced Tea", "description": "Sweet tea with milk", "image": "beverages/thai_iced_tea.png", "price": 4},
        {"restaurant_id": 7, "name": "Singha Beer", "description": "Thai lager beer", "image": "beverages/singha_beer.png", "price": 5},
        {"restaurant_id": 7, "name": "Lemongrass Juice", "description": "Refreshing juice with lemongrass", "image": "beverages/lemongrass_juice.png", "price": 4},

        # Chinese Wok
        {"restaurant_id": 8, "name": "Kung Pao Chicken", "description": "Stir-fried chicken with peanuts, vegetables, and chili peppers served with steamed rice", "image": "foods/kung_pao_chicken.png", "price": 12},
        {"restaurant_id": 8, "name": "Beef and Broccoli", "description": "Stir-fried beef with broccoli in a savory sauce served with steamed rice", "image": "foods/beef_and_broccoli.png", "price": 14},
        {"restaurant_id": 8, "name": "Sweet and Sour Pork", "description": "Battered pork with pineapple, bell peppers, and sweet and sour sauce served with steamed rice", "image": "foods/sweet_and_sour_pork.png", "price": 12},
        {"restaurant_id": 8, "name": "Vegetable Fried Rice", "description": "Fried rice with mixed vegetables and eggs", "image": "foods/vegetable_fried_rice.png", "price": 10},
        {"restaurant_id": 8, "name": "Spring Rolls", "description": "Crispy rolls filled with vegetables served with sweet and sour sauce", "image": "foods/spring_rolls.png", "price": 6},
        {"restaurant_id": 8, "name": "Tsingtao Beer", "description": "Chinese lager beer", "image": "beverages/tsingtao_beer.png", "price": 5},
        {"restaurant_id": 8, "name": "Jasmine Tea", "description": "Hot tea with jasmine flavor", "image": "beverages/jasmine_tea.png", "price": 3},
        {"restaurant_id": 8, "name": "Plum Juice", "description": "Sweet juice made from plums", "image": "beverages/plum_juice.png", "price": 4},

        # Mediterranean Grill
        {"restaurant_id": 9, "name": "Chicken Shawarma", "description": "Marinated chicken with garlic sauce and pickles wrapped in pita bread", "image": "foods/chicken_shawarma.png", "price": 10},
        {"restaurant_id": 9, "name": "Falafel", "description": "Deep-fried chickpea patties with tahini sauce and salad wrapped in pita bread", "image": "foods/falafel.png", "price": 8},
        {"restaurant_id": 9, "name": "Greek Salad", "description": "Fresh salad with tomatoes, cucumbers, olives, and feta cheese", "image": "foods/greek_salad.png", "price": 10},
        {"restaurant_id": 9, "name": "Hummus", "description": "Chickpea dip with olive oil and pita bread", "image": "foods/hummus.png", "price": 6},
        {"restaurant_id": 9, "name": "Baklava", "description": "Sweet pastry with layers of filo and chopped nuts", "image": "foods/baklava.png", "price": 5},
        {"restaurant_id": 9, "name": "Greek Wine", "description": "White or red Greek wine", "image": "beverages/greek_wine.png", "price": 7},
        {"restaurant_id": 9, "name": "Turkish Coffee", "description": "Strong coffee served in a small cup", "image": "beverages/turkish_coffee.png", "price": 3},
        {"restaurant_id": 9, "name": "Mint Lemonade", "description": "Refreshing lemonade with mint", "image": "beverages/mint_lemonade.png", "price": 4},

        # French Bistro
        {"restaurant_id": 10, "name": "Coq au Vin", "description": "Braised chicken with red wine, mushrooms, and onions served with mashed potatoes", "image": "foods/coq_au_vin.png", "price": 18},
        {"restaurant_id": 10, "name": "Beef Bourguignon", "description": "Slow-cooked beef with red wine, mushrooms, and carrots served with mashed potatoes", "image": "foods/beef_bourguignon.png", "price": 20},
        {"restaurant_id": 10, "name": "French Onion Soup", "description": "Caramelized onion soup with Gruyère cheese croutons", "image": "foods/french_onion_soup.png", "price": 8},
        {"restaurant_id": 10, "name": "Ratatouille", "description": "Stewed vegetables with tomato sauce and herbs served with crusty bread", "image": "foods/ratatouille.png", "price": 12},
        {"restaurant_id": 10, "name": "Crème Brûlée", "description": "Vanilla custard with caramelized sugar", "image": "foods/creme_brulee.png", "price": 6},
        {"restaurant_id": 10, "name": "French Wine", "description": "Red or white French wine", "image": "beverages/french_wine.png", "price": 8},
        {"restaurant_id": 10, "name": "Espresso", "description": "Strong French coffee", "image": "beverages/espresso.png", "price": 3},
        {"restaurant_id": 10, "name": "Lemonade", "description": "Refreshing lemonade", "image": "beverages/lemonade.png", "price": 4},

        # Steakhouse
        {"restaurant_id": 11, "name": "Ribeye Steak", "description": "Grilled ribeye steak with garlic herb butter served with mashed potatoes", "image": "foods/ribeye_steak.png", "price": 28},
        {"restaurant_id": 11, "name": "Filet Mignon", "description": "Tender filet mignon with red wine reduction served with mashed potatoes", "image": "foods/filet_mignon.png", "price": 32},
        {"restaurant_id": 11, "name": "Grilled Salmon", "description": "Grilled salmon with lemon herb sauce served with steamed vegetables", "image": "foods/grilled_salmon.png", "price": 22},
        {"restaurant_id": 11, "name": "Caesar Salad", "description": "Classic salad with romaine lettuce, croutons, and Parmesan cheese", "image": "foods/caesar_salad.png", "price": 10},
        {"restaurant_id": 11, "name": "Mashed Potatoes", "description": "Creamy mashed potatoes with butter", "image": "foods/mashed_potatoes.png", "price": 6},
        {"restaurant_id": 11, "name": "Cabernet Sauvignon", "description": "Full-bodied red wine", "image": "beverages/cabernet_sauvignon.png", "price": 8},
        {"restaurant_id": 11, "name": "Craft Beer", "description": "Local craft beer", "image": "beverages/craft_beer.png", "price": 6},
        {"restaurant_id": 11, "name": "Whiskey", "description": "Aged whiskey on the rocks", "image": "beverages/whiskey.png", "price": 7},

        # Vegan Cafe
        {"restaurant_id": 12, "name": "Vegan Burger", "description": "Plant-based burger with lettuce, tomato, and onion served with sweet potato fries", "image": "foods/vegan_burger.png", "price": 12},
        {"restaurant_id": 12, "name": "Quinoa Salad", "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables", "image": "foods/quinoa_salad.png", "price": 10},
        {"restaurant_id": 12, "name": "Lentil Soup", "description": "Hearty soup with lentils and vegetables", "image": "foods/lentil_soup.png", "price": 8},
        {"restaurant_id": 12, "name": "Stuffed Bell Peppers", "description": "Bell peppers filled with quinoa, beans, and vegetables", "image": "foods/stuffed_bell_peppers.png", "price": 14},
        {"restaurant_id": 12, "name": "Fruit Smoothie", "description": "Blended smoothie with a choice of fruits and almond milk", "image": "foods/fruit_smoothie.png", "price": 6},
        {"restaurant_id": 12, "name": "Green Juice", "description": "Healthy juice with kale, spinach, and apple", "image": "beverages/green_juice.png", "price": 5},
        {"restaurant_id": 12, "name": "Herbal Tea", "description": "Hot tea with a choice of herbs", "image": "beverages/herbal_tea.png", "price": 3},
        {"restaurant_id": 12, "name": "Almond Milk Latte", "description": "Coffee with almond milk", "image": "beverages/almond_milk_latte.png", "price": 4},

        # Greek Taverna
        {"restaurant_id": 13, "name": "Gyro", "description": "Grilled meat with tzatziki sauce, tomatoes, and onions wrapped in pita bread", "image": "foods/gyro.png", "price": 10},
        {"restaurant_id": 13, "name": "Moussaka", "description": "Layered dish with eggplant, ground beef, and béchamel sauce", "image": "foods/moussaka.png", "price": 14},
        {"restaurant_id": 13, "name": "Spanakopita", "description": "Savory pastry with spinach and feta cheese", "image": "foods/spanakopita.png", "price": 8},
        {"restaurant_id": 13, "name": "Dolmades", "description": "Stuffed grape leaves with rice and herbs", "image": "foods/dolmades.png", "price": 6},
        {"restaurant_id": 13, "name": "Greek Yogurt", "description": "Thick yogurt with honey and walnuts", "image": "foods/greek_yogurt.png", "price": 5},
        {"restaurant_id": 13, "name": "Greek Wine", "description": "White or red Greek wine", "image": "beverages/greek_wine.png", "price": 7},
        {"restaurant_id": 13, "name": "Ouzo", "description": "Anise-flavored Greek liquor", "image": "beverages/ouzo.png", "price": 6},
        {"restaurant_id": 13, "name": "Greek Coffee", "description": "Strong coffee served in a small cup", "image": "beverages/greek_coffee.png", "price": 3},

        # Southern Comfort
        {"restaurant_id": 14, "name": "Fried Chicken", "description": "Crispy fried chicken served with mashed potatoes and gravy", "image": "foods/fried_chicken.png", "price": 14},
        {"restaurant_id": 14, "name": "Shrimp and Grits", "description": "Sautéed shrimp with creamy grits and bacon", "image": "foods/shrimp_and_grits.png", "price": 16},
        {"restaurant_id": 14, "name": "Chicken and Waffles", "description": "Fried chicken with fluffy waffles and maple syrup", "image": "foods/chicken_and_waffles.png", "price": 14},
        {"restaurant_id": 14, "name": "Biscuits and Gravy", "description": "Buttermilk biscuits with sausage gravy", "image": "foods/biscuits_and_gravy.png", "price": 8},
        {"restaurant_id": 14, "name": "Pecan Pie", "description": "Sweet pie with pecan filling", "image": "foods/pecan_pie.png", "price": 6},
        {"restaurant_id": 14, "name": "Sweet Tea", "description": "Refreshing iced tea with sugar", "image": "beverages/sweet_tea.png", "price": 3},
        {"restaurant_id": 14, "name": "Bourbon", "description": "Aged bourbon on the rocks", "image": "beverages/bourbon.png", "price": 7},
        {"restaurant_id": 14, "name": "Mint Julep", "description": "Classic cocktail with bourbon, mint, and sugar", "image": "beverages/mint_julep.png", "price": 7},

        # BBQ Shack
        {"restaurant_id": 15, "name": "Pulled Pork Sandwich", "description": "Slow-cooked pulled pork with BBQ sauce served with coleslaw", "image": "foods/pulled_pork_sandwich.png", "price": 10},
        {"restaurant_id": 15, "name": "Beef Brisket", "description": "Smoked beef brisket with BBQ sauce served with coleslaw", "image": "foods/beef_brisket.png", "price": 14},
        {"restaurant_id": 15, "name": "Baby Back Ribs", "description": "Tender pork ribs with BBQ sauce served with coleslaw", "image": "foods/baby_back_ribs.png", "price": 16},
        {"restaurant_id": 15, "name": "Mac and Cheese", "description": "Creamy macaroni and cheese", "image": "foods/mac_and_cheese.png", "price": 6},
        {"restaurant_id": 15, "name": "Cornbread", "description": "Sweet and moist cornbread", "image": "foods/cornbread.png", "price": 4},
        {"restaurant_id": 15, "name": "Craft Beer", "description": "Local craft beer", "image": "beverages/craft_beer.png", "price": 6},
        {"restaurant_id": 15, "name": "Sweet Tea", "description": "Refreshing iced tea with sugar", "image": "beverages/sweet_tea.png", "price": 3},
        {"restaurant_id": 15, "name": "Bourbon", "description": "Aged bourbon on the rocks", "image": "beverages/bourbon.png", "price": 7},

        # Seafood Delight
        {"restaurant_id": 16, "name": "Grilled Salmon", "description": "Grilled salmon with lemon herb sauce served with steamed vegetables", "image": "foods/grilled_salmon.png", "price": 22},
        {"restaurant_id": 16, "name": "Shrimp Scampi", "description": "Sautéed shrimp with garlic, white wine, and butter served with pasta", "image": "foods/shrimp_scampi.png", "price": 20},
        {"restaurant_id": 16, "name": "Clam Chowder", "description": "Creamy soup with clams, potatoes, and onions", "image": "foods/clam_chowder.png", "price": 8},
        {"restaurant_id": 16, "name": "Fish and Chips", "description": "Battered fish with crispy fries and tartar sauce", "image": "foods/fish_and_chips.png", "price": 14},
        {"restaurant_id": 16, "name": "Lobster Roll", "description": "Fresh lobster with mayo and celery on a toasted bun", "image": "foods/lobster_roll.png", "price": 18},
        {"restaurant_id": 16, "name": "White Wine", "description": "Refreshing white wine", "image": "beverages/white_wine.png", "price": 7},
        {"restaurant_id": 16, "name": "Craft Beer", "description": "Local craft beer", "image": "beverages/craft_beer.png", "price": 6},
        {"restaurant_id": 16, "name": "Iced Tea", "description": "Refreshing iced tea", "image": "beverages/iced_tea.png", "price": 3},

        # Veggie Heaven
        {"restaurant_id": 17, "name": "Veggie Burger", "description": "Plant-based burger with lettuce, tomato, and onion served with sweet potato fries", "image": "foods/veggie_burger.png", "price": 12},
        {"restaurant_id": 17, "name": "Quinoa Salad", "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables", "image": "foods/quinoa_salad.png", "price": 10},
        {"restaurant_id": 17, "name": "Lentil Soup", "description": "Hearty soup with lentils and vegetables", "image": "foods/lentil_soup.png", "price": 8},
        {"restaurant_id": 17, "name": "Stuffed Bell Peppers", "description": "Bell peppers filled with quinoa, beans, and vegetables", "image": "foods/stuffed_bell_peppers.png", "price": 14},
        {"restaurant_id": 17, "name": "Vegan Chocolate Cake", "description": "Delicious chocolate cake made with plant-based ingredients", "image": "foods/vegan_chocolate_cake.png", "price": 6},
        {"restaurant_id": 17, "name": "Green Juice", "description": "Healthy juice with kale, spinach, and apple", "image": "beverages/green_juice.png", "price": 5},
        {"restaurant_id": 17, "name": "Herbal Tea", "description": "Hot tea with a choice of herbs", "image": "beverages/herbal_tea.png", "price": 3},
        {"restaurant_id": 17, "name": "Almond Milk Latte", "description": "Coffee with almond milk", "image": "beverages/almond_milk_latte.png", "price": 4},

        # Chicken Coop
        {"restaurant_id": 18, "name": "Fried Chicken", "description": "Crispy fried chicken served with mashed potatoes and gravy", "image": "foods/fried_chicken.png", "price": 14},
        {"restaurant_id": 18, "name": "Chicken and Waffles", "description": "Fried chicken with fluffy waffles and maple syrup", "image": "foods/chicken_and_waffles.png", "price": 14},
        {"restaurant_id": 18, "name": "Chicken Caesar Salad", "description": "Classic salad with romaine lettuce, croutons, Parmesan cheese, and grilled chicken", "image": "foods/chicken_caesar_salad.png", "price": 12},
        {"restaurant_id": 18, "name": "Chicken Noodle Soup", "description": "Hearty soup with chicken, noodles, and vegetables", "image": "foods/chicken_noodle_soup.png", "price": 8},
        {"restaurant_id": 18, "name": "Chicken Pot Pie", "description": "Comforting pie with chicken and vegetables in a creamy sauce", "image": "foods/chicken_pot_pie.png", "price": 12},
        {"restaurant_id": 18, "name": "Craft Beer", "description": "Local craft beer", "image": "beverages/craft_beer.png", "price": 6},
        {"restaurant_id": 18, "name": "Sweet Tea", "description": "Refreshing iced tea with sugar", "image": "beverages/sweet_tea.png", "price": 3},
        {"restaurant_id": 18, "name": "Lemonade", "description": "Refreshing lemonade", "image": "beverages/lemonade.png", "price": 4},

        # Pasta Paradise
        {"restaurant_id": 19, "name": "Spaghetti Carbonara", "description": "Creamy pasta with pancetta, egg, and Pecorino Romano cheese", "image": "foods/spaghetti_carbonara.png", "price": 14},
        {"restaurant_id": 19, "name": "Fettuccine Alfredo", "description": "Pasta with creamy Alfredo sauce and Parmesan cheese", "image": "foods/fettuccine_alfredo.png", "price": 12},
        {"restaurant_id": 19, "name": "Lasagna", "description": "Layered pasta with ground beef, tomato sauce, and cheese", "image": "foods/lasagna.png", "price": 16},
        {"restaurant_id": 19, "name": "Pesto Pasta", "description": "Pasta with basil pesto sauce and Parmesan cheese", "image": "foods/pesto_pasta.png", "price": 12},
        {"restaurant_id": 19, "name": "Tiramisu", "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream", "image": "foods/tiramisu.png", "price": 8},
        {"restaurant_id": 19, "name": "Chianti", "description": "Italianred wine", "image": "beverages/chianti.png", "price": 8},
        {"restaurant_id": 19, "name": "Espresso", "description": "Strong Italian coffee", "image": "beverages/espresso.png", "price": 3},
        {"restaurant_id": 19, "name": "Limoncello", "description": "Italian lemon liqueur", "image": "beverages/limoncello.png", "price": 7},

        # Bakery Bliss
        {"restaurant_id": 20, "name": "Croissant", "description": "Flaky and buttery French pastry", "image": "foods/croissant.png", "price": 3},
        {"restaurant_id": 20, "name": "Baguette", "description": "Crusty French bread", "image": "foods/baguette.png", "price": 2},
        {"restaurant_id": 20, "name": "Cinnamon Roll", "description": "Sweet roll with cinnamon and cream cheese frosting", "image": "foods/cinnamon_roll.png", "price": 4},
        {"restaurant_id": 20, "name": "Blueberry Muffin", "description": "Moist muffin with blueberries", "image": "foods/blueberry_muffin.png", "price": 3},
        {"restaurant_id": 20, "name": "Chocolate Chip Cookie", "description": "Sweet cookie with chocolate chips", "image": "foods/chocolate_chip_cookie.png", "price": 2},
        {"restaurant_id": 20, "name": "Coffee", "description": "Hot coffee with a choice of milk", "image": "beverages/coffee.png", "price": 3},
        {"restaurant_id": 20, "name": "Tea", "description": "Hot tea with a choice of flavors", "image": "beverages/tea.png", "price": 3},
        {"restaurant_id": 20, "name": "Hot Chocolate", "description": "Sweet hot chocolate with whipped cream", "image": "beverages/hot_chocolate.png", "price": 4},

        # Salad Bar
        {"restaurant_id": 21, "name": "Greek Salad", "description": "Fresh salad with tomatoes, cucumbers, olives, and feta cheese", "image": "foods/greek_salad.png", "price": 10},
        {"restaurant_id": 21, "name": "Caesar Salad", "description": "Classic salad with romaine lettuce, croutons, and Parmesan cheese", "image": "foods/caesar_salad.png", "price": 8},
        {"restaurant_id": 21, "name": "Cobb Salad", "description": "Hearty salad with chicken, bacon, avocado, eggs, and blue cheese", "image": "foods/cobb_salad.png", "price": 12},
        {"restaurant_id": 21, "name": "Spinach Salad", "description": "Healthy salad with spinach, strawberries, almonds, and goat cheese", "image": "foods/spinach_salad.png", "price": 10},
        {"restaurant_id": 21, "name": "Quinoa Salad", "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables", "image": "foods/quinoa_salad.png", "price": 10},
        {"restaurant_id": 21, "name": "Green Juice", "description": "Healthy juice with kale, spinach, and apple", "image": "beverages/green_juice.png", "price": 5},
        {"restaurant_id": 21, "name": "Herbal Tea", "description": "Hot tea with a choice of herbs", "image": "beverages/herbal_tea.png", "price": 3},
        {"restaurant_id": 21, "name": "Fruit Smoothie", "description": "Blended smoothie with a choice of fruits and almond milk", "image": "beverages/fruit_smoothie.png", "price": 6},

        # Ramen House
        {"restaurant_id": 22, "name": "Tonkotsu Ramen", "description": "Ramen with pork bone broth, pork belly, and soft-boiled egg", "image": "foods/tonkotsu_ramen.png", "price": 12},
        {"restaurant_id": 22, "name": "Shoyu Ramen", "description": "Ramen with soy sauce broth, chicken, and soft-boiled egg", "image": "foods/shoyu_ramen.png", "price": 11},
        {"restaurant_id": 22, "name": "Miso Ramen", "description": "Ramen with miso broth, corn, and soft-boiled egg", "image": "foods/miso_ramen.png", "price": 11},
        {"restaurant_id": 22, "name": "Gyoza", "description": "Japanese dumplings with pork and vegetables", "image": "foods/gyoza.png", "price": 6},
        {"restaurant_id": 22, "name": "Takoyaki", "description": "Fried octopus balls with bonito flakes and mayo", "image": "foods/takoyaki.png", "price": 6},
        {"restaurant_id": 22, "name": "Sake", "description": "Japanese rice wine", "image": "beverages/sake.png", "price": 6},
        {"restaurant_id": 22, "name": "Green Tea", "description": "Hot Japanese green tea", "image": "beverages/green_tea.png", "price": 3},
        {"restaurant_id": 22, "name": "Plum Wine", "description": "Sweet Japanese wine made from plums", "image": "beverages/plum_wine.png", "price": 7},

        # Ice Cream Shop
        {"restaurant_id": 23, "name": "Vanilla Ice Cream", "description": "Creamy ice cream with vanilla flavor", "image": "foods/vanilla_ice_cream.png", "price": 3},
        {"restaurant_id": 23, "name": "Chocolate Ice Cream", "description": "Rich ice cream with chocolate flavor", "image": "foods/chocolate_ice_cream.png", "price": 3},
        {"restaurant_id": 23, "name": "Strawberry Ice Cream", "description": "Sweet ice cream with strawberry flavor", "image": "foods/strawberry_ice_cream.png", "price": 3},
        {"restaurant_id": 23, "name": "Mint Chocolate Chip Ice Cream", "description": "Refreshing ice cream with mint and chocolate chips", "image": "foods/mint_chocolate_chip_ice_cream.png", "price": 4},
        {"restaurant_id": 23, "name": "Cookie Dough Ice Cream", "description": "Delicious ice cream with chunks of cookie dough", "image": "foods/cookie_dough_ice_cream.png", "price": 4},
        {"restaurant_id": 23, "name": "Root Beer Float", "description": "Classic dessert with root beer and vanilla ice cream", "image": "beverages/root_beer_float.png", "price": 5},
        {"restaurant_id": 23, "name": "Milkshake", "description": "Creamy milkshake with vanilla, chocolate, or strawberry", "image": "beverages/milkshake.png", "price": 5},
        {"restaurant_id": 23, "name": "Iced Coffee", "description": "Refreshing iced coffee with a choice of milk", "image": "beverages/iced_coffee.png", "price": 4},

        # Sandwich Shop
        {"restaurant_id": 24, "name": "Turkey Sandwich", "description": "Sandwich with turkey, lettuce, tomato, and mayo", "image": "foods/turkey_sandwich.png", "price": 8},
        {"restaurant_id": 24, "name": "Ham Sandwich", "description": "Sandwich with ham, cheese, lettuce, and mustard", "image": "foods/ham_sandwich.png", "price": 8},
        {"restaurant_id": 24, "name": "Tuna Salad Sandwich", "description": "Sandwich with tuna salad and lettuce", "image": "foods/tuna_salad_sandwich.png", "price": 8},
        {"restaurant_id": 24, "name": "BLT Sandwich", "description": "Classic sandwich with bacon, lettuce, and tomato", "image": "foods/blt_sandwich.png", "price": 8},
        {"restaurant_id": 24, "name": "Grilled Cheese Sandwich", "description": "Comforting sandwich with melted cheese", "image": "foods/grilled_cheese_sandwich.png", "price": 6},
        {"restaurant_id": 24, "name": "Soda", "description": "Refreshing carbonated drink", "image": "beverages/soda.png", "price": 3},
        {"restaurant_id": 24, "name": "Iced Tea", "description": "Refreshing iced tea", "image": "beverages/iced_tea.png", "price": 3},
        {"restaurant_id": 24, "name": "Coffee", "description": "Hot coffee with a choice of milk", "image": "beverages/coffee.png", "price": 3},

        # Pancake House
        {"restaurant_id": 25, "name": "Buttermilk Pancakes", "description": "Fluffy pancakes served with butter and maple syrup", "image": "foods/buttermilk_pancakes.png", "price": 8},
        {"restaurant_id": 25, "name": "Blueberry Pancakes", "description": "Pancakes with blueberries served with butter and maple syrup", "image": "foods/blueberry_pancakes.png", "price": 9},
        {"restaurant_id": 25, "name": "Chocolate Chip Pancakes", "description": "Pancakes with chocolate chips served with butter and maple syrup", "image": "foods/chocolate_chip_pancakes.png", "price": 9},
        {"restaurant_id": 25, "name": "Bacon and Egg Pancakes", "description": "Pancakes with bacon and eggs served with butter and maple syrup", "image": "foods/bacon_and_egg_pancakes.png", "price": 10},
        {"restaurant_id": 25, "name": "Banana Nut Pancakes", "description": "Pancakes with bananas and nuts served with butter and maple syrup", "image": "foods/banana_nut_pancakes.png", "price": 9},
        {"restaurant_id": 25, "name": "Coffee", "description": "Hot coffee with a choice of milk", "image": "beverages/coffee.png", "price": 3},
        {"restaurant_id": 25, "name": "Orange Juice", "description": "Freshly squeezed orange juice", "image": "beverages/orange_juice.png", "price": 4},
        {"restaurant_id": 25, "name": "Milk", "description": "Cold milk", "image": "beverages/milk.png", "price": 2},
    ]

    # Populate restaurants table
    for restaurant in restaurants:
        add_restaurant(db, restaurant["name"], restaurant["description"], restaurant["image"])

    # Populate foods table
    for food in foods:
        add_food(db, food["restaurant_id"], food["name"], food["description"], food["image"], food["price"])

    print("Data populated successfully!")

if __name__ == "__main__":
    main()