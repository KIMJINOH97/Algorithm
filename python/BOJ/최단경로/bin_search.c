#include <stdio.h>
#include <stdlib.h>

struct node
{

    int location;
    int value;
    struct node *next;
};

struct node *start = NULL;

void binary(int a, int b)
{
    struct node *link = (struct node *)malloc(sizeof(struct node));

    link->location = a;
    link->value = b;

    link->next = start;

    start = link;
}

struct node *find(int key)
{
    struct node *now = start;

    while (now->location != key)
    {
        if (now->next == NULL)
        {
            return NULL;
        }
        else
        {
            now = now->next;
        }
    }
    return now;
}

int binsearch(int searchnum, int left, int right)
{
    struct node *now = start;

    if (now->value == searchnum)
    {
        return now->location;
    }

    while (now->value != searchnum && left <= right)
    {
        int middle = (left + right) / 2;
        struct node *Link = find(middle);
        printf("hhhhh  hh %d\n", middle);

        if (Link->value < searchnum)
        {
            printf("%d이(가) %d보다 큽니다. %d보다 큰 영역 탐색합니다.\n", searchnum, Link->value, Link->value);
            left = middle + 1;
        }

        else if (Link->value > searchnum)
        {
            printf("%d이(가) %d보다 작습니다. %d보다 작은 영역 탐색합니다.\n", searchnum, Link->value, Link->value);
            right = middle - 1;
        }

        else if (Link->value == searchnum)
        {
            return middle;
        }
    }
}

int main()
{
    int i = 1;
    int num, result;

    binary(1, 1);
    binary(2, 3);
    binary(3, 5);
    binary(4, 6);
    binary(5, 7);
    binary(6, 8);
    binary(7, 11);
    binary(8, 12);
    binary(9, 14);
    binary(10, 15);
    binary(11, 24);
    binary(12, 26);
    binary(13, 42);
    binary(14, 43);
    binary(15, 48);
    binary(16, 49);
    binary(17, 51);
    binary(18, 55);
    binary(19, 56);
    binary(20, 59);
    binary(21, 66);
    binary(22, 67);
    binary(23, 69);
    binary(24, 70);
    binary(25, 71);
    binary(26, 73);
    binary(27, 75);
    binary(28, 80);
    binary(29, 96);
    binary(30, 99);

    while (i <= 6)
    {
        printf("%d. find your number ", i);
        scanf_s("%d", &num);
        result = binsearch(num, 1, 30);
        printf("%d 's which = %d", num, result);
        printf("\n");
        i++;
    }
    return 0;
}