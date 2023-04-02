from sqlalchemy import Column, Integer, String, ARRAY, MetaData, DateTime
from sqlalchemy.ext.declarative import declarative_base


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Document(Base):
    __tablename__ = 'documents'

    id              = Column(Integer, primary_key=True)
    rubrics         = Column(ARRAY(String))
    text            = Column(String)
    created_date    = Column(DateTime)