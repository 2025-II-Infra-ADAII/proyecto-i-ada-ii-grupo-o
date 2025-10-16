from tkinter import Tk, filedialog
from voraz import roV


#cargar las fincas en tuplas con sus datos (ts, tr, p)

def cargar_txt(load_file):
    finca = []
    with open(load_file, "r") as file:
        for line in file:
            ts, tr, p = map(int, line.strip().split())
            finca.append((ts, tr, p))
    return finca

def choose_file():
    Tk().withdraw()  
    file_path = filedialog.askopenfilename(title="Selecciona el archivo de la finca",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    return file_path    

#guardar los resultados en una tabla
def tabla(finca, orden):
    tiempo = 0
    filas = []
    costo_total = 0

    for i in orden:
        ts, tr, p = finca[i]
        fin_riego = tiempo + tr
        retraso = max(0, fin_riego - ts)
        costo_p = retraso * p
        filas.append((i, ts, tr, p, tiempo, fin_riego, retraso, costo_p))
        costo_total += costo_p
        tiempo = fin_riego

    return filas, costo_total

#Funcion para guardar los resultados en un archivo de txt
def save_results(nombre_archivo, filas, costo_total):
    with open(nombre_archivo, "w") as file:
        #encabezado alineado 
        file.write(f"{'Tablon':<8}{'ts':<8}{'tr':<8}{'p':<8}{'Inicio':<10}{'Fin':<10}{'Retraso':<10}{'Costo':<10}\n")
        file.write("="*72 + "\n")

        for fila in filas:
            i, ts, tr, p, inicio, fin, retraso, costo = fila
            file.write(f"{i:<8}{ts:<8}{tr:<8}{p:<8}{inicio:<10}{fin:<10}{retraso:<10}{costo:<10}\n")        
        file.write("="*72 + "\n")
        file.write(f"{'Costo total:':<62}{costo_total:<10}\n")      
        


        #file.write("Tablon\tts\ttr\tp\tInicio\tFin\tRetraso\tCosto\n")
        # for fila in filas:
        #     file.write("\t".join(map(str, fila)) + "\n")
        # file.write(f"Costo total: {costo_total}\n")




if __name__ == "__main__":
    archivo = choose_file()
    finca = cargar_txt(archivo)
    

    orden, _ = roV(finca)
    filas, costo_total = tabla(finca, orden)

    nombre_archivo = "resultados.txt"
    save_results(nombre_archivo, filas, costo_total)

    print(f"Resultados guardados en {nombre_archivo}")
    

