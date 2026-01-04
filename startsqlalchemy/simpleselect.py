from sqlalchemy import select
from sqlalchemy.orm import Session

import startsqlalchemy.createandpersist as engine_module
from startsqlalchemy.model import User, Address

session = Session(engine_module.engine)

stmt = select(User).where(User.name.in_(["Sponge Bob", "Sandy"]))

for user in session.scalars(stmt):
    print(user)


stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "Sandy")
    .where(Address.email_address == "[email protected]")
)

sandy_address = session.scalars(stmt).first()
print(sandy_address)