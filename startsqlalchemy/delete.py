from sqlalchemy import select
from sqlalchemy.orm import Session

import startsqlalchemy.createandpersist as engine_module
from startsqlalchemy.model import User, Address


session = Session(engine_module.engine)

sandy = session.get(User, 2)

stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "Sandy")
    .where(Address.email_address == "[email protected]")
)

sandy_address = session.scalars(stmt).first()
sandy.addresses.remove(sandy_address)


stmt = select(User).where(User.name == "Patrick")
patrick = session.scalars(stmt).one()

session.delete(patrick)
session.commit()