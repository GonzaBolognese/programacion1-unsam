import os
def archivos_png(directorio):
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file[-3:] == 'png':
                print(file)
            

if __name__ == '__main__':
    import sys
    archivos_png(sys.argv[1])