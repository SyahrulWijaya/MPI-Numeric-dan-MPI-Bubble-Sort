import time
def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len - 1):
        flag = 0

        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if flag == 0:
            break

    return arr
time_start=time.time()

arr = [100, 60, 80, 30, 20, 70, 50, 40, 10, 90]
sorted_arr = bubble_sort(arr)
print("List sorted with bubble sort in ascending order:", sorted_arr)

time_end=time.time()

waktu_eksekusi=time_end-time_start

print ("waktu eksekusi=",waktu_eksekusi)
