import aiomax
import logging

import key

bot = aiomax.Bot(key.k, default_format="markdown")

#клавиатура:
kb = aiomax.buttons.KeyboardBuilder()
kb2 = aiomax.buttons.KeyboardBuilder()
kb3 = aiomax.buttons.KeyboardBuilder()
kb4 = aiomax.buttons.KeyboardBuilder()

#кнопки 1
b1 = aiomax.buttons.CallbackButton("Внутренний мир вуза", "pl_liver")
b2 = aiomax.buttons.CallbackButton("Мероприятия вуза", "pl_trash")
kb.row(b1,b2)

#кнопки 2
b3 = aiomax.buttons.CallbackButton("1 институт", "pl_l")
b4 = aiomax.buttons.CallbackButton("2 институт", "pl_t")
b5 = aiomax.buttons.CallbackButton("3 институт", "pl_p")
b6 = aiomax.buttons.CallbackButton("4 институт", "pl_k")
b7 = aiomax.buttons.CallbackButton("5 институт", "pl_m")
b8 = aiomax.buttons.CallbackButton("6 институт", "pl_h")
b9 = aiomax.buttons.CallbackButton("7 институт", "pl_g")
b11 = aiomax.buttons.CallbackButton("Назад", "pl_v")
kb2.row(b3, b4, b5) 
kb2.row(b6, b7, b8)
kb2.row(b9, b11)

#переменная с ссылкой
l1 = "https://forms.yandex.ru/u/69149e7250569002112c5ae0"
l2 = "https://forms.yandex.ru/u/691769e690fa7b30ff668f78"
l3 = "https://forms.yandex.ru/u/69176b5f95add54b1e6b51f9"

#кнопки 3
b4_url = aiomax.buttons.LinkButton("1 Ссылка",l1)
b5_url = aiomax.buttons.LinkButton("2 Ссылка",l2)
b6_url = aiomax.buttons.LinkButton("3 Ссылка",l3)
kb3.row(b4_url, b5_url)
kb3.row(b6_url, b11)

#кнопки 4
p  = aiomax.buttons.CallbackButton("Назад", "pl_liver")
kb4.add(p)

@bot.on_bot_start()
async def info(pd: aiomax.BotStartPayload):
    await pd.send("Вас приветствует чат-бот СГТУ, Волга бот! ",keyboard=kb)

@bot.on_command("menu")
async def menu(ctx: aiomax.CommandContext):
    await ctx.reply("Вот снова я, Волга бот",keyboard=kb)

@bot.on_button_callback("pl_liver")
async def on_liver(callback: aiomax.Callback):
    await callback.answer(text="Направления в СГТУ:\n 1. ИнЭн\n 2. ИММТ\n 3. ИнЭТиП\n 4. ИнПИТ\n 5. ФТиП\n 6. УРБАС\n 7. СЭИ", keyboard=kb2)

@bot.on_button_callback("pl_trash")
async def on_trash(callback: aiomax.Callback):
    await callback.answer(text="В нашем ВУЗе так много крутых мероприятий, вот держи несколько из них:\nДень открытых дверей «Правила приема в 2026 году на программы ВО» (12.02.26) \n День открытых дверей «Поступай правильно» (05.03.26) \n День открытых дверей «Институт машиностроения, материаловедения и транспорта (15.04.26)»", keyboard=kb3)

@bot.on_button_callback("pl_l")
async def on_t(callback: aiomax.Callback):
    await callback.answer(text="ИНСТИТУТ ЭНЕРГЕТИКИ, кафедры:\n 1.«Промышленная теплотехника» (ПТ)\n 2.«Электроэнергетика и электротехника» (ЭЛЭТ)\n 3.«Тепловая и атомная энергетика» имени А.И. Андрющенко (ТАЭ) ", keyboard=kb4)

@bot.on_button_callback("pl_t")
async def on_l1(callback: aiomax.Callback):
    await callback.answer(text="ИНСТИТУТ МАШИНОСТРОЕНИЯ, МАТЕРИАЛОВЕДЕНИЯ И ТРАНСПОРТА, кафедры:\n 1.«Сварка и металлургия» (СМ)\2.«Технология машиностроения» (ТМС)\n 3.«Техническая механика и мехатроника» (ТММ)\n 4.«Материаловедение и биомедицинская инженерия» (МБИ)\n 5.«Инженерная геометрия и основы САПР» (ИГС)\n 6.«Организация перевозок, безопасность движения и сервис автомобилей» (ОПБС) ", keyboard=kb4)

