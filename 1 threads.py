import requests
import threading

def get_name():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()
        name = data["results"][0]["name"]["first"]
        print(name)
    else:
        print(response.status_code)


if __name__ == "__main__":
    #* ejecución secuencial
    # for _ in range(10):
    #     get_name()

    #! ejecución concurrente
    threads = []
    for _ in range(20):
        #configuramos el hilo
        thread = threading.Thread(target=get_name)
        threads.append(thread)
        #iniciamos el hilo
        thread.start()
    
    for thread in threads:
        thread.join()