import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session as db, User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    user = graphene.Field(User)

    @staticmethod
    def resolve_user(info):
        return info.context.get('user')


schema = graphene.Schema(query=Query)