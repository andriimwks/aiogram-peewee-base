from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from app.misc import dp, _
from app.models import User

@dp.message_handler(
    filters.ChatTypeFilter([types.ChatType.PRIVATE]),
    commands=['start', 'help'],
    state='*'
)
async def cmd_start_private(message: types.Message) -> None:
    user, __ = User.get_or_create(
        id=message.from_user.id,
        defaults={
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
            'language_code': message.from_user.language_code
        }
    )
    
    await message.answer(_('Hello, {first_name}!').format(first_name=user.first_name))

@dp.message_handler(commands=['cancel'])
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    await message.answer(_('Action canceled.'))
    await state.finish()

@dp.callback_query_handler(filters.Text(equals='cancel'), state='*')
async def call_cancel(call: types.CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(_('Action canceled.'))
    await state.finish()
