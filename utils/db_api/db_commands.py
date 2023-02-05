from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, tg_id, username, first_name):
        sql = ''' INSERT INTO main_botuser ("tg_id","username","first_name") VALUES ($1,$2,$3)'''
        return await self.execute(sql, tg_id, username, first_name, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM main_botuser"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM main_botuser WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_admin(self, **kwargs):
        sql = "SELECT * FROM main_botadmin WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM main_botuser"
        return await self.execute(sql, fetchval=True)

    async def select_all_admin(self):
        sql = "SELECT * from main_botadmin"
        return await self.execute(sql, fetch=True)

    async def delete_users(self):
        await self.execute("DELETE FROM main_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE main_user", execute=True)
