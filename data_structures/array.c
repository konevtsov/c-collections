/*
This is realization integer array on C
*/
#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int *data;
    int size;
    int capacity;
} DynamicArray;


DynamicArray init(int initial_capacity)
{
    DynamicArray arr;
    arr.data = malloc(sizeof(int) * initial_capacity);
    arr.size = 0;
    arr.capacity = initial_capacity;
    return arr;
}


void resize(DynamicArray *arr)
{
    arr->capacity *= 2;
    arr->data = realloc(arr->data, sizeof(int) * arr->capacity);
}


void append(DynamicArray *arr, int value)
{
    if (arr->size >= arr->capacity) {
        resize(arr);
    }
    arr->data[arr->size] = value;
    arr->size++;
    arr->capacity--;
}


void insert(DynamicArray *arr, int index, int value)
{
    if (index < 0 || index > arr->size) {
        puts("Error: Index out of range");
        return;
    }

    if (arr->size >= arr->capacity) {
        resize(arr);
    }

    for (int i = arr->size; i > index; i--) {
        arr->data[i] = arr->data[i - 1];
    }
    arr->data[index] = value;
    arr->size++;
}


void delete(DynamicArray *arr, int index)
{
    if (index < 0 || index > arr->size) {
        puts("Error: Index out of range");
        return;
    }

    for (int i = index; i < arr->size - 1; i++) {
        arr->data[i] = arr->data[i + 1];
    }
    arr->size--;
}


int get(DynamicArray arr, int index)
{
    if (index < 0 || index > arr.size) {
        puts("Error: Index out of range");
        return -1;
    }
    return arr.data[index];
}

int pop(DynamicArray *arr)
{
    if (arr->size == 0) {
        puts("Error: pop from empty array");
        return -1;
    }
    int value = arr->data[arr->size - 1];
    arr->size--;
    arr->capacity++;
    return value;
}


void free_array(DynamicArray *arr)
{
    free(arr->data);
}



int main(void)
{
    DynamicArray arr = init(4);
    insert(&arr, 0, 5);
    append(&arr, 15);
    append(&arr, 184);

    for (int i = 0; i < arr.size; i++) {
        printf("%d ", get(arr, i));
    }
    printf("\n");
    int last_arr_element = pop(&arr);
    printf("Last array element: %d\n", last_arr_element);

    delete(&arr, 0);
    for (int i = 0; i < arr.size; i++) {
        printf("%d ", get(arr, i));
    }
    printf("\n");
    free_array(&arr);

    return 0;
}