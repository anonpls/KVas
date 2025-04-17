"""
Файл с константами для бота ВКонтакте по загрузке клипов.
"""

# Токены и идентификаторы
# Токены и идентификаторы
BOT_TOKEN = "vk1.a.vBQIHQV9P6rYRxLGUBpQlK_4jTS8CGaRQ-YcK68nSjKnxVJ12xYfbkFYburQaljt5u5S7c3f3u2bDodJiQ4XaVxrrK8O4MDLSWr9B9jeo90BLdPtmU_92O7IYSiTUCGDB0gSFjrueby-PlEscVZ5eJdxt4FOww-RJ-F1RoWF4YbwkeVcQU2jblVUl09zews6UGQ8Ad_IOtFSO4EPYsbRKg"
GROUP_ID = 230138398
CONVERSATION_ID = 2000000001  # ID беседы из ссылки https://vk.com/im/convo/2000000059
API_VERSION = "5.199"  # Версия API ВКонтакте

# Пути к файлам и директориям
CLIPS_DIR = "clips"  # Директория для сохранения клипов

# Настройки хранения клипов
CLEANUP_INTERVAL_HOURS = 24  # Интервал проверки и удаления старых клипов в часах

# Настройки логирования
LOG_LEVEL = "INFO"  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Формат сообщений лога

# Настройки загрузки видео
USE_YTDLP = True  # Использовать yt-dlp для загрузки видео
YTDLP_PATH = "yt-dlp"  # Путь к исполняемому файлу yt-dlp
