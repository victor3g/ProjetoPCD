import concurrent.futures
import random
import time

# Função para contar os pontos dentro do círculo
def contar_pontos_dentro_do_circulo(amostras):
    pontos_dentro_do_circulo = 0
    for _ in range(amostras):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distancia = x ** 2 + y ** 2
        if distancia <= 1:
            pontos_dentro_do_circulo += 1

    return pontos_dentro_do_circulo

# Função para estimar Pi com multiprocessing
def estimar_pi_multiprocessing(num_amostras):
    num_processos = 4  # Número de processos
    amostras_por_processo = num_amostras // num_processos
    with concurrent.futures.ProcessPoolExecutor() as executor:
        resultados = executor.map(contar_pontos_dentro_do_circulo, [amostras_por_processo] * num_processos)
    pontos_dentro_do_circulo = sum(resultados)
    return 4 * pontos_dentro_do_circulo / num_amostras

# Função para estimar Pi com threading
def estimar_pi_threads(num_amostras):
    num_threads = 4  # Número de threads
    amostras_por_thread = num_amostras // num_threads
    resultados = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = [executor.submit(contar_pontos_dentro_do_circulo, amostras_por_thread) for _ in range(num_threads)]
        for futuro in concurrent.futures.as_completed(futuros):
            resultados.append(futuro.result())
    pontos_dentro_do_circulo = sum(resultados)
    return 4 * pontos_dentro_do_circulo / num_amostras

if __name__ == "__main__":
    num_amostras = 100000000 # Número de pontos a serem gerados
    tempo_inicio = time.time()

    # Calcula Pi com multiprocessing
    estimativa_pi_mp = estimar_pi_multiprocessing(num_amostras)
    print(f"Estimativa de Pi com multiprocessing: {estimativa_pi_mp}")
    print(f"Tempo de execução com multiprocessing: {time.time() - tempo_inicio} segundos\n")

    tempo_inicio = time.time()
    # Calcula Pi com threading
    estimativa_pi_threads = estimar_pi_threads(num_amostras)
    print(f"Estimativa de Pi com threading: {estimativa_pi_threads}")
    print(f"Tempo de execução com threading: {time.time() - tempo_inicio} segundos\n")