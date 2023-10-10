#include "lists.h"

/**
 * check_cycle - tests if it has a cycle
 * @list: *head
 * Return: 0 if there isnt, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	if (hare == NULL)
		return (0);

	while (tortoise != hare)
	{
		if (hare->next == NULL || hare->next->next == NULL)
			return (0);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (1);
}
