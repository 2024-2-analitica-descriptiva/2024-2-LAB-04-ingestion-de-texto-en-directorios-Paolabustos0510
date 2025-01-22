# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import shutil
    import pandas as pd
    import zipfile


    # Ruta del archivo .zip
    zip_path = "files/input.zip"

    # Ruta de extracción
    extract_dir = "files/input"

    def create_folder(path):
    # Verificar si la carpeta ya existe y eliminarla
        if os.path.exists(path):
            shutil.rmtree(path)  # Eliminar la carpeta existente

        # Verificar si existe la carpeta 'input'
        if not os.path.exists(path):
            os.makedirs(path)


    create_folder(extract_dir)

    with zipfile.ZipFile(zip_path , "r") as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(zip_path .split("/")[0])
        
    output_dir = "files/output"
    create_folder(output_dir)


    for i in os.listdir(extract_dir):
        type_folder = os.path.join(extract_dir, i)
        name = f"{i}_dataset.csv"
        all_data = []  

        for j in os.listdir(type_folder):
            sentiment = j
            sentiment_folder = os.path.join(type_folder, j)

            for k in os.listdir(sentiment_folder):
                file_path = os.path.join(sentiment_folder, k)
                
                # Leer el archivo usando Pandas
                try:
                    df = pd.read_csv(file_path, header=None, names=["phrase"], encoding="utf-8")
                    df["target"] = sentiment  
                    all_data.append(df)  
                except Exception as e:
                    print(f"Error procesando el archivo {file_path}: {e}")
            
        # Verificar si el archivo de salida ya existe y eliminarlo si es necesario
        output_file = os.path.join(output_dir, f"{i}_dataset.csv")
        if os.path.exists(output_file):
            os.remove(output_file)  

        if all_data:
            final_df = pd.concat(all_data, ignore_index=True)
            output_file = os.path.join(output_dir, name)
            final_df.to_csv(output_file, index=False, encoding="utf-8")
            print(f"Archivo guardado: {output_file}")

if __name__ == "__main__":
    print(pregunta_01())