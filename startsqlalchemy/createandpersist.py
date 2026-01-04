from sqlalchemy import create_engine

from startsqlalchemy.model import Base, Address, User

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session

with Session(engine) as session:
    spongbob = User(
        name = 'Sponge Bob',
        fullname = 'Sponge Bob Square Pants',
        addresses = [Address(email_address="[email protected]")],
    )

    sandy = User(
        name = 'Sandy',
        fullname = 'Sandy Cheeks',
        addresses = [
            Address(email_address="[email protected]"),
            Address(email_address="[email protected]")
        ],
    )
    patrick = User(name='Patrick', fullname='Patrick Star')

    session.add_all([spongbob, sandy, patrick])
    session.commit()