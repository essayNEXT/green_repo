FROM python:3.10.7
# стоврення користувача, який не є рутом
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
# тут ми сворюємо користувача з ім'м green_team, який не є рутом, і його UID за
# замовченням буде 1000 (раніше тут було ARG UID=1000 ENV UID=${UID}), він може бути
# замінений при старті контейнера передачою змінної або в файлі docker-compose.yaml
# або як аргумент команди docker
RUN useradd -m -u $UID green_team
USER green_team

# Инициализация проекта
WORKDIR /home/green_team/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN  pip install -r requirements.txt
COPY . .
CMD ["python3", "-m", "bot"]