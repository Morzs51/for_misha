from video_preprocessing import VideoPreprocessing
import cv2

def run_test():
    test = VideoPreprocessing()

    img1 = cv2.imread("1.jpg")
    img2 = cv2.imread("2.jpg")
    img3 = cv2.imread("3.jpg")

    img1 = test.change_image_color_mode(img1, cv2.COLOR_BGR2GRAY)
    cv2.imshow('после изменений', img1)
    cv2.waitKey(0)
    img1 = test.change_image_color_mode(img1, cv2.COLOR_GRAY2BGR)

    test.is_image_blured(img1)
    test.is_image_blured(img3)

    img2 = test.set_image_size(img2)
    cv2.imshow("изображение с измененныым размером", img2)
    cv2.waitKey(0)

    merge_img = test.merge_images(cv2.imread("1.jpg"), cv2.imread("2.jpg"))
    cv2.imshow("склеенное изображение", merge_img)
    cv2.waitKey(0)

    img3 = test.image_histogram_alignment(img3)
    cv2.imshow("изображение с измененной контрастностью", img3)
    cv2.waitKey(0)

    test.set_video_capture()

    frame = test.get_color_frame()
    depth_frame = test.get_depth_frame(frame)
    cv2.imshow("кадр глубины", depth_frame)
    cv2.waitKey(0)



# Путь к папке с изображениями
image_folder = "C:\\Users\\serzh\\PycharmProjects\\pythonProject\\rgb"

import os

# Путь к папке с изображениями
image_folder = "C:\\Users\\serzh\\PycharmProjects\\pythonProject\\rgb"

# Получаем список файлов в папке
image_files = os.listdir(image_folder)

# Цикл по всем файлам в папке
for image_file in image_files:
    if image_file.endswith('.jpg') or image_file.endswith('.png'):  # Укажите нужное расширение файла
        old_path = os.path.join(image_folder, image_file)

        # Создаем новое имя файла (без расширения)
        new_name = 0  # Задайте новое имя файла

        # Получаем расширение файла
        file_extension = os.path.splitext(image_file)[1]

        # Создаем новый путь к файлу с новым именем и старым расширением
        new_name = str(new_name)
        new_path = os.path.join(image_folder, new_name + file_extension)
        new_name = int(new_name)
        new_name +=1
        # Переименовываем файл
        os.rename(old_path, new_path)

# Теперь все изображения в папке переименованы без части старого имени

