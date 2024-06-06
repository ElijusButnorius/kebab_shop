from main import app, db, Product

with app.app_context():

    db.create_all()


    product1 = Product(name='Beef kebab', sudetis='Beef, vegetables, souce', aktyvi=True)
    product2 = Product(name='Lamb kebab', sudetis='Lamb, vegetables, souce', aktyvi=True)
    product3 = Product(name='Chiken kebab', sudetis='Chiken, vegetables, souce', aktyvi=True)
    product4 = Product(name='Pork kebab', sudetis='Pork,vegetables,souce', aktyvi=True)
    product5 = Product(name='Fried dumplings', sudetis='Beef meat', aktyvi=True)


    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.commit()
