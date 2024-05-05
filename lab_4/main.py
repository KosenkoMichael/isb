import multiprocessing as mp
import hashlib
import time

cores = mp.cpu_count()

hash = "2083ca0a0960daaa60a509a298d2eec8"
bin_list = [518901, 521324, 544714, 524468, 528041, 538994, 551960, 553420, 553691]
num_end = 1994


def search(bin, mid):
    return (
        f"{bin}{str(mid).zfill(6)}1994"
        if hashlib.md5(f"521324{str(mid).zfill(6)}{num_end}".encode()).hexdigest()
        == hash
        else False
    )


if __name__ == "__main__":
    start_time = time.time()
    with mp.Pool(processes=cores) as p:
        for result in p.starmap(
            search, [(val1, val2) for val1 in bin_list for val2 in range(0, 1000000)]
        ):
            if result:
                print(f"we have found {result} and have terminated pool")
                p.terminate()
                break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения кода: {execution_time} секунд")
