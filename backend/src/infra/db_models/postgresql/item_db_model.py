""" Defines the Items database model
"""


import uuid
from sqlalchemy import String, Float, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from src.infra.db_models.postgresql.postgresql_base import Base


class ItemsDBModel(Base):
    """ Items database model
    """

    __tablename__ = "items"

    item_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    codebar: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        unique=True
    )
    name: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
        unique=True
    )
    description: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )
    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    state: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
