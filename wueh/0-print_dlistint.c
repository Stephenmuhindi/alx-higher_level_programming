#include "lists.h"

/**
 * print_dlistint - displ. all the elements of a dlistint_t list.
 * @h: *list
 * Return: count
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *current;
	size_t count;

	current = (dlistint_t *) h;
	count = 0;
	while (current)
	{
		count++;
		printf("%d\n", current->n);
		current = current->next;
	}
	return (count);
}