@bot.on_button_callback("pl_p")
async def on_l2(callback: aiomax.Callback):
    await callback.answer(text="ИНСТИТУТ ЭЛЕКТРОННОЙ ТЕХНИКИ И ПРИБОРОСТРОЕНИЯ, кафедры:\n 1.«Системотехника и управление в технических системах» (СТУ)\n 2.«Радиоэлектроника и телекоммуникации» (РТ)\n 3.«Приборостроение» (ПБС)\n 4.«Электронные приборы и устройства» (ЭПУ)\n 5.«Информационная безопасность автоматизированных систем» (ИБС) ", keyboard=kb4)

@bot.on_button_callback("pl_k")
async def on_l3(callback: aiomax.Callback):
    await callback.answer(text="ИНСТИТУТ ПРИКЛАДНЫХ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И КОММУНИКАЦИЙ, кафедры:\n 1.«Информационно-коммуникационные системы и программная инженерия» (ИКСП)\n 2.«Прикладные информационные технологии» (ПИТ)\n 3.«Медиакоммуникации» (МКМ)\n 4.«Переводоведение и межкультурная коммуникация» (ПМК)\n 5.«Информационные системы и моделирование» (ИСМ)\n 6.«Программное обеспечение вычислительных систем и компьютерных сетей» (ПВКС) ", keyboard=kb4)

@bot.on_button_callback("pl_m")
async def on_l4(callback: aiomax.Callback):
    await callback.answer(text="ФИЗИКО-ТЕХНИЧЕСКИЙ ИНСТИТУТ, кафедры:\n 1.«Математика и моделирование» (МиМ)\n 2.«Прикладная математика и системный анализ» (ПМиСА)\n 3.«Физика» (ФИЗ)\n 4.«Химия и хиУРБАСмическая технология материалов» (ХИМ) ", keyboard=kb4)

@bot.on_button_callback("pl_h")
async def on_l5(callback: aiomax.Callback):
    await callback.answer(text="ИНСТИТУТ УРБАНИСТИКИ, АРХИТЕКТУРЫ И СТРОИТЕЛЬСТВА, кафедры:\n 1.«Архитектура» (АРХ)\n 2.«Дизайн архитектурной среды» (ДАС)\n 3.«Теплогазоснабжение и нефтегазовое дело» (ТНД)\n 4.«Строительные материалы, конструкции и технологии» (СМКТ)\n 5.«Экология и техносферная безопасность» (ЭТБ)\n 6.«Транспортное строительство» (ТСТ) ", keyboard=kb4)

@bot.on_button_callback("pl_g")
async def on_l6(callback: aiomax.Callback):
    await callback.answer(text="СОЦИАЛЬНО-ЭКОНОМИЧЕСКИЙ ИНСТИТУТ, кафедры:\n 1.Бухгалтерского учета, анализа хозяйственной деятельности и аудита (БУХ)\n 2.«Производственный менеджмент» (ПМН)\n 3.Таможенного дела и товароведения (ТМЖ)\n 4.«Экономика и маркетинг» (ЭКМ)\n 5.«Отраслевое управление и экономическая безопасность» (ОУБ)\n 6.«Политология и социология» (ПС)\n 7.«История и философия» (ИФ)\n 8.«Иностранные языки и профессиональная коммуникация» (ИПК)\n 9.«Физическая культура и спорт» (ФКС) ", keyboard=kb4)

@bot.on_button_callback("n")
async def on_l7(callback: aiomax.Callback):
    await callback.answer(text="Вот небольшая информация о СГТУ:\n 1. Институт энергетики\n 2. Институт машиностроения, материаловедени и трансопрта\n 3. Институт электронной техники и приборостроения\n 4. Институт прикладных информационных технологий и комуникаций\n 5. Физико-технический институт\n 6. Институт урбанистики, архитектуры и строительства\n 7. Социально-экономический институт\n 8. Устройство кампуса", keyboard=kb2)

@bot.on_button_callback("pl_v")
async def on_l8(callback: aiomax.Callback):
    await callback.answer(text="Вас приветствует чат-бот СГТУ, Волга бот! ",keyboard=kb)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
