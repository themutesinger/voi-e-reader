
import speech_recognition as sr

CHUNK = 20
r = sr.Recognizer()
print("Аудио файл должен быть в формате .wav")
sourcepath = input("Введите имя аудио файла: ")
duration = int(input("Введите продожительность аудио в секундах: "))
file_name = input("Выберите название файла: ")
value = sr.AudioFile(sourcepath)
with open(f'{file_name}.txt', 'w') as file:
    file.write('')
servererror = 0
if duration < CHUNK:
    try:
        with value as source:
            audio = r.record(source)
            result = r.recognize_google(audio, language='ru')
        with open(f'{file_name}.txt', 'a') as file:
            file.write(result)
        # print(f"offset:{offset}")
    except Exception as suvan:
        print(suvan)
        print("Ошибка соединения с сервером, но это небольшая проблема")
        servererror += 1
else:
    for offset in range(0, duration, CHUNK):
        try:
            with value as source:
                audio = r.record(source, duration=CHUNK, offset=offset)
                result = r.recognize_google(audio, language='ru')
            with open(f'{file_name}.txt', 'a') as file:
                file.write(result)
            # print(f"offset:{offset}")
            print(f"Завершено {int(offset*100/duration)}%")
        except Exception as suvan:
            print(suvan)
            print("Ошибка соединения с сервером, но это небольшая проблема")
            servererror += 1
            continue
print("Завершено 100%")
print("Готово!")
print(f"Количество потерь по 20 секунд : {servererror}")
