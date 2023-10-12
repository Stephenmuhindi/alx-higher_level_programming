#include "lists.h"

/**
 * sum_dlistint - calculates sum
 * @head: *head
 * Return: sum
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current;
	int sum = 0;

	if (head == NULL)
		return (sum);
	current = head;
	while (current)
	{
		sum += current->n;
		current = current->next;
	}
	return (sum);
}
