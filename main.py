from PIL import Image
import os
import platform

def make_pdf_all(dir_path):
    if platform.system() == "Windows":
        join = str("/")
        dir_files = [dir_path + join + f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return dir_files

    elif platform.system() == "Linux":
        join = str('\'')
        dir_files = [dir_path + join + f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return dir_files

def make_pdf_only_selected(selected_files, file_name, pdf_location):
    images_list = []
    for f in selected_files:
        try:
            images_list.append((Image.open(f)).convert('RGB'))
        except IOError:
            pass
    os.chdir(pdf_location)
    images_list[0].save(file_name, save_all=True, append_images=images_list[1:])

if __name__ == '__main__':
    print("This Is The Main Backend Module!")
