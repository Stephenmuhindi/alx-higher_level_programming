#include "lists.h"

/**
 * free_dlistint - rees lst
 * @head: *head
 * Return: naught
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	current = head;
	while (head)
	{
		head = head->next;
		free(current);
		current = head;
	}
}
