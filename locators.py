# Хедер - кнопка "Конструктор", логотип "Stellar Burgers", кнопка "Личный кабинет"
header_constructor_btn = './/header//li[1]/a/p'
header_logo_btn = './/header/nav/div[@class="AppHeader_header__logo__2D0X2"]/a'
header_personal_area_btn = './/header/nav/a'

# Вход в личный кабинет - ссылки "Зарегистрироваться" и "Восстановить пароль"
do_register = './/main/div/div/p[1]/a[text()="Зарегистрироваться"]'
password_recovery = './/main/div/div/p[2]/a[text()="Восстановить пароль"]'

# Регистрация - инпуты "Имя", "Email", "Пароль", кнопка "Зарегистрироваться"
input_name = './/main/div/form[@class="Auth_form__3qKeq mb-20"]/fieldset[1]/div/div/input'
input_email = './/main/div/form[@class="Auth_form__3qKeq mb-20"]/fieldset[2]/div/div/input'
input_password = './/main/div/form[@class="Auth_form__3qKeq mb-20"]/fieldset[3]/div/div/input'
register_btn = './/*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]'

# Регистрация/восстановление пароля - ссылка "Войти"
login_link = './/*[@id="root"]/div/main/div/div/p/a[text()="Войти"]'

# Авторизация - инпуты "Email", "Пароль", кнопка "Войти"
login_input_email = './/main/div/form[@class="Auth_form__3qKeq mb-20"]/fieldset[1]/div/div/input'
login_input_password = './/main/div/form[@class="Auth_form__3qKeq mb-20"]/fieldset[2]/div/div/input'
login_btn = './/*[@id="root"]/div/main/div/form/button[text()="Войти"]'

# Текст ошибки при регистрации с некорректным паролем
incorrect_password = './/main/div/form/fieldset[3]/div/p[@class="input__error text_type_main-default"]'

# Кнопка "Войти в аккаунт" / "Оформить заказ" появляется на главной странице после авторизации
login_or_make_order_btn = './/main/section[2]/div/button'

# Личный кабинет - инпуты "Имя", "Email", кнопки "Сохранить" и "Выход"
profile_name = './/main/div/div/div/ul/li[1]/div/div/input'
profile_email = './/main/div/div/div/ul/li[2]/div/div/input'
profile_save_btn = './/main/div/div/div/div/button[2]'
profile_logout_btn = './/main/div/nav/ul/li[3]/button[text()="Выход"]'

# Конструктор - кнопки и разделы «Булки», «Соусы», «Начинки»
constructor_category_buttons = './/main/section[1]/div[1]'
constructor_bread_btn = './/main/section[1]/div[1]/div[1]'
constructor_bread_title = './/main/section[1]/div[2]/h2[1][text()="Булки"]'
constructor_sauce_btn = './/main/section[1]/div[1]/div[2]/span[text()="Соусы"]'
constructor_sauce_title = './/main/section[1]/div[2]/h2[2][text()="Соусы"]'
constructor_filling_btn = './/main/section[1]/div[1]/div[3]/span[text()="Начинки"]'
constructor_filling_title = './/main/section[1]/div[2]/h2[3][text()="Начинки"]'
